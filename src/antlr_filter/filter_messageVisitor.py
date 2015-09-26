# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by filter_messageParser.

class filter_messageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by filter_messageParser#Program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#Expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#All.
    def visitAll(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#Or.
    def visitOr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#And.
    def visitAnd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#Equality.
    def visitEquality(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#ValID.
    def visitValID(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#ValReplace.
    def visitValReplace(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#Literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_messageParser#Replace.
    def visitReplace(self, ctx):
        return self.visitChildren(ctx)


