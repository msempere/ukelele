grammar ukelele;

@header {
from symbolsTable import SymbolsTable, Scope, Stype
from utilities import error_message, error_message_without_line, already_defined_message, reserved_word_message
}

options {
    language=Python;
}

@parser::members{
    self.types = {'int': 'int32', 'string': 'string', 'bool': 'bool', 'float': 'float32'}
    self.RESERVED_WORDS = ['int', 'string', 'float', 'main', 'bool', 'Print', 'Println', 'auto', 'True', 'False']
    self.branches = 0
}


/* ----- GRAMMAR RULES ----- */
s[SymbolsTable ts] returns [String code]
@init{
$code = ".assembly __ukelele__cil__file__ {}\n.assembly extern mscorlib {}\n\n"
}
    : (from_funcdef=funcdef[$ts, Scope.BLOCK_LOCAL] {$code += $from_funcdef.code} )*
{
if not $ts.get('main'):
    error_message_without_line('"main" not defined')
}
    ;


funcdef[SymbolsTable ts, String scope] returns [String code]
@init{
$code = ""
}
    : DEF IDENTIFIER {$code += ".method static "} params=parameters type_specifier {$code +=$type_specifier.text + ' '} 
{
if $IDENTIFIER.text == 'main':
    $ts.add(name=$IDENTIFIER.text, stype=($type_specifier.text, Stype.METHOD), isFunction=True, scope=Scope.GLOBAL, line=$IDENTIFIER.line)
    $code += "Main" + $params.text + " cil managed {\n.entrypoint\n"
else:
    $ts.add(name=$IDENTIFIER.text, stype=($type_specifier.text, Stype.METHOD), isFunction=True, scope=Scope.GLOBAL, line=$IDENTIFIER.line)
    $code += $IDENTIFIER.text + $params.text + " cil managed {\n"
ts_son = SymbolsTable($ts)
} 

    from_block=block[ts_son, $scope, $type_specifier.text]
{
# if there is no return and the type defined is void, should be OK
#if (not $from_block.type_out) and ($type_specifier.text == 'void'):
#    pass
#else:
#    # if types differ, throw error
#    if $from_block.type_out != $type_specifier.text:
#        error_message('"' + $IDENTIFIER.text + '" with type "' + $type_specifier.text + '" returning "' + $from_block.type_out + '"', $IDENTIFIER.line)

$code += ".maxstack " + str($from_block.stack_out) + "\n" + '.locals init ('
local_vars = []
for t,n,i in $from_block.locals:
    if '[' and ']' in t:
        array_type = t.split('[')[0]
        local_vars.append(t.replace(array_type, self.types[array_type])  + ' ' +  n + '_' + str(i))
    else:
        if t == 'int':
            local_vars.append('int32 ' + n + '_' + str(i))
        elif t == 'bool':
            local_vars.append('bool ' + n + '_' + str(i))
        elif t == 'float':
            local_vars.append('float32 ' + n + '_' + str(i))
$code += ','.join(local_vars) + ')\n'

$code += $from_block.body 
#if $type_specifier.text == 'void':
#    $code += 'ret\n'
$code += "}\n"
}
    ;

/*block : LBRACKET declins RBRACKET*/
/*declins : ( instr | decl )**/

block[SymbolsTable ts, String scope, String expected_return] returns [Int stack_out, String body, List locals, String type_out]
@init
{
$body = ''
$stack_out = 0
$locals = []
}
    : LBRACKET from_declins=declins[ts, $scope, $expected_return]
{
$type_out = $from_declins.type_out
$locals += $from_declins.locals
$stack_out += $from_declins.stack_out
$body += $from_declins.body
}
    RBRACKET
    ;


declins[SymbolsTable ts, String scope, String expected_return] returns [Int stack_out, String body, List locals, String type_out]
@init
{
$stack_out = 0
$locals = []
$body = ''
}
    : ( from_instr=instr[ts, $scope, $expected_return]
{
$type_out = $from_instr.type_out
$locals += $from_instr.locals
$stack_out += $from_instr.stack_out 
$body += $from_instr.body
}
    | from_decl=decl[ts, $scope]
{
$locals += $from_decl.locals
$stack_out += $from_decl.stack_out 
$body += $from_decl.body
}
    )*
    ;


