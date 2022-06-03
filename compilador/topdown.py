# topdown.py
from model import *
from render import DotRender
import sly


class Lexer(sly.Lexer):
    tokens = {
        IDENT, NUMBER,
    }
    literals = '+-*/()='

    # ignorec
    ignore = ' \t'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # tokens
    IDENT = r'[a-zA-Z_]\w*'

    @_(r'\d+(\.\d*)?([eE][-+]?\d+)?')
    def NUMBER(self, t):
        if '.' in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t

    def error(self, t):
        print(f"linea {self.lineno}, error léxico: caracter '{t.value[0]}' no es permitido")
        self.index += 1


class RecursiveDescentParser:
    '''
    '''

    def statement(self):
        '''
        statement ::= assignment | expression
        '''
        while self.assignment() or self.expression():
            Asgmnt = self.assignment()
            Expr = self.expression()
            return Asgmnt, Expr
        else:
            raise SyntaxError("Se espera una asignación o una expresión")

    def assignment(self):
        # assignment ::= IDENT '=' expression #
        if self._accept('IDENT'):
            name = self.tok.value
            self._expect('=')
            expr = self.expression()
            return Assignment(Ident(name), expr)
        else:
            raise SyntaxError("Esperando un IDENT")

    def expression(self):
        '''
        expression ::= term (('+'|'-') term)*
        '''
        expr = self.term()
        while self._accept('+') or self._accept('-'):
            oper = self.tok.value
            right = self.term()
            expr = Binop(oper, expr, right)
        return expr

    def term(self):
        '''
        term ::= factor (('*'|'/'|'%') factor)*
        '''
        term = self.factor()
        while self._accept('*') or self._accept('/') or self._accept('%'):
            oper = self.tok.value
            right = self.factor()
            term = Binop(oper, term, right)
        return term

    def factor(self):
        '''
        factor ::= IDENT | NUMBER | '(' expression ')'
        '''
        if self._accept('IDENT'):
            return Ident(self.tok.value)
        elif self._accept('NUMBER'):
            return Number(self.tok.value)
        elif self._accept('('):
            expr = self.expression()
            self._expect(')')
            return expr
        else:
            raise SyntaxError('Se espera un IDENT, NUMBER o (')

    # ----------------------------------------
    # Funciones de Utilidad - No modificar
    #
    def _advance(self):
        'Avanza el lexer en un simbol'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Consume el siguiente token si coincide con un tipo esperado'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume y descarta el siguiente token o raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError(f"Esperaba {toktype}")

    def start(self):
        'Punto de entrada al objeto'
        self._advance()  # carga primer token leido
        return self.assignment()

    def parse(self, tokens):
        'Punto de entrada al parser'
        self.tok = None  # ultimo simbol consumido
        self.nexttok = None  # siguiente simbol tokenized
        self.tokens = tokens
        return self.start()


def sintactico(text):
    lexer = Lexer()
    parser = RecursiveDescentParser()
    ast = parser.parse(lexer.tokenize(text))
    dot = DotRender()
    dot.visit(ast)
    print("\n", ast)
    print(dot)
