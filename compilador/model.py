from dataclasses import dataclass, field
from email.policy import default
from turtle import st
from typing import Any, List
from multimethod import multimeta
import types

# ----------------------------------------
# Clases abstractas
#

class Visitor(metaclass=multimeta):
    pass

@dataclass
class Node:
    pass

@dataclass
class Statement(Node):
    pass

@dataclass
class Expression(Statement):
    pass

@dataclass
class Term(Node):
	oper : str
	factor: Expression

@dataclass
class Factor(Node):
	Ident : str
	Number : float
	Expr : Expression

@dataclass
class Declaration(Statement):
    pass


# ----------------------------------------
# Declaration son Statement especiales que
# declara la existencia de algo
#
'''@dataclass
class ClassDeclaration(Declaration):
	name : str
	superclass : Expression
	methods    : List[Statement]=field(default_factory=list)
'''

@dataclass
class FuncDeclaration(Declaration):
	pass

@dataclass
class VarDeclaration(Declaration):
	pass

# ----------------------------------------
# Statements representan acciones sin
# valores asociados
#
@dataclass
class Print(Statement):
	pass

class ExprStmt(Statement):
	pass

class IfStmt(Statement):
	pass

class WhileStmt(Statement):
	cod : Expression
	boy : List[Statement]=field(default_factory=list)

class Return(Statement):
	exr : Expression

class Statements(Statement):
	stms : List[Statement]=field(default_factory=list)

# ----------------------------------------
# Expression representan valores
#
@dataclass
class Literal(Expression):
	vale : Any

@dataclass
class Binop(Expression):
	oper : str
	left : Expression
	right : Expression

@dataclass
class Logical(Expression):
	op   : str
	let : Expression
	right: Expression

@dataclass
class Unary(Expression):
	op : str
	expr : Expression

@dataclass
class Grouping(Expression):
	pass

@dataclass
class Variable(Expression):
	Variable : str

@dataclass
class Call(Expression):
	func : str
	args : List[Expression] = field(default_factory=list)

@dataclass
class Get(Expression):
	object : str
	name   : str

@dataclass
class Set(Expression):
	object : str
	name   : str
	value  : Expression

@dataclass
class This(Expression):
	pass

@dataclass
class Super(Expression):
	name : str

@dataclass
class Assignment(Statement):
	ident: Expression
	expr : Expression

@dataclass
class Number(Expression):
	value : float

@dataclass
class Ident(Expression):
	name : str