decl[SymbolsTable ts, String scope] returns [Int stack_out, String body, List locals]
@init
{
assignation = False
dimensions = 0
numelements = 0
$body = ""
$stack_out = 0
$locals = []
}
    : type_simple IDENTIFIER (ASSIGN from_expr=expr[ts, $scope]{assignation=True})?
{
if not $IDENTIFIER.text in self.RESERVED_WORDS:
    element = $ts.get($IDENTIFIER.text)

    if not element:
        $ts.add(name=$IDENTIFIER.text, stype=$type_simple.text, isFunction=False, scope=$scope, line=$IDENTIFIER.line)
        element = $ts.get($IDENTIFIER.text)

        if $type_simple.text == 'auto' and not assignation:
            error_message('Type for variable "' + $IDENTIFIER.text + '" can not be deducted', $IDENTIFIER.line)

        if $type_simple.text != 'auto':
            $locals.append(($type_simple.text, $IDENTIFIER.text, element.index))
        
        if assignation:
            if $type_simple.text == 'auto':
                identifier = $ts.get($IDENTIFIER.text)
                identifier.stype = $from_expr.type_out
                $locals.append(($from_expr.type_out, $IDENTIFIER.text, identifier.index))

            $stack_out += $from_expr.stack_out 
            $body += $from_expr.expr_out + 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
            assignation = False
    else:
        if $scope == Scope.LOOP:
            error_message('"' + $IDENTIFIER.text + '" shadows a variable', $IDENTIFIER.line)
        else:
            already_defined_message($IDENTIFIER.text, $IDENTIFIER.line, element.line)
else:
    reserved_word_message($IDENTIFIER.text, $IDENTIFIER.line)
}
    ( COMMA IDENTIFIER (ASSIGN{assignation=True}expr[ts, $scope])? 
{
if not $IDENTIFIER.text in self.RESERVED_WORDS:
    element = $ts.get($IDENTIFIER.text, $scope != Scope.LOOP)
    if not element:
        $ts.add(name=$IDENTIFIER.text, stype=$type_simple.text, isFunction=False, scope=$scope, line=$IDENTIFIER.line)
        element = $ts.get($IDENTIFIER.text, $scope != Scope.LOOP)

        if $type_simple.text != 'auto':
            $locals.append(($type_simple.text, $IDENTIFIER.text, element.index))

        
        if assignation:
            if $type_simple.text == 'auto':
                identifier = $ts.get($IDENTIFIER.text)
                identifier.stype = $from_expr.type_out
                $locals.append(($from_expr.type_out, $IDENTIFIER.text, identifier.index))

            $stack_out += $from_expr.stack_out 
            $body += $from_expr.expr_out + 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
            assignation = False
    else:
        already_defined_message($IDENTIFIER.text, $IDENTIFIER.line, element.line)
else:
    reserved_word_message($IDENTIFIER.text, $IDENTIFIER.line)
}
    )* SEMICOLON

    | type_simple IDENTIFIER LCOR from_dims=dims RCOR
{
dimensions = 1
elements = [$from_dims.body]
}
    (LCOR from_another_dims=dims RCOR
{
dimensions += 1
elements.append($from_another_dims.body)
}
    )* SEMICOLON
{
dims = '[' 
if dimensions > 1:
    for i in range(dimensions):
        dims += ','
dims += ']'
$ts.add(name=$IDENTIFIER.text, stype=$type_simple.text + dims, isFunction=False, scope=Scope.BLOCK_LOCAL if not $scope else $scope, line=$IDENTIFIER.line)
$locals.append(($type_simple.text + dims, $IDENTIFIER.text, $ts.get($IDENTIFIER.text).index))

$body += 'ldc.i4 ' + str(reduce(lambda x, y: int(x)*int(y), elements)) + '\n'
$stack_out += 1
$body += 'newarr [mscorlib]System.Int32\n'
$body += 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
}
    ;


