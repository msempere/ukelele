grammar ukelele;

@header {
from symbolsTable import SymbolsTable, Scope, Stype
}

options {
    language=Python;
}

@parser::members{
    self.types = {'int': 'int32', 'string': 'string', 'bool': 'bool', 'float': 'float32'}
    self.branches = 0
}


/* ----- GRAMMAR RULES ----- */
s[SymbolsTable ts] returns [String code]
@init{
$code = ".assembly __ukelele__cil__file__ {}\n.assembly extern mscorlib {}\n\n"
}
    : (from_funcdef=funcdef[$ts] {$code += $from_funcdef.code} )*
    ;


funcdef[SymbolsTable ts] returns [String code]
@init{
$code = ""
}
    : DEF IDENTIFIER {$code += ".method static "} params=parameters type_specifier {$code +=$type_specifier.text + ' '} 
{
if $IDENTIFIER.text == 'main':
    $ts.add(name=$IDENTIFIER.text, stype=($type_specifier.text, Stype.METHOD), isFunction=True, scope=Scope.GLOBAL)
    $code += "Main" + $params.text + " cil managed {\n.entrypoint\n"
else:
    $ts.add(name=$IDENTIFIER.text, stype=($type_specifier.text, Stype.METHOD), isFunction=True, scope=Scope.GLOBAL)
    $code += $IDENTIFIER.text + $params.text + " cil managed {\n"
ts_son = SymbolsTable($ts)
} 

    from_block=block[ts_son]
{
$code += ".maxstack " + str($from_block.stack_out) + "\n" + '.locals init ('
local_vars = []
for t,n in $from_block.locals:
    i = 0
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
if $type_specifier.text == 'void':
    $code += 'ret\n'
$code += "}\n"
}
    ;

/*block : LBRACKET declins RBRACKET*/
/*declins : ( instr | decl )**/

block[SymbolsTable ts] returns [Int stack_out, String body, List locals]
@init
{
$body = ''
$stack_out = 0
$locals = []
}
    : LBRACKET from_declins=declins[ts]
{
$locals += $from_declins.locals
$stack_out += $from_declins.stack_out
$body += $from_declins.body
}
    RBRACKET
    ;


declins[SymbolsTable ts] returns [Int stack_out, String body, List locals]
@init
{
$stack_out = 0
$locals = []
$body = ''
}
    : ( from_instr=instr[ts]
{
$locals += $from_instr.locals
$stack_out += $from_instr.stack_out 
$body += $from_instr.body
}
    | from_decl=decl[ts, '']
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
    : type_simple IDENTIFIER (ASSIGN from_expr=expr[ts]{assignation=True})?
{

if not $ts.get($IDENTIFIER.text):
    if $type_simple.text != 'auto':
        $locals.append(($type_simple.text, $IDENTIFIER.text))

    $ts.add(name=$IDENTIFIER.text, stype=$type_simple.text, isFunction=False, scope=Scope.BLOCK_LOCAL if not $scope else $scope)
    
    if assignation:
        if $type_simple.text == 'auto':
            identifier = $ts.get($IDENTIFIER.text)
            identifier.stype = $from_expr.type_out
            $locals.append(($from_expr.type_out, $IDENTIFIER.text))

        $stack_out += $from_expr.stack_out 
        $body += $from_expr.expr_out + 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
        assignation = False
else:
    if $scope == Scope.FOR_LOOP:
        print($IDENTIFIER.text + ' shadows a var')
    else:
        print($IDENTIFIER.text + ' already defined')
}
    ( COMMA IDENTIFIER (ASSIGN{assignation=True}expr[ts])? )* SEMICOLON

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
$locals.append(($type_simple.text + dims, $IDENTIFIER.text))
$ts.add(name=$IDENTIFIER.text, stype=$type_simple.text + dims, isFunction=False, scope=Scope.BLOCK_LOCAL if not $scope else $scope)

$body += 'ldc.i4 ' + str(reduce(lambda x, y: int(x)*int(y), elements)) + '\n'
$stack_out += 1
$body += 'newarr [mscorlib]System.Int32\n'
$body += 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
}
    ;


