from cast import *

# ---------------------------------------------------------------------
# Tabla de Simbolos
# ---------------------------------------------------------------------
class Symtab:
	'''
	Una tabla de símbolos.  Este es un objeto simple que sólo
	mantiene una hashtable (dict) de nombres de simbolos y los
	nodos de declaracion o definición de funciones a los que se
	refieren.
	Hay una tabla de simbolos separada para cada elemento de
	código que tiene su propio alcance (por ejemplo cada función,
	clase, tendra su propia tabla de simbolos). Como resultado,
	las tablas de simbolos se pueden anidar si los elementos de
	código estan anidados y las búsquedas de las tablas de
	simbolos se repetirán hacia arriba a través de los padres
	para representar las reglas de alcance léxico.
	'''
	
	class SymbolDefinedError(Exception):
		'''
		Se genera una excepción cuando el código intenta agregar
		un simbol a una tabla donde el simbol ya se ha definido.
		Tenga en cuenta que 'definido' se usa aquí en el sentido
		del lenguaje C, es decir, 'se ha asignado espacio para el
		simbol', en lugar de una declaración.
		'''
		pass
		
	class SymbolConflitError(Exception):
		'''
		Se genera una excepción cuando el código intenta agregar
		un símbol a la tabla donde el simbol ya existe y su tipo
		difiere del existente anteriormente
		'''
		pass
		
	def __init__(self, parent=None):
		'''
		Crea una tabla de símbolos vacia con la tabla de
		simbolos padre dada.
		'''
		self.entries = {}
		self.parent = parent
		if self.parent:
			self.parent.children.append(self)
		self.children = []
		
	def add(self, name, value):
		'''
		Agrega un simbol con el valor dado a la tabla de simbolos.
		El valor suele ser un nodo AST que representa la declaración
		o definición de una función, variable (por ejemplo, Declaración
		o FuncDeclaration)
		'''
		#if name in self.entries:
			#raise Symtab.SymbolDefinedError()
		self.entries[name] = value
		
	def get(self, name):
		'''
		Recupera el símbol con el nombre dado de la tabla de
		simbol, recurriendo hacia arriba a traves de las tablas
		de simbol principales si no se encuentra en la actual.
		'''
		if name in self.entries:
			return self.entries[name]
		elif self.parent:
			return self.parent.get(name)
		return None
		
class Checker(Visitor):
	'''
	Visitante que crea y adjunta tablas de símbolos al AST.
	'''

	def push_symtab(self, node):
		'''
		Inserta una nueva tabla de símbolos en la pila de 
		tablas de símbolos del visitante y adjunta esta tabla 
		de símbolos al nodo dado.  Esto se usa cada vez que 
		se encuentra un nuevo ámbito léxico, por lo que el 
		nodo suele ser un objeto Statements.
		'''
		self.curr_symtab = Symtab(self.curr_symtab)
		node.symtab = self.curr_symtab

	def pop_symtab(self):
		'''
		Saca una tabla de símbolos de la pila de tablas de 
		símbolos del visitante.  Esto se usa cada vez que 
		se sale de un nuevo ámbito léxico.
		'''
		self.curr_symtab = self.curr_symtab.parent

	def _add_symbol(self, node):
		'''
		Intenta agregar un símbolo para el nodo dado a 
		la tabla de símbolos actual, capturando cualquier 
		excepción que ocurra e imprimiendo errores si es 
		necesario.
		'''
		try:
			self.curr_symtab.add(node.name, node)
		except Symtab.SymbolDefinedError:
			self.error(f"Simbol '{node.name}' esta definido.")
		except Symtab.SymbolConflictError:
			self.error("Simbol '{node.name}' tiene multiples declaraciones diferentes.")

	@classmethod
	def check(cls, node):
		check = cls()
		node.accept(check)
		return check
 	
	def visit(self, node: ClassDeclaration):
		pass
		
	def visit(self, node: FuncDeclaration):
		for name in node.params:
			self._add_symbol(Variable(name))