instr[SymbolsTable ts, String scope, String expected_return] returns [Int stack_out, String body, List locals, String type_out]
@init
{
ts_son = None
$stack_out = 0
$body = ""
$locals = []
initialize = False
}
    : operation=print_operation[0, $ts, $scope]
{
$stack_out += $operation.stack_out
$body += $operation.operation
}
    | from_block=block[$ts, $scope, $expected_return]
{
$type_out = $from_block.type_out
$stack_out = $from_block.stack_out
$body += $from_block.body
}
    | IF condition=expr[$ts, $scope] from_instr=instr[$ts, $scope, $expected_return]
{
$stack_out += 1
self.branches += 1
$locals = $from_instr.locals
$body += $expr.expr_out + 'ldc.i4 1\n'
$body += 'beq L' + str(self.branches) + '\n'
}
    (ELSE from_another_instr=instr[$ts, $scope, $expected_return]
{
$stack_out += max($from_instr.stack_out, $from_another_instr.stack_out)
$body += $from_another_instr.body
$body += 'br L' + str(self.branches + 1) + '\n'
}
    )?
{
$body += 'L' + str(self.branches) + ':\n'
self.branches += 1
$body += $from_instr.body
$body += 'L' + str(self.branches) + ':\n'
}
    | IDENTIFIER (COLON{initialize=True})?ASSIGN from_expr=expr[$ts, $scope] SEMICOLON
{
element = $ts.get($IDENTIFIER.text)

if element:
    if not initialize:
        $stack_out += $from_expr.stack_out
        $body += $from_expr.expr_out + 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
else:
    error_message('"' + $IDENTIFIER.text + '" not defined', $IDENTIFIER.line)
}
    | IDENTIFIER LCOR pos=expr[$ts, $scope] RCOR
{
element = $ts.get($IDENTIFIER.text)

if element:
    array = $ts.get($IDENTIFIER.text)
    if array:
        $stack_out += $pos.stack_out + 1
        $body += 'ldloc ' + str(array.index) + '\n' + $pos.expr_out
else:
    error_message('"' + $IDENTIFIER.text + '" not defined', $IDENTIFIER.line)
}
    (LCOR another_pos=expr[$ts, $scope] RCOR
{
if array:
    $stack_out += $another_pos.stack_out
    $body += $another_pos.expr_out + 'mul\n'
}
    )* ASSIGN new_value=expr[$ts, $scope] SEMICOLON
{
if array:
    $body += $new_value.expr_out + 'stelem.'

    if $new_value.type_out == 'int' or $new_value.type_out == 'bool':
        $body += 'i4\n'
    elif $new_value.type_out == 'float':
        $body += 'r4\n'
    elif $new_value.type_out == 'string':
        $body = $body[:-1] + '\n'
}
    | FOR from_forexpr=forexpr[$ts, $expected_return]
{
$type_out = $from_forexpr.type_out
$stack_out += $from_forexpr.stack_out 
$body += $from_forexpr.body
$locals = $from_forexpr.locals
}
    | DO {ts_son = SymbolsTable($ts)} from_block=block[ts_son, Scope.LOOP, $expected_return] WHILE LPAREN comparison=expr[$ts, $scope] RPAREN
{
$type_out = $from_block.type_out
self.branches += 1
$locals = $from_block.locals
init_branch = self.branches
$stack_out += $from_block.stack_out + 1 + $comparison.stack_out
$body += 'L' + str(init_branch) + ':\n'
$body += $from_block.body + $comparison.expr_out + 'ldc.i4 1\nbeq L' + str(init_branch) + '\n'
}
    | WHILE LPAREN comparison=expr[$ts, $scope] RPAREN {ts_son = SymbolsTable($ts)} from_block=block[ts_son, Scope.LOOP, $expected_return]
{
$type_out = $from_block.type_out
self.branches += 1
$locals = $from_block.locals
init_branch = self.branches
$stack_out += $comparison.stack_out + 1 + $from_block.stack_out
$body += 'L' + str(init_branch) + ':\n'
self.branches += 1
$body += $comparison.expr_out + 'ldc.i4 1\nbne.un L' + str(self.branches) + '\n' + $from_block.body + 'br L' + str(init_branch) + '\n' 
$body += 'L' + str(self.branches) + ':\n'
}
    | RETURN LPAREN{void_expr=True} (from_expr=expr[$ts, $scope]
{
$type_out = $from_expr.type_out
$stack_out += $from_expr.stack_out
$body += $from_expr.expr_out
void_expr = False
}
    )? RPAREN SEMICOLON
{
$type_out = '' if not $type_out else $type_out

if void_expr:
    if $expected_return == 'void':
        pass
    else:
        error_message('Excepted returning "' + $expected_return + '", and got "' + $type_out + '"', $RETURN.line)
else:
    if $expected_return == 'void':
        error_message('Returning a not empty value while expecting void', $RETURN.line)
    else:
        if $type_out != $expected_return:
            error_message('Excepted returning "' + $expected_return + '", and got "' + $type_out + '"', $RETURN.line)

$body += 'ret\n'
}
    ;

