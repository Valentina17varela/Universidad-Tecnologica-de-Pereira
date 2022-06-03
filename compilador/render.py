# render.py
from graphviz import Digraph
from model import *

class DotRender(Visitor):

    _node_defaults = {
        'shape' : 'box',
        'color' : 'lightblue2',
        'style' : 'filled',
    }
    _edge_defaults = {
        'arrowhead' : 'none',
    }

    def __init__(self):
        self.dot = Digraph('AST')
        self.dot.attr('node', **self._node_defaults) 
        self.dot.attr('edge', **self._edge_defaults)
        self.seq = 0
    
    def __repr__(self):
        return self.dot.source

    def __str__(self):
        return self.dot.source

    def name(self):
        self.seq += 1
        return 'n%02d' % self.seq

    def visit(self, node : Assignment):
        name = self.name()
        self.dot.node(name, label='=')
        self.dot.edge(name, self.visit(node.ident))
        self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : Binop):
        name = self.name()
        self.dot.node(name, label=node.oper)
        self.dot.edge(name, self.visit(node.left))
        self.dot.edge(name, self.visit(node.right))
        return name

    def visit(self, node : Number):
        name = self.name()
        self.dot.node(name, label=str(node.value))
        return name

    def visit(self, node : Ident):
        name = self.name()
        self.dot.node(name, label=str(node.name))
        return name
    
    @classmethod
    def render(cls,model):
        dot = cls()
        model.accept(dot)
        return dot.dot