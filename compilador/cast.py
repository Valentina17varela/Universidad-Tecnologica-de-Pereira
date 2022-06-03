from dataclasses import dataclass, field
from multimethod import multimeta
from typing import Any, List
from model import *

# ----------------------------------------
# clases abstractas
#


class Visitor(metaclass=multimeta):
  pass

class Evaluate(Visitor):

  def visit(self, node: Binop):
    if node.op == "+":
      return self.visit(node.left) + self.visit(node.right)
    elif node.op == "-":
      return self.visit(node.left) - self.visit(node.right)
    elif node.op == "*":
      return self.visit(node.left) * self.visit(node.rigth)
    elif node.op == "/":
      return self.visit(node.left) / self.visit(node.right)


  def visit(self, node: Number):
    return node.value



@dataclass
class Node:
	pass

@dataclass
class Statement(Node):
	pass

@dataclass
class Expression(Node):
	pass

@dataclass
class Declaration(Statement):
	pass

# ----------------------------------------
# Declaration son Statement especiales que
# declara la existencia de algo
#
@dataclass
class ClassDeclaration(Declaration):
	name: str
	superclass: Expression
	methods: List[Statement]=field(default_factory=list)

@dataclass
class FuncDeclaration(Declaration):
	name: str
	params: List[Expression]=field(default_factory=list)
	body: List[Statement]=field(default_factory=list)

@dataclass
class VarDeclaration(Declaration):
	name: str
	expr: Expression

# ----------------------------------------
# Statements representan acciones sin 
# valores asociados
#
@dataclass
class Print(Statement):
	expr: Expression

@dataclass
class ExprStmt(Statement):
	expr: Expression

@dataclass
class IfStmt(Statement):
	cond: Expression
	const: list
	alt: list

@dataclass
class WhileStmt(Statement):
	cond: Expression
	body: List[Statement]=field(default_factory=list)

@dataclass
class Return(Statement):
	expr: Expression

@dataclass
class Statements(Statement):
	stmts: List[Statement]=field(default_factory=list)

# ----------------------------------------
# Expression representan valores
#
@dataclass
class Literal(Expression):
	value: Any

@dataclass
class Binary(Expression):
	op   : str
	left : Expression
	right: Expression

@dataclass
class Logical(Expression):
	op   : str
	left : Expression
	right: Expression

@dataclass
class Unary(Expression):
	op: str
	expr: Expression

@dataclass
class Grouping(Expression):
	pass

@dataclass
class Variable(Expression):
	name : str

@dataclass
class Assign(Expression):
	left : Expression
	right: Expression

@dataclass
class Call(Expression):
	func: str
	args: List[Expression] = field(default_factory=list)

@dataclass
class Get(Expression):
	object: str
	name: str

@dataclass
class Set(Expression):
	object: str
	name: str
	value: Expression

@dataclass
class This(Expression):
	pass#This()

@dataclass
class Super(Expression):
	name: str
