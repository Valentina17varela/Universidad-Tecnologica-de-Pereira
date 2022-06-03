import sly

class Lexer(sly.Lexer):
	tokens = {
		# keywords
		CLASS, FUN, VAR, FOR, IF, ELSE, 
		PRINT, RETURN, WHILE, TRUE, FALSE, 
		NIL, THIS, SUPER,
		
		# operators
		OR, AND, NOT,
		GE, GT, LT, LE, EQ, NE,
		
		# others
		NUMBER, STRING, IDENTIFIER,
		
	}
	literals = '+-*/=.(){};,'
	
	# ignore white-space
	ignore = ' \t'
	
	@_(r'//.*\n')
	def ignore_comments(self, t):
		self.lineno += 1
	
	@_(r'\n+')
	def ignore_newline(self, t):
		self.lineno += t.value.count('\n')

	# operators
	EQ = r'=='
	NE = r'!='
	LE = r'<='
	LT = r'<'
	GE = r'>='
	GT = r'>'
	AND = r'&&'
	OR  = r'\|\|'
	NOT = r'!'

	# tokens definitions	
	@_(r'\d*\.\d+|\d+\.?')
	def NUMBER(self, t):
		try:
			t.value = int(t.value)
		except ValueError:
			t.value = float(t.value)
		return t

	@_(r'"(.|\n)*?"')
	def STRING(self, t):
		self.lineno += t.value.count('\n')
		t.value = t.value[1:-1]
		return t

	IDENTIFIER = '[a-zA-Z_]\w*'
	IDENTIFIER['class'] = CLASS
	IDENTIFIER['fun'] = FUN
	IDENTIFIER['var'] = VAR
	IDENTIFIER['for'] = FOR
	IDENTIFIER['if'] = IF
	IDENTIFIER['else'] = ELSE
	IDENTIFIER['print'] = PRINT
	IDENTIFIER['return'] = RETURN
	IDENTIFIER['while'] = WHILE
	IDENTIFIER['true'] = TRUE
	IDENTIFIER['false'] = FALSE
	IDENTIFIER['nil'] = NIL
	IDENTIFIER['this'] = THIS
	IDENTIFIER['super'] = SUPER
	
	def error(self, t):
		print(f"Linea {self.lineno}: Caracter ilegal '{t.value[0]}'")
		self.index += 1