dims returns [String body]
@init{
$body = ""
}
    : INTEGER 
{
$body += $INTEGER.text
}
    ;

forexpr[SymbolsTable ts, String expected_return] returns [Int stack_out, String body, List locals, String type_out]
@init{
ts_son = SymbolsTable($ts)
$stack_out = 0
$body = ""
$locals = []
}
    :  LPAREN initial_decl=decl[ts_son, Scope.LOOP]
{
$stack_out += $initial_decl.stack_out 
$body += $initial_decl.body
$locals += $initial_decl.locals
}
    comparison=expr[ts_son, Scope.LOOP] SEMICOLON IDENTIFIER
{
element = ts_son.get($IDENTIFIER.text)

if not element:
    error_message('"' + $IDENTIFIER.text + '" not defined', $IDENTIFIER.line)
}
    (COLON)? ASSIGN post_comparison=expr[ts_son, Scope.LOOP] RPAREN body_for=block[ts_son, Scope.LOOP, $expected_return]
{
$type_out = $body_for.type_out
$locals += $body_for.locals
self.branches += 1
init_branch = self.branches
$body += 'L' + str(init_branch) + ':\n'
$stack_out += $comparison.stack_out + 1 + $body_for.stack_out 
self.branches += 1
$body += $comparison.expr_out + 'ldc.i4 1\nbne.un L' + str(self.branches) + '\n' + $body_for.body 
$body += $post_comparison.expr_out + 'stloc.' + str(ts_son.get($IDENTIFIER.text).index) + '\n'
$body += 'br L' + str(init_branch) + '\nL' + str(self.branches) + ':\n'
}
    ;

assignment_operator
    : ASSIGN
    ;

type_specifier
    : INT
    | VOID
    | STRING
    ;

type_simple
    : INT
    | STRING
    | FLOAT
    | BOOL
    | AUTO
    ;

print_operation[Int stack_in, SymbolsTable ts, Scope scope] returns [Int stack_out, String operation] 
@init {
$operation = ""
ln = False
}
    : 
    (   PRINT 
    |   PRINTLN {ln=True} 
    ) LPAREN from_expr=expr[$ts, $scope] RPAREN SEMICOLON 
{
if ln:
    $operation += $from_expr.expr_out + "call void [mscorlib]System.Console::WriteLine( " + self.types[$from_expr.type_out] + " )\n"
else:
    $operation += $from_expr.expr_out + "call void [mscorlib]System.Console::Write( " + self.types[$from_expr.type_out] + " )\n"
$stack_out = $from_expr.stack_out
}
    ;


parameters returns [String params]
@init{
$params = ""
}
    : LPAREN {$params += "("} (argument_expression_list)? RPAREN {$params += ") "}
    ;

argument_expression_list
    :   definition (',' definition)*
    ;

definition
    : type_specifier IDENTIFIER
    ;

expr[SymbolsTable ts, String scope] returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
} : from_eand=eand[ts, '', $scope]{
$stack_out = $from_eand.stack_out
$expr_out = $from_eand.expr_out
$type_out = $from_eand.type_out
}
( OR from_eand=eand[ts, $type_out, $scope]
{
$stack_out += $from_eand.stack_out
$expr_out += $from_eand.expr_out + 'or\n'
$type_out = $from_eand.type_out
}
)* ;


eand[SymbolsTable ts, String type_in, String scope]  returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}: from_erel=erel[ts, type_in, $scope]{
$stack_out = $from_erel.stack_out
$expr_out = $from_erel.expr_out
$type_out = $from_erel.type_out
}
( AND from_erel=erel[ts, $type_out, $scope]
{
$stack_out += $from_erel.stack_out
$expr_out += $from_erel.expr_out + 'and\n'
$type_out = $from_erel.type_out
}
)* ;


