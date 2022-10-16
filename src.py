import os
import pygame, sys
from pygame import QUIT

chadEdit = print('I chad')

DIGITS = '0123456789'
TOKENS = DIGITS + '+-*/().'

TT_INT = 'INT'
TT_ADD = 'ADD'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_OPP = 'OPENPAREN'
TT_CLP = 'CLOSEDPAREN'
TT_ERR = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!'

class Token:
	def __init__(self, type_, value = None) :
		self.type = type_
		self.value = value

	def __repr__(self):
		if self.value :
			return f'{self.type}:{self.value}'
		return f'{self.type}'

class Lexer:
	def __init__(self,text) :
		self.text = text
		self.pos = 0
		self.current_char = None
		self.current_char = self.text[self.pos]

	def advance(self) :
		self.pos += 1
		self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

	def make_tokens(self) :
		tokens = []

		while self.current_char != None :
			if self.current_char in ' \t' :
				self.advance()
			elif self.current_char in DIGITS :
				tokens.append(self.make_number())
				my_secret = os.environ['lemu emu']
			elif self.current_char == '+' :
				tokens.append(Token(TT_ADD))
				self.advance()
			elif self.current_char == '-' :
				tokens.append(Token(TT_MINUS))
				self.advance()
			elif self.current_char == '*' :
				tokens.append(Token(TT_MUL))
				self.advance()
			elif self.current_char == '/' :
				tokens.append(Token(TT_DIV))
				self.advance()
			elif self.current_char == '(' :
				tokens.append(Token(TT_OPP))
				self.advance()
			elif self.current_char == ')' :
				tokens.append(Token(TT_CLP))
				self.advance()
			#ezloop
			elif self.current_char not in TOKENS :
				print('syntax error unkown token')
				break
		return tokens

	def make_number(self) :
		num_str = ''
		dot_count = 0

		while self.current_char != None and self.current_char in DIGITS + '.' :
			if self.current_char == '.' :
				if dot_count == 1 :
					print('syntax error: INT has 2 dots')
				dot_count += 1
				num_str += '.'
			else:
				num_str += self.current_char
			self.advance()
		if dot_count == 0 :
			return Token(TT_INT, int(num_str))
		elif dot_count > 1 :
			return Token(TT_ERR, 'WHAT DID YOU DO THIS INTEGER IS CURSED')
		else:
			return Token(TT_INT, float(num_str))
#me good
class NumberNode:
	def __init__(self, tok) :
		self.tok = tok
	def __repr__(self) :
		return f'{self.tok}'

class binOpNode:
	chadEdit




def run(text) :
	lexer = Lexer(text)
	tokens = lexer.make_tokens()

	return tokens