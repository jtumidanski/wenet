# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .filter_messageVisitor import filter_messageVisitor
else:
    from filter_messageVisitor import filter_messageVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\13")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\3\3\3\5\3\23\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\7\4 \n\4\f\4\16\4#\13\4\3\5\3\5\5\5\'")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\2\3\6\b\2\4\6")
        buf.write("\b\n\f\2\2.\2\16\3\2\2\2\4\22\3\2\2\2\6\24\3\2\2\2\b&")
        buf.write("\3\2\2\2\n(\3\2\2\2\f,\3\2\2\2\16\17\5\4\3\2\17\3\3\2")
        buf.write("\2\2\20\23\5\6\4\2\21\23\7\3\2\2\22\20\3\2\2\2\22\21\3")
        buf.write("\2\2\2\23\5\3\2\2\2\24\25\b\4\1\2\25\26\5\b\5\2\26\27")
        buf.write("\7\6\2\2\27\30\5\b\5\2\30!\3\2\2\2\31\32\f\5\2\2\32\33")
        buf.write("\7\4\2\2\33 \5\6\4\6\34\35\f\4\2\2\35\36\7\5\2\2\36 \5")
        buf.write("\6\4\5\37\31\3\2\2\2\37\34\3\2\2\2 #\3\2\2\2!\37\3\2\2")
        buf.write("\2!\"\3\2\2\2\"\7\3\2\2\2#!\3\2\2\2$\'\5\n\6\2%\'\5\f")
        buf.write("\7\2&$\3\2\2\2&%\3\2\2\2\'\t\3\2\2\2()\7\7\2\2)*\7\n\2")
        buf.write("\2*+\7\7\2\2+\13\3\2\2\2,-\7\b\2\2-.\7\n\2\2./\7\t\2\2")
        buf.write("/\r\3\2\2\2\6\22\37!&")
        return buf.getvalue()


class filter_messageParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'1'", u"' and '", u"' or '", u"' \\u003D '", 
                     u"'\\u0027'", u"'\\u007B'", u"'\\u007D'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"STR", u"WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_val = 3
    RULE_lit = 4
    RULE_rpl = 5

    ruleNames =  [ "prog", "stat", "expr", "val", "lit", "rpl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    STR=8
    WS=9

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return filter_messageParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.ProgContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self):
            return self.getTypedRuleContext(filter_messageParser.StatContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)



    def prog(self):

        localctx = filter_messageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            localctx = filter_messageParser.ProgramContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return filter_messageParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AllContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.StatContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitAll(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.StatContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(filter_messageParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = filter_messageParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 16
            token = self._input.LA(1)
            if token in [filter_messageParser.T__4, filter_messageParser.T__5]:
                localctx = filter_messageParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.expr(0)

            elif token in [filter_messageParser.T__0]:
                localctx = filter_messageParser.AllContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(filter_messageParser.T__0)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return filter_messageParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(filter_messageParser.ExprContext)
            else:
                return self.getTypedRuleContext(filter_messageParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(filter_messageParser.ExprContext)
            else:
                return self.getTypedRuleContext(filter_messageParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.ExprContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(filter_messageParser.ValContext)
            else:
                return self.getTypedRuleContext(filter_messageParser.ValContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = filter_messageParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = filter_messageParser.EqualityContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 19
            self.val()
            self.state = 20
            self.match(filter_messageParser.T__3)
            self.state = 21
            self.val()
            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 29
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = filter_messageParser.AndContext(self, filter_messageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 24
                        self.match(filter_messageParser.T__1)
                        self.state = 25
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = filter_messageParser.OrContext(self, filter_messageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 27
                        self.match(filter_messageParser.T__2)
                        self.state = 28
                        self.expr(3)
                        pass

             
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return filter_messageParser.RULE_val

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ValIDContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.ValContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def lit(self):
            return self.getTypedRuleContext(filter_messageParser.LitContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitValID(self)
            else:
                return visitor.visitChildren(self)


    class ValReplaceContext(ValContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.ValContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def rpl(self):
            return self.getTypedRuleContext(filter_messageParser.RplContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitValReplace(self)
            else:
                return visitor.visitChildren(self)



    def val(self):

        localctx = filter_messageParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_val)
        try:
            self.state = 36
            token = self._input.LA(1)
            if token in [filter_messageParser.T__4]:
                localctx = filter_messageParser.ValIDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.lit()

            elif token in [filter_messageParser.T__5]:
                localctx = filter_messageParser.ValReplaceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.rpl()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return filter_messageParser.RULE_lit

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LiteralContext(LitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.LitContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(filter_messageParser.STR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)



    def lit(self):

        localctx = filter_messageParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lit)
        try:
            localctx = filter_messageParser.LiteralContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(filter_messageParser.T__4)
            self.state = 39
            self.match(filter_messageParser.STR)
            self.state = 40
            self.match(filter_messageParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RplContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return filter_messageParser.RULE_rpl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReplaceContext(RplContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a filter_messageParser.RplContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(filter_messageParser.STR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, filter_messageVisitor ):
                return visitor.visitReplace(self)
            else:
                return visitor.visitChildren(self)



    def rpl(self):

        localctx = filter_messageParser.RplContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rpl)
        try:
            localctx = filter_messageParser.ReplaceContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(filter_messageParser.T__5)
            self.state = 43
            self.match(filter_messageParser.STR)
            self.state = 44
            self.match(filter_messageParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         