erel[SymbolsTable ts, String type_in, String scope]  returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}: from_esum=esum[ts, type_in, $scope]
{
$stack_out = $from_esum.stack_out
$expr_out = $from_esum.expr_out
$type_out = $from_esum.type_out
}
( RELOP from_esum=esum[ts, $type_out, $scope]
{
$stack_out += $from_esum.stack_out
$expr_out += $from_esum.expr_out
self.branches += 1

if $RELOP.text == '==':
    $expr_out += 'beq L'

elif $RELOP.text == '!=':
    $expr_out += 'bne.un L'

elif $RELOP.text == '>':
    $expr_out += 'bgt L'

elif $RELOP.text == '<':
    $expr_out += 'blt L'

elif $RELOP.text == '>=':
    $expr_out += 'bge L'

elif $RELOP.text == '<=':
    $expr_out += 'ble L'

$expr_out += str(self.branches) + '\n' + 'ldc.i4 0\n' + 'br L' + str(self.branches + 1) + '\n'
$expr_out += 'L' + str(self.branches) + ':\nldc.i4 1\nL' + str(self.branches + 1) + ':\n'
self.branches += 1
$type_out = 'bool'

})* ;


esum[SymbolsTable ts, String type_in, String scope]  returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}: from_term=term[ts, type_in, $scope]
{
$stack_out = $from_term.stack_out
$expr_out = $from_term.expr_out
$type_out = $from_term.type_out
}
( ADDOP from_another_term=term[ts, $type_out, $scope]
{
$stack_out += $from_another_term.stack_out
$expr_out += $from_another_term.expr_out

if $ADDOP.text == '+':
    $expr_out += 'add' + '\n'
else:
    $expr_out += 'sub' + '\n'
$type_out = $from_another_term.type_out
}
)* ;


term[SymbolsTable ts, String type_in, String scope]  returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}: from_factor=factor[ts, type_in, $scope]
{
$stack_out = $from_factor.stack_out
$expr_out = $from_factor.expr_out
$type_out = $from_factor.type_out
}
( MULOP from_another_factor=factor[ts, $type_out, $scope]
{
$stack_out += $from_another_factor.stack_out
$expr_out += ('conv.r8\n' if $MULOP.text == '/' else '') + $from_another_factor.expr_out 

if $MULOP.text == '*':
    $expr_out += 'mul' + '\n'
    $type_out = $from_another_factor.type_out
else:
    if $from_another_factor.type_out != 'float':
        $expr_out += 'conv.r8\n'
    $expr_out += 'div' + '\n'
    $type_out = 'float'
}
)* ;


factor[SymbolsTable ts, String type_in, String scope] returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}
    : from_base=base[ts, type_in, $scope]
{
$stack_out = $from_base.stack_out
$expr_out = $from_base.expr_out
$type_out = $from_base.type_out
}
    | NOT factor[ts, type_in, $scope]
    |LPAREN ADDOP from_factor=factor[ts, type_in, $scope]
{
$stack_out = $from_factor.stack_out
$expr_out = $from_factor.expr_out + 'neg\n' if $ADDOP.text == '-' else ''
$type_out = $from_factor.type_out
}
    RPAREN ;