instr[SymbolsTable ts] returns [Int stack_out, String body, List locals]
@init
{
ts_son = None
$stack_out = 0
$body = ""
$locals = []
initialize = False
}
    : operation=print_operation[0, $ts]
{
$stack_out += $operation.stack_out
$body += $operation.operation
}
    | from_block=block[$ts]
{
$stack_out = $from_block.stack_out
$body += $from_block.body
}
    | IF condition=expr[$ts] from_instr=instr[$ts]
{
$stack_out += 1
self.branches += 1
$body += $expr.expr_out + 'ldc.i4 1\n' + 'beq L' + str(self.branches) + '\n'
}
    (ELSE from_another_instr=instr[$ts]
{
$stack_out += max($from_instr.stack_out, $from_another_instr.stack_out)
$body += $from_another_instr.body + 'br L' + str(self.branches + 1) + '\n'
}
    )?
{
$body += 'L' + str(self.branches) + ':\n'
self.branches += 1
$body += $from_instr.body +  'L' + str(self.branches) + ':\n'
}
    | IDENTIFIER (COLON{initialize=True})?ASSIGN from_expr=expr[$ts] SEMICOLON
{
if not initialize:
    $stack_out += $from_expr.stack_out 
    $body += $from_expr.expr_out + 'stloc.' + str($ts.get($IDENTIFIER.text).index) + '\n'
} 
    | IDENTIFIER LCOR pos=expr[$ts] RCOR
{
array = $ts.get($IDENTIFIER.text)
if array:
    $stack_out += $pos.stack_out + 1
    $body += 'ldloc ' + str(array.index) + '\n' + $pos.expr_out
}
    (LCOR another_pos=expr[$ts] RCOR
{
if array:
    $stack_out += $another_pos.stack_out
    $body += $another_pos.expr_out + 'mul\n'
}
    )* ASSIGN new_value=expr[$ts] SEMICOLON
{
if array:
    $body += $new_value.expr_out + 'stelem.'

    if $new_value.type_out == 'int' or $new_value.type_out == 'bool':
        $body += 'i4\n'
    elif $new_value.type_out == 'float':
        $body += 'r4\n'
}
    | FOR from_forexpr=forexpr[$ts]
{
$stack_out += $from_forexpr.stack_out 
$body += $from_forexpr.body
$locals = $from_forexpr.locals
}
    | DO {ts_son = SymbolsTable($ts)} from_block=block[ts_son] WHILE LPAREN comparison=expr[$ts] RPAREN
{
self.branches += 1
init_branch = self.branches
$stack_out += $from_block.stack_out + 1 + $comparison.stack_out
$body += 'L' + str(init_branch) + ':\n'
$body += $from_block.body + $comparison.expr_out + 'ldc.i4 1\nbeq L' + str(init_branch) + '\n'
}
    | WHILE LPAREN comparison=expr[ts] RPAREN {ts_son = SymbolsTable($ts)} from_block=block[ts_son]
{
self.branches += 1
init_branch = self.branches
$stack_out += $comparison.stack_out + 1 + $from_block.stack_out
$body += 'L' + str(init_branch) + ':\n'
self.branches += 1
$body += $comparison.expr_out + 'ldc.i4 1\nbne.un L' + str(self.branches) + '\n' + $from_block.body + 'br L' + str(init_branch) + '\n' 
$body += 'L' + str(self.branches) + ':\n'
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

forexpr[SymbolsTable ts] returns [Int stack_out, String body, List locals]
@init{
ts_son = SymbolsTable($ts)
$stack_out = 0
$body = ""
$locals = []
}
    :  LPAREN initial_decl=decl[ts_son, Scope.FOR_LOOP]
{
$stack_out += $initial_decl.stack_out 
$body += $initial_decl.body
$locals = $initial_decl.locals
}
    comparison=expr[ts_son] SEMICOLON IDENTIFIER (COLON)? ASSIGN post_comparison=expr[ts_son] RPAREN body_for=block[ts_son]
{
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

print_operation[Int stack_in, SymbolsTable ts] returns [Int stack_out, String operation] 
@init {
$operation = ""
ln = False
}
    : 
    (   PRINT 
    |   PRINTLN {ln=True} 
    ) LPAREN from_expr=expr[$ts] RPAREN SEMICOLON 
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

expr[SymbolsTable ts] returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
} : from_eand=eand[ts, '']{
$stack_out = $from_eand.stack_out
$expr_out = $from_eand.expr_out
$type_out = $from_eand.type_out
}
( OR from_eand=eand[ts, $type_out]
{
$stack_out += $from_eand.stack_out
$expr_out += $from_eand.expr_out + 'or\n'
$type_out = $from_eand.type_out
}
)* ;


eand[SymbolsTable ts, String type_in]  returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}: from_erel=erel[ts, type_in]{
$stack_out = $from_erel.stack_out
$expr_out = $from_erel.expr_out
$type_out = $from_erel.type_out
}
( AND from_erel=erel[ts, $type_out]
{
$stack_out += $from_erel.stack_out
$expr_out += $from_erel.expr_out + 'and\n'
$type_out = $from_erel.type_out
}
)* ;


