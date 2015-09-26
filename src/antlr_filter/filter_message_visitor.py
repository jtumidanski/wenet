from antlr4 import *
import json
from antlr_filter import filter_messageVisitor

class filter_message_visitor(filter_messageVisitor.filter_messageVisitor):
	def __init__(self, message):
		self.json_message = json.loads(message)

	# Visit a parse tree produced by filter_messageParser#Program.
	def visitProgram(self, ctx):
		return self.visit(ctx.stat())

	# Visit a parse tree produced by filter_messageParser#Expression.
	def visitExpression(self, ctx):
		return self.visit(ctx.expr())

	# Visit a parse tree produced by filter_messageParser#All.
	def visitAll(self, ctx):
		return True

	# Visit a parse tree produced by filter_messageParser#Or.
	def visitOr(self, ctx):
		left = bool(self.visit(ctx.val(0)))
		right = bool(self.visit(ctx.val(1)))

		return (left or right)

	# Visit a parse tree produced by filter_messageParser#And.
	def visitAnd(self, ctx):
		left = bool(self.visit(ctx.val(0)))
		right = bool(self.visit(ctx.val(1)))

		return (left and right)

	# Visit a parse tree produced by filter_messageParser#Equality.
	def visitEquality(self, ctx):
		left = self.visit(ctx.val(0))
		right = self.visit(ctx.val(1))
		return (left == right)

	# Visit a parse tree produced by filter_messageParser#ValID.
	def visitValID(self, ctx):
		return self.visit(ctx.lit())

	# Visit a parse tree produced by filter_messageParser#ValReplace.
	def visitValReplace(self, ctx):
		return self.visit(ctx.rpl())

	# Visit a parse tree produced by filter_messageParser#Literal.
	def visitLiteral(self, ctx):
		return ctx.STR().getText()

	# Visit a parse tree produced by filter_messageParser#Replace.
	def visitReplace(self, ctx):
		key = ctx.STR().getText()

		if key in self.json_message:
			return self.json_message[key]
		else:
			return ""