base[SymbolsTable ts, String type_in, String scope] returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}
    : INTEGER
{
$stack_out = 1
$expr_out = 'ldc.i4 ' + $INTEGER.text + '\n'
$type_out = 'int'
if $type_in == 'float':
    $expr_out += 'conv.r8\n'
    $type_out = 'float'
}
    | TEXT
{
$stack_out = 1
$expr_out = 'ldstr ' + $TEXT.text + '\n'
$type_out = 'string'
}
    | REAL
{
$stack_out = 1
$expr_out = 'ldc.r4 ' + $REAL.text + '\n'
$type_out = 'float'
}
    | BOOLEANO
{
$stack_out = 1
$expr_out = 'ldc.i4 1\n' if $BOOLEANO.text == 'True' else 'ldc.i4 0\n'
$type_out = 'bool'
}
    | LPAREN from_expr=expr[ts, $scope]
{
$stack_out = $from_expr.stack_out
$expr_out = $from_expr.expr_out
$type_out = $from_expr.type_out
}
    RPAREN
    | IDENTIFIER
{
element = $ts.get($IDENTIFIER.text)

if not element:
    error_message('"' + $IDENTIFIER.text + '" not defined', $IDENTIFIER.line)
else:
    #if element.scope == Scope.LOOP and scope != Scope.LOOP:
    #    error_message('"' + $IDENTIFIER.text + '" not defined in this scope', $IDENTIFIER.line)
    #else:
    $expr_out = 'ldloc ' + str(element.index) + '\n'
    $stack_out = 1
    $type_out = element.stype

    if $type_in == 'float':
        if $type_out == 'int':
            $expr_out += 'conv.r8\n'
            $type_out = 'float'
}
    | IDENTIFIER LCOR from_expr=expr[ts, $scope] RCOR
{
array = $ts.get($IDENTIFIER.text)
if array:
    $expr_out += 'ldloc ' + str(array.index) + '\n' + $from_expr.expr_out
    $stack_out += $from_expr.stack_out + 1
}
    (LCOR from_another_expr=expr[ts, $scope] RCOR
{
if array:
    $expr_out += $from_another_expr.expr_out + 'mul\n'
    $stack_out += $from_another_expr.stack_out
}
    )*
{
array = $ts.get($IDENTIFIER.text)
if array:
    array_type = array.stype.split('[')[0]
    if array_type == 'int':
        $expr_out += 'ldelem.i4' + '\n'
        $stack_out +=  1
        $type_out = 'int'

    elif array_type == 'float':
        $expr_out += 'ldelem.r4' + '\n'
        $stack_out +=  1
        $type_out = 'float'

    elif array_type == 'bool':
        $expr_out += 'ldelem.i4' + '\n'
        $stack_out +=  1
        $type_out = 'bool'

    elif array_type == 'string':
        $expr_out += 'ldelem' + '\n'
        $stack_out +=  1
        $type_out = 'string'
}
    | POSTADDOP IDENTIFIER
{
$expr_out += 'ldloc ' + str($ts.get($IDENTIFIER.text).index) + '\n'

if $ts.get($IDENTIFIER.text).stype  == 'int':
    $expr_out += 'ldc.i4 1\nadd\n' if $POSTADDOP.text == '++' else 'ldc.i4 1\nsub\n'
elif $ts.get($IDENTIFIER.text).stype  == 'float':
    $expr_out += 'ldc.r4 1\nadd\n' if $POSTADDOP.text == '++' else 'ldc.r4 1\nsub\n'

$expr_out += 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
$expr_out += 'ldloc ' + str($ts.get($IDENTIFIER.text).index) + '\n'
$stack_out += 3
$type_out = 'int'
}
    | IDENTIFIER POSTADDOP
{
$expr_out += 'ldloc ' + str($ts.get($IDENTIFIER.text).index) + '\n'
$expr_out += 'ldloc ' + str($ts.get($IDENTIFIER.text).index) + '\n'

if $ts.get($IDENTIFIER.text).stype  == 'int':
    $expr_out += 'ldc.i4 1\nadd\n' if $POSTADDOP.text == '++' else 'ldc.i4 1\nsub\n'
elif $ts.get($IDENTIFIER.text).stype  == 'float':
    $expr_out += 'ldc.r4 1\nadd\n' if $POSTADDOP.text == '++' else 'ldc.r4 1\nsub\n'

$expr_out += 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
$stack_out += 3
$type_out = 'int'
}   
    ;

fragment ESCAPED_QUOTE : '\\"';

/* ----- LEXICAL RULES ----- */
VOID : 'void';
INT : 'int';
STRING : 'string';
FLOAT : 'float';
DEF : 'def';
FOR : 'for';
DO : 'do';
WHILE : 'while';
IF : 'if';
ELSE : 'else';
RETURN : 'return';
PRINT : 'print';
PRINTLN : 'println';
BOOL : 'bool';
AUTO : 'auto';
OR : 'or';
NOT : 'not';
AND : 'and';
POSTADDOP: '++' | '--';
RELOP : '=='|'!='|'<' | '>' | '<=' | '>=';
ADDOP : '+' | '-';
MULOP : '*' | '/';
BOOLEANO : 'True' | 'False';
TEXT :   '"' ( ESCAPED_QUOTE | ~('\n'|'\r') )*? '"';
IDENTIFIER : LETTER (LETTER|'0'..'9')* ;
LETTER : 'A'..'Z' | 'a'..'z' | '_' ;
INTEGER : '0'..'9' DIGITS* ;
REAL    :   ('0'..'9')+'.'('0'..'9')+;
DIGITS : ( '0' .. '9' )+ ;
COLON: ':';
ASSIGN : '=';
SEMICOLON : ';';
LPAREN    : '(';
RPAREN    : ')';
LCOR : '[';
RCOR : ']';
LBRACKET    : '{';
RBRACKET    : '}';
COMMA: ',';

BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;

WS  :  (' '|'\r'|'\t'|'\u000C'|'\n') -> skip
    ;