erel[SymbolsTable ts, String type_in]  returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}: from_esum=esum[ts, type_in]
{
$stack_out = $from_esum.stack_out
$expr_out = $from_esum.expr_out
$type_out = $from_esum.type_out
}
( RELOP from_esum=esum[ts, $type_out]
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


esum[SymbolsTable ts, String type_in]  returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}: from_term=term[ts, type_in]
{
$stack_out = $from_term.stack_out
$expr_out = $from_term.expr_out
$type_out = $from_term.type_out
}
( ADDOP from_another_term=term[ts, $type_out]
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


term[SymbolsTable ts, String type_in]  returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}: from_factor=factor[ts, type_in]
{
$stack_out = $from_factor.stack_out
$expr_out = $from_factor.expr_out
$type_out = $from_factor.type_out
}
( MULOP from_another_factor=factor[ts, $type_out]
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


factor[SymbolsTable ts, String type_in] returns [Int stack_out, String expr_out, String type_out]
@init
{
$stack_out = 0
$expr_out = ''
$type_out = ''
}
    : from_base=base[ts, type_in]
{
$stack_out = $from_base.stack_out
$expr_out = $from_base.expr_out
$type_out = $from_base.type_out
}
    | NOT factor[ts, type_in]
    |LPAREN ADDOP from_factor=factor[ts, type_in]
{
$stack_out = $from_factor.stack_out
$expr_out = $from_factor.expr_out + 'neg\n' if $ADDOP.text == '-' else ''
$type_out = $from_factor.type_out
}
    RPAREN ;


base[SymbolsTable ts, String type_in] returns [Int stack_out, String expr_out, String type_out]
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
    | STRING
{
$stack_out = 1
$expr_out = 'ldstr ' + $STRING.text + '\n'
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
    | LPAREN from_expr=expr[ts]
{
$stack_out = $from_expr.stack_out
$expr_out = $from_expr.expr_out
$type_out = $from_expr.type_out
}
    RPAREN
    | IDENTIFIER
{
symbol = $ts.get($IDENTIFIER.text)
$expr_out = 'ldloc ' + str(symbol.index) + '\n'
$stack_out = 1
$type_out = symbol.stype

if $type_in == 'float':
    if $type_out == 'int':
        $expr_out += 'conv.r8\n'
        $type_out = 'float'
}
    | IDENTIFIER LCOR from_expr=expr[ts] RCOR
{
array = $ts.get($IDENTIFIER.text)
if array:
    $expr_out += 'ldloc ' + str(array.index) + '\n' + $from_expr.expr_out
    $stack_out += $from_expr.stack_out + 1
}
    (LCOR from_another_expr=expr[ts] RCOR
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
STRING :   '"' ( ESCAPED_QUOTE | ~('\n'|'\r') )*? '"';
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

