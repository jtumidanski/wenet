# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\13")
        buf.write("8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\6\t.\n\t\r\t\16\t/\3\n\6\n\63\n\n\r\n\16")
        buf.write("\n\64\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\3\2\4\n\2\"#%(\60\60\62;B\\^^``c|\4\2\13\f\17")
        buf.write("\179\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\3\25\3\2\2\2\5\27\3\2\2\2\7\35\3\2\2\2\t\"\3")
        buf.write("\2\2\2\13&\3\2\2\2\r(\3\2\2\2\17*\3\2\2\2\21-\3\2\2\2")
        buf.write("\23\62\3\2\2\2\25\26\7\63\2\2\26\4\3\2\2\2\27\30\7\"\2")
        buf.write("\2\30\31\7c\2\2\31\32\7p\2\2\32\33\7f\2\2\33\34\7\"\2")
        buf.write("\2\34\6\3\2\2\2\35\36\7\"\2\2\36\37\7q\2\2\37 \7t\2\2")
        buf.write(" !\7\"\2\2!\b\3\2\2\2\"#\7\"\2\2#$\7?\2\2$%\7\"\2\2%\n")
        buf.write("\3\2\2\2&\'\7)\2\2\'\f\3\2\2\2()\7}\2\2)\16\3\2\2\2*+")
        buf.write("\7\177\2\2+\20\3\2\2\2,.\t\2\2\2-,\3\2\2\2./\3\2\2\2/")
        buf.write("-\3\2\2\2/\60\3\2\2\2\60\22\3\2\2\2\61\63\t\3\2\2\62\61")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("\66\3\2\2\2\66\67\b\n\2\2\67\24\3\2\2\2\5\2/\64\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class filter_messageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    STR = 8
    WS = 9

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            "'1'", "' and '", "' or '", "' \\u003D '", "'\\u0027'", "'\\u007B'", 
            "'\\u007D'" ]

    symbolicNames = [ u"<INVALID>",
            "STR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "STR", "WS" ]

    grammarFileName = "filter_message.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


