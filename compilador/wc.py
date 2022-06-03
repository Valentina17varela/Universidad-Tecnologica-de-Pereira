from typing_extensions import get_type_hints
import sly
from model import *

palabra = 0
linea = 0

class Lexer(sly.Lexer):

    caracter, palabra, linea = 0, 0, 0

    tokens = {
        IDENT, NUMBER,
    }

    literals = '+-*/()='

    ignore = ' \t'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self,t):
        print("caracter ilegal")
        self.index += 1

    @_(r'\d+(\.\d*)?([eE][-+]?\d+)?')
    def NUMBER(self,t):
        if '.' in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t 


    IDENT = r'[a-zA-Z_]\w*'

    


class RecursiveDescendentParser:

    def assignment(self):
        if self._accept('IDENT'):
            name = self.tok.value
            self._expect('=')
            expr = self.expression()
            return Assignment(name,expr)
        else:
            return SyntaxError('Esperando un IDENT')

    def expression(self):
        expr = self.term()
        while self._accept('+') and self._accept('-'):
            op = self.tok.value()
            right = self.term()
            expr = Binop(op,expr,right)
        return expr
    
    def term(self):
        term = self.factor()
        while self._accept('*') and self._accept('/'):
            oper = self.tok.value
            right = self.factor()
            term = Binop(oper,term,right)

    def factor(self):
        if self._accept('IDENT'):
            return self.tok.value
        elif self._accept('NUMBER'):
            return Number(self.tok.value)
        elif self._accept('('):
            expr = self.expression()
            self._expect(')')
            return expr
        else:
            raise SyntaxError('Se espera un IDENT, NUMBER O ()')

    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens,)

    def _accept(self,toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self,toktype):
        if not self._accept(toktype):
            raise SyntaxError(f"Esperaba {toktype}")

    def start(self):
        self._advance()
        return self.assignment()

    def parse(self,tokens):
        self.tok = None
        self.nexttok = None
        self.tokens = tokens
        return self.start()



 