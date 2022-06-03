from cast import *
from clex import Lexer
import logging
import sly

class Parser(sly.Parser):
	debugfile = "minic.txt"
	expected_shift_reduce = 1
	tokens = Lexer.tokens
	
	precedence = (
		('right', '='),
		('left', OR),
		('left', AND),
		('left', EQ, NE),
		('left', LT, LE, GT, GE),
		('left', '+', '-'),
		('left', '*', '/'),
		('right', UNARY),
	)
	
	@_("declarations")
	def program(self, p):
		pass

	@_("{ declaration }")
	def declarations(self, p):
		pass

	@_("var_declaration",
	   "func_declaration",
	   "class_declaration",)
	def declaration(self, p):
		pass
    
	@_("VAR IDENTIFIER [ '=' expression ] ';'")
	def var_declaration(self, p):
		pass

	@_("FUN function")
	def func_declaration(self, p):
		pass

	@_("IDENTIFIER '(' parameters ')' statement_block")
	def function(self, p):
		pass
        
	@_("IDENTIFIER '(' ')' statement_block")
	def function(self, p):
		pass
        
	@_("IDENTIFIER { ',' IDENTIFIER }")
	def parameters(self, p):
		return [p.IDENTIER0]+p.IDENTIFIER1
        
	@_("CLASS IDENTIFIER [ LT IDENTIFIER ] '{' { function } '}'")
	def class_declaration(self, p):
		pass
    
	@_("statement")
	def declaration(self, p):
		pass

	@_("statement_block",
	   "expression_statement",
	   "print_statement",
	   "if_statement",
	   "while_statement",
	   "for_statement",
	   "return_statement")
	def statement(self, p):
		pass
    
	@_("'{' declarations '}'")
	def statement_block(self, p):
		pass

	@_("expression ';'")
	def expression_statement(self, p):
		pass
    
	@_("PRINT expression ';'")
	def print_statement(self, p):
		pass

	@_("IF '(' expression ')' statement [ ELSE statement ]")
	def if_statement(self, p):
		pass
        
	@_("WHILE '(' expression ')' statement")
	def while_statement(self, p):
		return WhileStmt(p.expression, p.statement)
        
	@_("FOR '(' for_initializer [ expression ] ';' [ expression ] ')' statement")
	def for_statement(self, p):
		body = p.statement
		if p.expression1:
			if not isinstance(body, Statements):
				body = Statements([body])
			body.stmts.append(ExprStmt(p.expression1))
		body = WhileStmt(p.expression0 or Literal(True), body)
		body = Statements([p.for_initializer, body])
		return body
        
	@_("FOR '(' ';' [ expression ] ';' [ expression ] ')' statement")
	def for_statement(self, p):
		body = p.statement
		if p.expression1:
			if not isinstance(body, Statements):
				body = Statements([body])
			body.stmts.append(ExprStmt(p.expression1))
		body = WhileStmt(p.expression0 or Literal(True), body)
		return body
        
	@_("var_declaration",
	   "expression_statement")
	def for_initializer(self, p):
		pass
        
	@_("RETURN expression ';'")
	def return_statement(self, p):
		pass
        
	@_("expression '=' expression")
	def expression(self, p):
		if isinstance(p.expression0, Variable):
			return Assign(p.expression0, p.expression1)
		elif isinstance(p.expression0, Get):
			return Set(p.expression0.object, p.expression0.name, p.expression1)
		else:
			raise SyntaxError(f"Linea {p.lineno}: no se puede asignar {p.expression0}")


	@_("expression OR expression",
	   "expression AND expression")
	def expression(self, p):
		return Logical(p[1], p.expression0, p.expression1)

	@_("expression '+' expression",
	   "expression '-' expression",
	   "expression '*' expression",
	   "expression '/' expression",
	   "expression LT  expression",
	   "expression LE  expression",
	   "expression GT  expression",
	   "expression GE  expression",
	   "expression EQ  expression",
	   "expression NE  expression")
	def expression(self, p):
		return Binary(p[1], p.expression0, p.expression1)

	@_("factor")
	def expression(self, p):
		pass

	@_("'(' expression ')'")
	def factor(self, p):
		pass

	@_("'-' factor %prec UNARY",
	   "NOT factor %prec UNARY")
	def factor(self, p):
		return Unary(p[0],p.factor)

	@_("NUMBER", "STRING")
	def factor(self, p):
		pass

	@_("TRUE", "FALSE")
	def factor(self, p):
		return Literal(p[0]=='true') #True/False (valores de python)

	@_("NIL")
	def factor(self, p):
		return Literal(None)
        
	@_("IDENTIFIER")
	def factor(self, p):
		return Variable(p.IDENTIFIER)
        
	@_("THIS")
	def factor(self, p):
		return This()
        
	@_("SUPER '.' IDENTIFIER")
	def factor(self, p):
		return Super(p.IDENTIFIER)

	@_("factor '.' IDENTIFIER")
	def factor(self, p):
		return Get(p.factor, p.IDENTIFIER)

	@_("factor '(' arguments ')'")
	def factor(self, p):
		return Call(p.factor, p.arguments)

	@_("factor '(' ')'")
	def factor(self, p):
		return Call(p.factor)

	@_("expression { ',' expression }")
	def arguments(self, p):
		return [p.expression0] + p.expression1

	def error(self, p):
		lineno = p.lineno if p else "EOF"
		value = repr(p.value) if p else "EOF"
		print(f"{lineno}: Syntax error at {value}")

if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 2:
		print('usage: cparse file')
		exit(1)
	
	l = Lexer()
	p = Parser()
	