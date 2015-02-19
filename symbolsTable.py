class Scope(object):
    FUNCTION_PARAMETER = 0
    GLOBAL = 1
    BLOCK_LOCAL = 2
    LOOP = 3

class Stype(object):
    CLASS = 0
    METHOD = 1
    VAR = 2

class Symbol(object):
    def __init__(self, name, stype, isFunction, scope, line, index=None):
        self.name = name
        self.stype = stype
        self.isFunction = isFunction
        self.scope = scope
        self.index = index
        self.line = line

    def __repr__(self):
        return '( index:' + str(self.index) + ', name:'  + self.name + ', scope:' + str(self.scope) + ', type:' + str(self.stype) + ' )'

    def __str__(self):
        return self.__repr__()


class SymbolsTable(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}

    def add(self, name, stype, isFunction, scope, line):
        s = Symbol(name, stype, isFunction, scope, line)
        s.index = self.get_index()
        self.symbols[name] = s

    def get_index(self):
        return len(self.symbols) + self.parent.get_index() if self.parent else 0

    def __repr__(self):
        return str(self.symbols)

    def get(self, name, recursive=True):
        obj = self.symbols.get(name, None)

        if obj:
            return obj
        else:
            if recursive:
                if self.parent:
                    self = self.parent
                    return self.get(name)
            return None