class Checker(Visitor):
	'''
	Visitante que crea y adjunta tablas de símbolos al AST.
	'''
	def __init__(self):
		self.curr_symtab = Symtab()

	def push_symtab(self, node):
		'''
		Inserta una nueva tabla de símbolos en la pila de 
		tablas de símbolos del visitante y adjunta esta tabla 
		de símbolos al nodo dado.  Esto se usa cada vez que 
		se encuentra un nuevo ámbito léxico, por lo que el 
		nodo suele ser un objeto Statements.
		'''
		self.curr_symtab = Symtab(self.curr_symtab)
		node.symtab = self.curr_symtab

	def pop_symtab(self):
		'''
		Saca una tabla de símbolos de la pila de tablas de 
		símbolos del visitante.  Esto se usa cada vez que 
		se sale de un nuevo ámbito léxico.
		'''
		self.curr_symtab = self.curr_symtab.parent

	def _add_symbol(self, node):
		'''
		Intenta agregar un símbolo para el nodo dado a 
		la tabla de símbolos actual, capturando cualquier 
		excepción que ocurra e imprimiendo errores si es 
		necesario.
		'''
		try:
			self.curr_symtab.add(node.name, node)
		except Symtab.SymbolDefinedError:
			self.error(f"Simbol '{node.name}' esta definido.")
		except Symtab.SymbolConflictError:
			self.error("Simbol '{node.name}' tiene multiples declaraciones diferentes.")

	def error(self,text):
		'''
		La define como bien le convenga
		'''

	@classmethod
	def check(cls, model):
		check = cls()
		model.accept(check)
		return check
		
	def visit(self, node: ClassDeclaration):
		'''
		1. Agregar el nombre de clase a symtab actual
		2. Veriicar que exista 'node.superclass'. si está definido.
		3. crear una nueva symtab para la clase (contexto)
		4. Visitar todo los métodos definidos
		'''
		self._add_symbol(node)
		if node.superclass:
			result = self.curr_symtab.get(node.superclass)
			if result is None:
				self.error(f"Simbol '{node.superclass} no está definido.")
		self.push_symtab(node)
		for meth in node.methods:
			self.visit(meth)

	def visit(self, node: FuncDeclaration):
		'''
		1. Agregar el nombre de clase a symtab actual
		2. Veriicar que exista 'node.superclass'. si está definido.
		3. crear una nueva symtab para la clase (contexto)
		4. Visitar todo los 'node.stmts' definidos.
		'''
		self._add_symbol(node)
		if node.Declaration:
			result = self.curr_symtab.get(node.Declaration)
			if result is None:
				self.error(f"Simbol '{node.Declaration} no está definido")
		self.push_symtab(node)
		
	def visit(self, node: VarDeclaration):
		self._add_symbol(node)
		if node.Declaration:
			result = self.curr_symtab.get(node.Declaration)
			if result is None:
				self.error(f"Simbol '{node.Declaration} ya está definido")
		self.push_symtab(node)
		'''
		1. Agregar 'node.name' al symtab actual
		4. Visitar 'node.expr', si existe
		'''
		
	def visit(self, node: Statements):
		self._add_symbol(node)
		if node.Statements:
			result = self.curr_symtab.get(node.Statements)
			if result is None:
				self.error(f"Error de Sintaxis en {node.Statements}")
		self.push_symtab(node)
		'''
		1. Visitar todas las instruccioes contenidas en 'node.stmts'
		'''
		
	def visit(self, node: Print):
		self._add_symbol(node)
		if node.Expression:
			result = self.curr_symtab.get(node.Expression)
			if result is None:
				self.error(f"Error de sintaxis en {node.Expression}")
		self.push_symtab(node)
		'''
		1. Visitar 'node.expr'
		'''

	def visit(self, node: WhileStmt):
		self._add_symbol(node)
		self._add_symbol(node)
		if node.Statement:
			result = self.curr_symtab.get(node.Statement)
			if result is None:
				self.error(f"Se requiere una condición. Error : {node.Statement}")
		elif (node.Statements):
			result = self.curr_symtab.get(node.Statements)
			if result is None:
				self.error(f"No hay sentencias para romper el ciclo en {node.Statements}")
		self.push_symtab(node)
		self.push_symtab(node)
		'''
		1. Visitar node.cond
		2. Visitar node.body
		'''
		
	def visit(self, node: IfStmt):
		self._add_symbol(node)
		if node.Statement:
			result = self.curr_symtab.get(node.Statement)
			if result is None:
				self.error(f"Se requiere una condición. Error : {node.Statement}")
		self.push_symtab(node)
		'''
		1. visitar node.cond
		'''
		
	def visit(self, node: Return):
		pass
		
	def visit(self, node: Literal):
		'''
		No se hace nada
		'''
		pass
		
	def visit(self, node: Binary):
		self._add_symbol(node)
		if node.Expression:
			result  = self.curr_symtab.get(node.Expression)
			if result is None:
				self.error(f"Expresión no válida : {node.Expression}")
		self.push_symtab(node)
		'''
		1. Visitar node.left
		2. visitar node.right
		'''
		
	def visit(self, node: Logical):
		pass
		
	def visit(self, node: Unary):
		self._add_symbol(node)
		if node.Expression:
			result = self.curr_symtab.get(node.Expression)
			if result is None:
				self.error(f"Expresión no válida : {node.Expression}")
		self.push_symtab(node)
		'''
		Visitar node.expr
		'''

		
	def visit(self, node: Assign):
		'''
		1. Visitar node.left (Ojo, puede ser str)
		2. visitar node.right
		'''
		pass
		
	def visit(self, node: Variable):
		self._add_symbol(node)
		if node.name:
			result = self.curr_symtab.get(node.name)
			if result is None:
				self.error(f"{node.name} no ha sido declarado")
		self.push_symtab(node)
		'''
		1. Buscar node.name
		'''
		
	def visit(self, node: Set):
		pass
		
	def visit(self, node: Get):
		pass
		
	def visit(self, node: This):
		pass

	def visit(self, node: Super):
		pass  
		
