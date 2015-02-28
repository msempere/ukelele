# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ukeleleListener import ukeleleListener
else:
    from ukeleleListener import ukeleleListener

from symbolsTable import SymbolsTable, Scope, Stype
from utilities import error_message, error_message_without_line, already_defined_message, reserved_word_message, not_defined_message

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"/\u019b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\3\2\3\2\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3\2")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5P\n\5\f\5\16\5S\13")
        buf.write(u"\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6[\n\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\5\6c\n\6\3\6\7\6f\n\6\f\6\16\6i\13\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6x\n\6\f")
        buf.write(u"\6\16\6{\13\6\3\6\3\6\3\6\5\6\u0080\n\6\3\7\3\7\3\7\3")
        buf.write(u"\7\3\7\7\7\u0087\n\7\f\7\16\7\u008a\13\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00b4")
        buf.write(u"\n\b\3\b\3\b\3\b\3\b\3\b\5\b\u00bb\n\b\3\b\3\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00cc")
        buf.write(u"\n\b\f\b\16\b\u00cf\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write(u"\u00f1\n\b\3\b\3\b\3\b\5\b\u00f6\n\b\3\t\3\t\3\t\3\n")
        buf.write(u"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0103\n\n\3\n\3\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write(u"\16\5\16\u0114\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write(u"\3\17\3\17\5\17\u011f\n\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write(u"\20\7\20\u0127\n\20\f\20\16\20\u012a\13\20\3\21\3\21")
        buf.write(u"\3\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u0135\n\22\f")
        buf.write(u"\22\16\22\u0138\13\22\3\23\3\23\3\23\3\23\3\23\3\23\7")
        buf.write(u"\23\u0140\n\23\f\23\16\23\u0143\13\23\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\7\24\u014b\n\24\f\24\16\24\u014e\13\24")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0156\n\25\f\25\16")
        buf.write(u"\25\u0159\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0161")
        buf.write(u"\n\26\f\26\16\26\u0164\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0171\n\27\3\30\3")
        buf.write(u"\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write(u"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\7\30\u018c\n\30\f\30\16\30\u018f\13\30")
        buf.write(u"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0199\n")
        buf.write(u"\30\3\30\2\2\31\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(u" \"$&(*,.\2\4\3\2\3\5\4\2\4\6\22\23\u01b0\2\65\3\2\2")
        buf.write(u"\2\4:\3\2\2\2\6D\3\2\2\2\bQ\3\2\2\2\n\177\3\2\2\2\f\u0088")
        buf.write(u"\3\2\2\2\16\u00f5\3\2\2\2\20\u00f7\3\2\2\2\22\u00fa\3")
        buf.write(u"\2\2\2\24\u010a\3\2\2\2\26\u010c\3\2\2\2\30\u010e\3\2")
        buf.write(u"\2\2\32\u0113\3\2\2\2\34\u011b\3\2\2\2\36\u0123\3\2\2")
        buf.write(u"\2 \u012b\3\2\2\2\"\u012e\3\2\2\2$\u0139\3\2\2\2&\u0144")
        buf.write(u"\3\2\2\2(\u014f\3\2\2\2*\u015a\3\2\2\2,\u0170\3\2\2\2")
        buf.write(u".\u0198\3\2\2\2\60\61\5\4\3\2\61\62\b\2\1\2\62\64\3\2")
        buf.write(u"\2\2\63\60\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66")
        buf.write(u"\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\b\2\1\29\3\3\2\2")
        buf.write(u"\2:;\7\7\2\2;<\7\35\2\2<=\b\3\1\2=>\5\34\17\2>?\5\26")
        buf.write(u"\f\2?@\b\3\1\2@A\b\3\1\2AB\5\6\4\2BC\b\3\1\2C\5\3\2\2")
        buf.write(u"\2DE\7)\2\2EF\5\b\5\2FG\b\4\1\2GH\7*\2\2H\7\3\2\2\2I")
        buf.write(u"J\5\16\b\2JK\b\5\1\2KP\3\2\2\2LM\5\n\6\2MN\b\5\1\2NP")
        buf.write(u"\3\2\2\2OI\3\2\2\2OL\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3")
        buf.write(u"\2\2\2R\t\3\2\2\2SQ\3\2\2\2TU\5\30\r\2UZ\7\35\2\2VW\7")
        buf.write(u"#\2\2WX\5\"\22\2XY\b\6\1\2Y[\3\2\2\2ZV\3\2\2\2Z[\3\2")
        buf.write(u"\2\2[\\\3\2\2\2\\g\b\6\1\2]^\7,\2\2^b\7\35\2\2_`\7#\2")
        buf.write(u"\2`a\b\6\1\2ac\5\"\22\2b_\3\2\2\2bc\3\2\2\2cd\3\2\2\2")
        buf.write(u"df\b\6\1\2e]\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2hj")
        buf.write(u"\3\2\2\2ig\3\2\2\2jk\7$\2\2k\u0080\3\2\2\2lm\5\30\r\2")
        buf.write(u"mn\7\35\2\2no\7\'\2\2op\5\20\t\2pq\7(\2\2qy\b\6\1\2r")
        buf.write(u"s\7\'\2\2st\5\20\t\2tu\7(\2\2uv\b\6\1\2vx\3\2\2\2wr\3")
        buf.write(u"\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{y\3\2")
        buf.write(u"\2\2|}\7$\2\2}~\b\6\1\2~\u0080\3\2\2\2\177T\3\2\2\2\177")
        buf.write(u"l\3\2\2\2\u0080\13\3\2\2\2\u0081\u0082\5.\30\2\u0082")
        buf.write(u"\u0083\7+\2\2\u0083\u0084\5\6\4\2\u0084\u0085\b\7\1\2")
        buf.write(u"\u0085\u0087\3\2\2\2\u0086\u0081\3\2\2\2\u0087\u008a")
        buf.write(u"\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write(u"\u008b\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c\7\r\2")
        buf.write(u"\2\u008c\u008d\7+\2\2\u008d\u008e\5\6\4\2\u008e\u008f")
        buf.write(u"\b\7\1\2\u008f\r\3\2\2\2\u0090\u0091\5\32\16\2\u0091")
        buf.write(u"\u0092\b\b\1\2\u0092\u00f6\3\2\2\2\u0093\u0094\7\t\2")
        buf.write(u"\2\u0094\u0095\7\35\2\2\u0095\u0096\7)\2\2\u0096\u0097")
        buf.write(u"\b\b\1\2\u0097\u0098\5\f\7\2\u0098\u0099\7*\2\2\u0099")
        buf.write(u"\u009a\b\b\1\2\u009a\u00f6\3\2\2\2\u009b\u009c\7\35\2")
        buf.write(u"\2\u009c\u009d\7%\2\2\u009d\u009e\7&\2\2\u009e\u009f")
        buf.write(u"\7$\2\2\u009f\u00f6\b\b\1\2\u00a0\u00a1\7\27\2\2\u00a1")
        buf.write(u"\u00a2\7\35\2\2\u00a2\u00a3\7$\2\2\u00a3\u00f6\b\b\1")
        buf.write(u"\2\u00a4\u00a5\7\35\2\2\u00a5\u00a6\7\27\2\2\u00a6\u00a7")
        buf.write(u"\7$\2\2\u00a7\u00f6\b\b\1\2\u00a8\u00a9\5\6\4\2\u00a9")
        buf.write(u"\u00aa\b\b\1\2\u00aa\u00f6\3\2\2\2\u00ab\u00ac\7\f\2")
        buf.write(u"\2\u00ac\u00ad\5\"\22\2\u00ad\u00ae\5\16\b\2\u00ae\u00b3")
        buf.write(u"\b\b\1\2\u00af\u00b0\7\16\2\2\u00b0\u00b1\5\16\b\2\u00b1")
        buf.write(u"\u00b2\b\b\1\2\u00b2\u00b4\3\2\2\2\u00b3\u00af\3\2\2")
        buf.write(u"\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write(u"\b\b\1\2\u00b6\u00f6\3\2\2\2\u00b7\u00ba\7\35\2\2\u00b8")
        buf.write(u"\u00b9\7\"\2\2\u00b9\u00bb\b\b\1\2\u00ba\u00b8\3\2\2")
        buf.write(u"\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd")
        buf.write(u"\7#\2\2\u00bd\u00be\5\"\22\2\u00be\u00bf\7$\2\2\u00bf")
        buf.write(u"\u00c0\b\b\1\2\u00c0\u00f6\3\2\2\2\u00c1\u00c2\7\35\2")
        buf.write(u"\2\u00c2\u00c3\7\'\2\2\u00c3\u00c4\5\"\22\2\u00c4\u00c5")
        buf.write(u"\7(\2\2\u00c5\u00cd\b\b\1\2\u00c6\u00c7\7\'\2\2\u00c7")
        buf.write(u"\u00c8\5\"\22\2\u00c8\u00c9\7(\2\2\u00c9\u00ca\b\b\1")
        buf.write(u"\2\u00ca\u00cc\3\2\2\2\u00cb\u00c6\3\2\2\2\u00cc\u00cf")
        buf.write(u"\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write(u"\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7#\2\2")
        buf.write(u"\u00d1\u00d2\5\"\22\2\u00d2\u00d3\7$\2\2\u00d3\u00d4")
        buf.write(u"\b\b\1\2\u00d4\u00f6\3\2\2\2\u00d5\u00d6\7\b\2\2\u00d6")
        buf.write(u"\u00d7\5\22\n\2\u00d7\u00d8\b\b\1\2\u00d8\u00f6\3\2\2")
        buf.write(u"\2\u00d9\u00da\7\n\2\2\u00da\u00db\b\b\1\2\u00db\u00dc")
        buf.write(u"\5\6\4\2\u00dc\u00dd\7\13\2\2\u00dd\u00de\7%\2\2\u00de")
        buf.write(u"\u00df\5\"\22\2\u00df\u00e0\7&\2\2\u00e0\u00e1\b\b\1")
        buf.write(u"\2\u00e1\u00f6\3\2\2\2\u00e2\u00e3\7\13\2\2\u00e3\u00e4")
        buf.write(u"\7%\2\2\u00e4\u00e5\5\"\22\2\u00e5\u00e6\7&\2\2\u00e6")
        buf.write(u"\u00e7\b\b\1\2\u00e7\u00e8\5\6\4\2\u00e8\u00e9\b\b\1")
        buf.write(u"\2\u00e9\u00f6\3\2\2\2\u00ea\u00eb\7\17\2\2\u00eb\u00ec")
        buf.write(u"\7%\2\2\u00ec\u00f0\b\b\1\2\u00ed\u00ee\5\"\22\2\u00ee")
        buf.write(u"\u00ef\b\b\1\2\u00ef\u00f1\3\2\2\2\u00f0\u00ed\3\2\2")
        buf.write(u"\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3")
        buf.write(u"\7&\2\2\u00f3\u00f4\7$\2\2\u00f4\u00f6\b\b\1\2\u00f5")
        buf.write(u"\u0090\3\2\2\2\u00f5\u0093\3\2\2\2\u00f5\u009b\3\2\2")
        buf.write(u"\2\u00f5\u00a0\3\2\2\2\u00f5\u00a4\3\2\2\2\u00f5\u00a8")
        buf.write(u"\3\2\2\2\u00f5\u00ab\3\2\2\2\u00f5\u00b7\3\2\2\2\u00f5")
        buf.write(u"\u00c1\3\2\2\2\u00f5\u00d5\3\2\2\2\u00f5\u00d9\3\2\2")
        buf.write(u"\2\u00f5\u00e2\3\2\2\2\u00f5\u00ea\3\2\2\2\u00f6\17\3")
        buf.write(u"\2\2\2\u00f7\u00f8\7\37\2\2\u00f8\u00f9\b\t\1\2\u00f9")
        buf.write(u"\21\3\2\2\2\u00fa\u00fb\7%\2\2\u00fb\u00fc\5\n\6\2\u00fc")
        buf.write(u"\u00fd\b\n\1\2\u00fd\u00fe\5\"\22\2\u00fe\u00ff\7$\2")
        buf.write(u"\2\u00ff\u0100\7\35\2\2\u0100\u0102\b\n\1\2\u0101\u0103")
        buf.write(u"\7\"\2\2\u0102\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write(u"\u0104\3\2\2\2\u0104\u0105\7#\2\2\u0105\u0106\5\"\22")
        buf.write(u"\2\u0106\u0107\7&\2\2\u0107\u0108\5\6\4\2\u0108\u0109")
        buf.write(u"\b\n\1\2\u0109\23\3\2\2\2\u010a\u010b\7#\2\2\u010b\25")
        buf.write(u"\3\2\2\2\u010c\u010d\t\2\2\2\u010d\27\3\2\2\2\u010e\u010f")
        buf.write(u"\t\3\2\2\u010f\31\3\2\2\2\u0110\u0114\7\20\2\2\u0111")
        buf.write(u"\u0112\7\21\2\2\u0112\u0114\b\16\1\2\u0113\u0110\3\2")
        buf.write(u"\2\2\u0113\u0111\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116")
        buf.write(u"\7%\2\2\u0116\u0117\5\"\22\2\u0117\u0118\7&\2\2\u0118")
        buf.write(u"\u0119\7$\2\2\u0119\u011a\b\16\1\2\u011a\33\3\2\2\2\u011b")
        buf.write(u"\u011c\7%\2\2\u011c\u011e\b\17\1\2\u011d\u011f\5\36\20")
        buf.write(u"\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120")
        buf.write(u"\3\2\2\2\u0120\u0121\7&\2\2\u0121\u0122\b\17\1\2\u0122")
        buf.write(u"\35\3\2\2\2\u0123\u0128\5 \21\2\u0124\u0125\7,\2\2\u0125")
        buf.write(u"\u0127\5 \21\2\u0126\u0124\3\2\2\2\u0127\u012a\3\2\2")
        buf.write(u"\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\37\3")
        buf.write(u"\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\5\26\f\2\u012c")
        buf.write(u"\u012d\7\35\2\2\u012d!\3\2\2\2\u012e\u012f\5$\23\2\u012f")
        buf.write(u"\u0136\b\22\1\2\u0130\u0131\7\24\2\2\u0131\u0132\5$\23")
        buf.write(u"\2\u0132\u0133\b\22\1\2\u0133\u0135\3\2\2\2\u0134\u0130")
        buf.write(u"\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136")
        buf.write(u"\u0137\3\2\2\2\u0137#\3\2\2\2\u0138\u0136\3\2\2\2\u0139")
        buf.write(u"\u013a\5&\24\2\u013a\u0141\b\23\1\2\u013b\u013c\7\26")
        buf.write(u"\2\2\u013c\u013d\5&\24\2\u013d\u013e\b\23\1\2\u013e\u0140")
        buf.write(u"\3\2\2\2\u013f\u013b\3\2\2\2\u0140\u0143\3\2\2\2\u0141")
        buf.write(u"\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142%\3\2\2\2\u0143")
        buf.write(u"\u0141\3\2\2\2\u0144\u0145\5(\25\2\u0145\u014c\b\24\1")
        buf.write(u"\2\u0146\u0147\7\30\2\2\u0147\u0148\5(\25\2\u0148\u0149")
        buf.write(u"\b\24\1\2\u0149\u014b\3\2\2\2\u014a\u0146\3\2\2\2\u014b")
        buf.write(u"\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2")
        buf.write(u"\2\u014d\'\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0150\5")
        buf.write(u"*\26\2\u0150\u0157\b\25\1\2\u0151\u0152\7\31\2\2\u0152")
        buf.write(u"\u0153\5*\26\2\u0153\u0154\b\25\1\2\u0154\u0156\3\2\2")
        buf.write(u"\2\u0155\u0151\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155")
        buf.write(u"\3\2\2\2\u0157\u0158\3\2\2\2\u0158)\3\2\2\2\u0159\u0157")
        buf.write(u"\3\2\2\2\u015a\u015b\5,\27\2\u015b\u0162\b\26\1\2\u015c")
        buf.write(u"\u015d\7\32\2\2\u015d\u015e\5,\27\2\u015e\u015f\b\26")
        buf.write(u"\1\2\u015f\u0161\3\2\2\2\u0160\u015c\3\2\2\2\u0161\u0164")
        buf.write(u"\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write(u"+\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\5.\30\2\u0166")
        buf.write(u"\u0167\b\27\1\2\u0167\u0171\3\2\2\2\u0168\u0169\7\25")
        buf.write(u"\2\2\u0169\u0171\5,\27\2\u016a\u016b\7%\2\2\u016b\u016c")
        buf.write(u"\7\31\2\2\u016c\u016d\5,\27\2\u016d\u016e\b\27\1\2\u016e")
        buf.write(u"\u016f\7&\2\2\u016f\u0171\3\2\2\2\u0170\u0165\3\2\2\2")
        buf.write(u"\u0170\u0168\3\2\2\2\u0170\u016a\3\2\2\2\u0171-\3\2\2")
        buf.write(u"\2\u0172\u0173\7\37\2\2\u0173\u0199\b\30\1\2\u0174\u0175")
        buf.write(u"\7\34\2\2\u0175\u0199\b\30\1\2\u0176\u0177\7 \2\2\u0177")
        buf.write(u"\u0199\b\30\1\2\u0178\u0179\7\33\2\2\u0179\u0199\b\30")
        buf.write(u"\1\2\u017a\u017b\7%\2\2\u017b\u017c\5\"\22\2\u017c\u017d")
        buf.write(u"\b\30\1\2\u017d\u017e\7&\2\2\u017e\u0199\3\2\2\2\u017f")
        buf.write(u"\u0180\7\35\2\2\u0180\u0199\b\30\1\2\u0181\u0182\7\35")
        buf.write(u"\2\2\u0182\u0183\7\'\2\2\u0183\u0184\5\"\22\2\u0184\u0185")
        buf.write(u"\7(\2\2\u0185\u018d\b\30\1\2\u0186\u0187\7\'\2\2\u0187")
        buf.write(u"\u0188\5\"\22\2\u0188\u0189\7(\2\2\u0189\u018a\b\30\1")
        buf.write(u"\2\u018a\u018c\3\2\2\2\u018b\u0186\3\2\2\2\u018c\u018f")
        buf.write(u"\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write(u"\u0190\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\b\30\1")
        buf.write(u"\2\u0191\u0199\3\2\2\2\u0192\u0193\7\27\2\2\u0193\u0194")
        buf.write(u"\7\35\2\2\u0194\u0199\b\30\1\2\u0195\u0196\7\35\2\2\u0196")
        buf.write(u"\u0197\7\27\2\2\u0197\u0199\b\30\1\2\u0198\u0172\3\2")
        buf.write(u"\2\2\u0198\u0174\3\2\2\2\u0198\u0176\3\2\2\2\u0198\u0178")
        buf.write(u"\3\2\2\2\u0198\u017a\3\2\2\2\u0198\u017f\3\2\2\2\u0198")
        buf.write(u"\u0181\3\2\2\2\u0198\u0192\3\2\2\2\u0198\u0195\3\2\2")
        buf.write(u"\2\u0199/\3\2\2\2\34\65OQZbgy\177\u0088\u00b3\u00ba\u00cd")
        buf.write(u"\u00f0\u00f5\u0102\u0113\u011e\u0128\u0136\u0141\u014c")
        buf.write(u"\u0157\u0162\u0170\u018d\u0198")
        return buf.getvalue()


class ukeleleParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'void'", u"'int'", u"'string'", u"'float'", 
                     u"'def'", u"'for'", u"'match'", u"'do'", u"'while'", 
                     u"'if'", u"'_'", u"'else'", u"'return'", u"'print'", 
                     u"'println'", u"'bool'", u"'auto'", u"'or'", u"'not'", 
                     u"'and'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"':'", u"'='", u"';'", u"'('", u"')'", u"'['", u"']'", 
                     u"'{'", u"'}'", u"'->'", u"','" ]

    symbolicNames = [ u"<INVALID>", u"VOID", u"INT", u"STRING", u"FLOAT", 
                      u"DEF", u"FOR", u"MATCH", u"DO", u"WHILE", u"IF", 
                      u"ANONYMOUS", u"ELSE", u"RETURN", u"PRINT", u"PRINTLN", 
                      u"BOOL", u"AUTO", u"OR", u"NOT", u"AND", u"POSTADDOP", 
                      u"RELOP", u"ADDOP", u"MULOP", u"BOOLEANO", u"TEXT", 
                      u"IDENTIFIER", u"LETTER", u"INTEGER", u"REAL", u"DIGITS", 
                      u"COLON", u"ASSIGN", u"SEMICOLON", u"LPAREN", u"RPAREN", 
                      u"LCOR", u"RCOR", u"LBRACKET", u"RBRACKET", u"ARROW", 
                      u"COMMA", u"BlockComment", u"LineComment", u"WS" ]

    RULE_s = 0
    RULE_funcdef = 1
    RULE_block = 2
    RULE_declins = 3
    RULE_decl = 4
    RULE_matching = 5
    RULE_instr = 6
    RULE_dims = 7
    RULE_forexpr = 8
    RULE_assignment_operator = 9
    RULE_type_specifier = 10
    RULE_type_simple = 11
    RULE_print_operation = 12
    RULE_parameters = 13
    RULE_argument_expression_list = 14
    RULE_definition = 15
    RULE_expr = 16
    RULE_eand = 17
    RULE_erel = 18
    RULE_esum = 19
    RULE_term = 20
    RULE_factor = 21
    RULE_base = 22

    ruleNames =  [ u"s", u"funcdef", u"block", u"declins", u"decl", u"matching", 
                   u"instr", u"dims", u"forexpr", u"assignment_operator", 
                   u"type_specifier", u"type_simple", u"print_operation", 
                   u"parameters", u"argument_expression_list", u"definition", 
                   u"expr", u"eand", u"erel", u"esum", u"term", u"factor", 
                   u"base" ]

    EOF = Token.EOF
    VOID=1
    INT=2
    STRING=3
    FLOAT=4
    DEF=5
    FOR=6
    MATCH=7
    DO=8
    WHILE=9
    IF=10
    ANONYMOUS=11
    ELSE=12
    RETURN=13
    PRINT=14
    PRINTLN=15
    BOOL=16
    AUTO=17
    OR=18
    NOT=19
    AND=20
    POSTADDOP=21
    RELOP=22
    ADDOP=23
    MULOP=24
    BOOLEANO=25
    TEXT=26
    IDENTIFIER=27
    LETTER=28
    INTEGER=29
    REAL=30
    DIGITS=31
    COLON=32
    ASSIGN=33
    SEMICOLON=34
    LPAREN=35
    RPAREN=36
    LCOR=37
    RCOR=38
    LBRACKET=39
    RBRACKET=40
    ARROW=41
    COMMA=42
    BlockComment=43
    LineComment=44
    WS=45

    def __init__(self, input):
        super(ukeleleParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self.types = {'int': 'int32', 'string': 'string', 'bool': 'bool', 'float': 'float32'}
        self.RESERVED_WORDS = ['match', 'int', 'string', 'float', 'main', 'bool', 'Print', 'Println', 'auto', 'True', 'False']
        self.branches = 0


    class SContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None):
            super(ukeleleParser.SContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.code = None
            self.from_funcdef = None # FuncdefContext
            self.ts = ts

        def funcdef(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.FuncdefContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.FuncdefContext,i)


        def getRuleIndex(self):
            return ukeleleParser.RULE_s

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterS(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitS(self)




    def s(self, ts):

        localctx = ukeleleParser.SContext(self, self._ctx, self.state, ts)
        self.enterRule(localctx, 0, self.RULE_s)

        localctx.code = ".assembly __ukelele__cil__file__ {}\n.assembly extern mscorlib {}\n\n"

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ukeleleParser.DEF:
                self.state = 46
                localctx.from_funcdef = self.funcdef(localctx.ts, Scope.BLOCK_LOCAL)
                localctx.code += localctx.from_funcdef.code
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            element = localctx.ts.get('main')
            if not element:
                error_message_without_line('"main" not defined')
            elif element.stype != 'void':
                error_message_without_line('"main" function should return void')

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, scope=None):
            super(ukeleleParser.FuncdefContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.scope = None
            self.code = None
            self._IDENTIFIER = None # Token
            self.params = None # ParametersContext
            self._type_specifier = None # Type_specifierContext
            self.from_block = None # BlockContext
            self.ts = ts
            self.scope = scope

        def DEF(self):
            return self.getToken(ukeleleParser.DEF, 0)

        def IDENTIFIER(self):
            return self.getToken(ukeleleParser.IDENTIFIER, 0)

        def type_specifier(self):
            return self.getTypedRuleContext(ukeleleParser.Type_specifierContext,0)


        def parameters(self):
            return self.getTypedRuleContext(ukeleleParser.ParametersContext,0)


        def block(self):
            return self.getTypedRuleContext(ukeleleParser.BlockContext,0)


        def getRuleIndex(self):
            return ukeleleParser.RULE_funcdef

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterFuncdef(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitFuncdef(self)




    def funcdef(self, ts, scope):

        localctx = ukeleleParser.FuncdefContext(self, self._ctx, self.state, ts, scope)
        self.enterRule(localctx, 2, self.RULE_funcdef)

        localctx.code = ""

        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ukeleleParser.DEF)
            self.state = 57
            localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
            localctx.code += ".method static "
            self.state = 59
            localctx.params = self.parameters()
            self.state = 60
            localctx._type_specifier = self.type_specifier()
            localctx.code +=(None if localctx._type_specifier is None else self._input.getText((localctx._type_specifier.start,localctx._type_specifier.stop))) + ' '

            element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

            if not element:
                if (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) == 'main':
                    localctx.ts.add(name=(None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), stype=(None if localctx._type_specifier is None else self._input.getText((localctx._type_specifier.start,localctx._type_specifier.stop))), isFunction=True, scope=Scope.GLOBAL, line=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))
                    localctx.code += "Main" + (None if localctx.params is None else self._input.getText((localctx.params.start,localctx.params.stop))) + " cil managed {\n.entrypoint\n"
                else:
                    localctx.ts.add(name=(None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), stype=(None if localctx._type_specifier is None else self._input.getText((localctx._type_specifier.start,localctx._type_specifier.stop))), isFunction=True, scope=Scope.GLOBAL, line=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))
                    localctx.code += (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + (None if localctx.params is None else self._input.getText((localctx.params.start,localctx.params.stop))) + " cil managed {\n"
                ts_son = SymbolsTable(localctx.ts)
            else:
                already_defined_message((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line), element.line)

            self.state = 63
            localctx.from_block = self.block(ts_son, localctx.scope, (None if localctx._type_specifier is None else self._input.getText((localctx._type_specifier.start,localctx._type_specifier.stop))))

            if not localctx.from_block.has_return:
                error_message('Expected return statement for function "' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '"', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))


            localctx.code += ".maxstack " + str(localctx.from_block.stack_out) + "\n" + '.locals init ('
            local_vars = []
            for t,n,i in localctx.from_block.locals:
                if '[' and ']' in t:
                    array_type = t.split('[')[0]
                    local_vars.append(t.replace(array_type, self.types[array_type])  + ' ' +  n + '_' + str(i))
                else:
                    if t == 'int':
                        local_vars.append('int32 ' + n + '_' + str(i))
                    elif t == 'bool':
                        local_vars.append('bool ' + n + '_' + str(i))
                    elif t == 'float':
                        local_vars.append('float32 ' + n + '_' + str(i))
            localctx.code += ','.join(local_vars) + ')\n'

            localctx.code += localctx.from_block.body 
            #if (None if localctx._type_specifier is None else self._input.getText((localctx._type_specifier.start,localctx._type_specifier.stop))) == 'void':
            #    localctx.code += 'ret\n'
            localctx.code += "}\n"

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, scope=None, expected_return=None):
            super(ukeleleParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.scope = None
            self.expected_return = None
            self.stack_out = None
            self.body = None
            self.locals = None
            self.type_out = None
            self.has_return = None
            self.from_declins = None # DeclinsContext
            self.ts = ts
            self.scope = scope
            self.expected_return = expected_return

        def LBRACKET(self):
            return self.getToken(ukeleleParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ukeleleParser.RBRACKET, 0)

        def declins(self):
            return self.getTypedRuleContext(ukeleleParser.DeclinsContext,0)


        def getRuleIndex(self):
            return ukeleleParser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitBlock(self)




    def block(self, ts, scope, expected_return):

        localctx = ukeleleParser.BlockContext(self, self._ctx, self.state, ts, scope, expected_return)
        self.enterRule(localctx, 4, self.RULE_block)

        localctx.body = ''
        localctx.stack_out = 0
        localctx.locals = []

        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ukeleleParser.LBRACKET)
            self.state = 67
            localctx.from_declins = self.declins(ts, localctx.scope, localctx.expected_return)

            localctx.has_return = localctx.from_declins.has_return
            localctx.type_out = localctx.from_declins.type_out
            localctx.locals += localctx.from_declins.locals
            localctx.stack_out += localctx.from_declins.stack_out
            localctx.body += localctx.from_declins.body

            self.state = 69
            self.match(ukeleleParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclinsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, scope=None, expected_return=None):
            super(ukeleleParser.DeclinsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.scope = None
            self.expected_return = None
            self.stack_out = None
            self.body = None
            self.locals = None
            self.type_out = None
            self.has_return = None
            self.from_instr = None # InstrContext
            self.from_decl = None # DeclContext
            self.ts = ts
            self.scope = scope
            self.expected_return = expected_return

        def instr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.InstrContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.InstrContext,i)


        def decl(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.DeclContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.DeclContext,i)


        def getRuleIndex(self):
            return ukeleleParser.RULE_declins

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterDeclins(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitDeclins(self)




    def declins(self, ts, scope, expected_return):

        localctx = ukeleleParser.DeclinsContext(self, self._ctx, self.state, ts, scope, expected_return)
        self.enterRule(localctx, 6, self.RULE_declins)

        localctx.stack_out = 0
        localctx.locals = []
        localctx.body = ''

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ukeleleParser.INT) | (1 << ukeleleParser.STRING) | (1 << ukeleleParser.FLOAT) | (1 << ukeleleParser.FOR) | (1 << ukeleleParser.MATCH) | (1 << ukeleleParser.DO) | (1 << ukeleleParser.WHILE) | (1 << ukeleleParser.IF) | (1 << ukeleleParser.RETURN) | (1 << ukeleleParser.PRINT) | (1 << ukeleleParser.PRINTLN) | (1 << ukeleleParser.BOOL) | (1 << ukeleleParser.AUTO) | (1 << ukeleleParser.POSTADDOP) | (1 << ukeleleParser.IDENTIFIER) | (1 << ukeleleParser.LBRACKET))) != 0):
                self.state = 77
                token = self._input.LA(1)
                if token in [ukeleleParser.FOR, ukeleleParser.MATCH, ukeleleParser.DO, ukeleleParser.WHILE, ukeleleParser.IF, ukeleleParser.RETURN, ukeleleParser.PRINT, ukeleleParser.PRINTLN, ukeleleParser.POSTADDOP, ukeleleParser.IDENTIFIER, ukeleleParser.LBRACKET]:
                    self.state = 71
                    localctx.from_instr = self.instr(ts, localctx.scope, localctx.expected_return)

                    localctx.has_return = localctx.from_instr.has_return
                    localctx.type_out = localctx.from_instr.type_out
                    localctx.locals += localctx.from_instr.locals
                    localctx.stack_out += localctx.from_instr.stack_out 
                    localctx.body += localctx.from_instr.body


                elif token in [ukeleleParser.INT, ukeleleParser.STRING, ukeleleParser.FLOAT, ukeleleParser.BOOL, ukeleleParser.AUTO]:
                    self.state = 74
                    localctx.from_decl = self.decl(ts, localctx.scope)

                    localctx.locals += localctx.from_decl.locals
                    localctx.stack_out += localctx.from_decl.stack_out 
                    localctx.body += localctx.from_decl.body


                else:
                    raise NoViableAltException(self)

                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, scope=None):
            super(ukeleleParser.DeclContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.scope = None
            self.stack_out = None
            self.body = None
            self.locals = None
            self._type_simple = None # Type_simpleContext
            self._IDENTIFIER = None # Token
            self.from_expr = None # ExprContext
            self.from_dims = None # DimsContext
            self.from_another_dims = None # DimsContext
            self.ts = ts
            self.scope = scope

        def type_simple(self):
            return self.getTypedRuleContext(ukeleleParser.Type_simpleContext,0)


        def IDENTIFIER(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.IDENTIFIER)
            else:
                return self.getToken(ukeleleParser.IDENTIFIER, i)

        def SEMICOLON(self):
            return self.getToken(ukeleleParser.SEMICOLON, 0)

        def ASSIGN(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.ASSIGN)
            else:
                return self.getToken(ukeleleParser.ASSIGN, i)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.COMMA)
            else:
                return self.getToken(ukeleleParser.COMMA, i)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.ExprContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.ExprContext,i)


        def LCOR(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.LCOR)
            else:
                return self.getToken(ukeleleParser.LCOR, i)

        def RCOR(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.RCOR)
            else:
                return self.getToken(ukeleleParser.RCOR, i)

        def dims(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.DimsContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.DimsContext,i)


        def getRuleIndex(self):
            return ukeleleParser.RULE_decl

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterDecl(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitDecl(self)




    def decl(self, ts, scope):

        localctx = ukeleleParser.DeclContext(self, self._ctx, self.state, ts, scope)
        self.enterRule(localctx, 8, self.RULE_decl)

        assignation = False
        dimensions = 0
        numelements = 0
        localctx.body = ""
        localctx.stack_out = 0
        localctx.locals = []

        self._la = 0 # Token type
        try:
            self.state = 125
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                localctx._type_simple = self.type_simple()
                self.state = 83
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 88
                _la = self._input.LA(1)
                if _la==ukeleleParser.ASSIGN:
                    self.state = 84
                    self.match(ukeleleParser.ASSIGN)
                    self.state = 85
                    localctx.from_expr = self.expr(ts, localctx.scope)
                    assignation=True



                if not (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) in self.RESERVED_WORDS:
                    element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                    if not element:
                        localctx.ts.add(name=(None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), stype=(None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))), isFunction=False, scope=localctx.scope, line=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))
                        element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                        if (None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))) == 'auto' and not assignation:
                            error_message('Type for variable "' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '" can not be deducted', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))

                        if (None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))) != 'auto':
                            localctx.locals.append(((None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))), (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), element.index))
                        
                        if assignation:
                            if (None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))) == 'auto':
                                identifier = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))
                                identifier.stype = localctx.from_expr.type_out
                                localctx.locals.append((localctx.from_expr.type_out, (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), identifier.index))

                            localctx.stack_out += localctx.from_expr.stack_out 
                            localctx.body += localctx.from_expr.expr_out + 'stloc.' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                            assignation = False
                    else:
                        if localctx.scope == Scope.LOOP:
                            error_message('"' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '" shadows a variable', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))
                        else:
                            already_defined_message((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line), element.line)
                else:
                    reserved_word_message((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))

                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ukeleleParser.COMMA:
                    self.state = 91
                    self.match(ukeleleParser.COMMA)
                    self.state = 92
                    localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                    self.state = 96
                    _la = self._input.LA(1)
                    if _la==ukeleleParser.ASSIGN:
                        self.state = 93
                        self.match(ukeleleParser.ASSIGN)
                        assignation=True
                        self.state = 95
                        self.expr(ts, localctx.scope)



                    if not (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) in self.RESERVED_WORDS:
                        element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx.scope != Scope.LOOP)
                        if not element:
                            localctx.ts.add(name=(None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), stype=(None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))), isFunction=False, scope=localctx.scope, line=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))
                            element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx.scope != Scope.LOOP)

                            if (None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))) != 'auto':
                                localctx.locals.append(((None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))), (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), element.index))

                            
                            if assignation:
                                if (None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))) == 'auto':
                                    identifier = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))
                                    identifier.stype = localctx.from_expr.type_out
                                    localctx.locals.append((localctx.from_expr.type_out, (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), identifier.index))

                                localctx.stack_out += localctx.from_expr.stack_out 
                                localctx.body += localctx.from_expr.expr_out + 'stloc.' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                                assignation = False
                        else:
                            already_defined_message((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line), element.line)
                    else:
                        reserved_word_message((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))

                    self.state = 103
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 104
                self.match(ukeleleParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                localctx._type_simple = self.type_simple()
                self.state = 107
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 108
                self.match(ukeleleParser.LCOR)
                self.state = 109
                localctx.from_dims = self.dims()
                self.state = 110
                self.match(ukeleleParser.RCOR)

                dimensions = 1
                elements = [localctx.from_dims.body]

                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ukeleleParser.LCOR:
                    self.state = 112
                    self.match(ukeleleParser.LCOR)
                    self.state = 113
                    localctx.from_another_dims = self.dims()
                    self.state = 114
                    self.match(ukeleleParser.RCOR)

                    dimensions += 1
                    elements.append(localctx.from_another_dims.body)

                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 122
                self.match(ukeleleParser.SEMICOLON)

                dims = '[' 
                if dimensions > 1:
                    for i in range(dimensions):
                        dims += ','
                dims += ']'
                localctx.ts.add(name=(None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), stype=(None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))) + dims, isFunction=False, scope=Scope.BLOCK_LOCAL if not localctx.scope else localctx.scope, line=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))
                localctx.locals.append(((None if localctx._type_simple is None else self._input.getText((localctx._type_simple.start,localctx._type_simple.stop))) + dims, (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index))

                localctx.body += 'ldc.i4 ' + str(reduce(lambda x, y: int(x)*int(y), elements)) + '\n'
                localctx.stack_out += 1
                localctx.body += 'newarr [mscorlib]System.Int32\n'
                localctx.body += 'stloc.' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MatchingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, scope=None, expected_return=None, index=None):
            super(ukeleleParser.MatchingContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.scope = None
            self.expected_return = None
            self.index = None
            self.stack_out = None
            self.body = None
            self.locals = None
            self.type_out = None
            self.has_return = None
            self.from_base = None # BaseContext
            self.from_block = None # BlockContext
            self.from_anon_block = None # BlockContext
            self.ts = ts
            self.scope = scope
            self.expected_return = expected_return
            self.index = index

        def ANONYMOUS(self):
            return self.getToken(ukeleleParser.ANONYMOUS, 0)

        def ARROW(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.ARROW)
            else:
                return self.getToken(ukeleleParser.ARROW, i)

        def block(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.BlockContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.BlockContext,i)


        def base(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.BaseContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.BaseContext,i)


        def getRuleIndex(self):
            return ukeleleParser.RULE_matching

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterMatching(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitMatching(self)




    def matching(self, ts, scope, expected_return, index):

        localctx = ukeleleParser.MatchingContext(self, self._ctx, self.state, ts, scope, expected_return, index)
        self.enterRule(localctx, 10, self.RULE_matching)

        localctx.stack_out = 0
        localctx.body = ""
        localctx.locals = []
        final_body = ""

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ukeleleParser.POSTADDOP) | (1 << ukeleleParser.BOOLEANO) | (1 << ukeleleParser.TEXT) | (1 << ukeleleParser.IDENTIFIER) | (1 << ukeleleParser.INTEGER) | (1 << ukeleleParser.REAL) | (1 << ukeleleParser.LPAREN))) != 0):
                self.state = 127
                localctx.from_base = self.base(localctx.ts, '', localctx.scope)
                self.state = 128
                self.match(ukeleleParser.ARROW)
                self.state = 129
                localctx.from_block = self.block(localctx.ts, localctx.scope, localctx.expected_return)

                self.branches += 1
                localctx.body += localctx.index
                localctx.body += localctx.from_base.expr_out
                localctx.stack_out += localctx.from_base.stack_out + localctx.from_block.stack_out + 1
                localctx.body += 'beq L' + str(self.branches) + '\n'
                final_body += 'L' + str(self.branches) + ':\n' + localctx.from_block.body + 'br L{final_branch}\n'
                localctx.locals += localctx.from_block.locals

                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
            self.match(ukeleleParser.ANONYMOUS)
            self.state = 138
            self.match(ukeleleParser.ARROW)
            self.state = 139
            localctx.from_anon_block = self.block(localctx.ts, localctx.scope, localctx.expected_return)

            self.branches += 1
            localctx.body += 'br L' + str(self.branches) + '\n'
            localctx.body += final_body.format(final_branch=str(self.branches)) + 'L' + str(self.branches) + ':\n' + localctx.from_anon_block.body
            localctx.stack_out += localctx.from_anon_block.stack_out
            localctx.locals += localctx.from_anon_block.locals

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstrContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, scope=None, expected_return=None):
            super(ukeleleParser.InstrContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.scope = None
            self.expected_return = None
            self.stack_out = None
            self.body = None
            self.locals = None
            self.type_out = None
            self.has_return = None
            self.operation = None # Print_operationContext
            self._IDENTIFIER = None # Token
            self.from_matching = None # MatchingContext
            self._POSTADDOP = None # Token
            self.from_block = None # BlockContext
            self.condition = None # ExprContext
            self._expr = None # ExprContext
            self.from_instr = None # InstrContext
            self.from_another_instr = None # InstrContext
            self.from_expr = None # ExprContext
            self.pos = None # ExprContext
            self.another_pos = None # ExprContext
            self.new_value = None # ExprContext
            self.from_forexpr = None # ForexprContext
            self.comparison = None # ExprContext
            self._RETURN = None # Token
            self.ts = ts
            self.scope = scope
            self.expected_return = expected_return

        def print_operation(self):
            return self.getTypedRuleContext(ukeleleParser.Print_operationContext,0)


        def MATCH(self):
            return self.getToken(ukeleleParser.MATCH, 0)

        def IDENTIFIER(self):
            return self.getToken(ukeleleParser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(ukeleleParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ukeleleParser.RBRACKET, 0)

        def matching(self):
            return self.getTypedRuleContext(ukeleleParser.MatchingContext,0)


        def LPAREN(self):
            return self.getToken(ukeleleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ukeleleParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ukeleleParser.SEMICOLON, 0)

        def POSTADDOP(self):
            return self.getToken(ukeleleParser.POSTADDOP, 0)

        def block(self):
            return self.getTypedRuleContext(ukeleleParser.BlockContext,0)


        def IF(self):
            return self.getToken(ukeleleParser.IF, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.ExprContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.ExprContext,i)


        def instr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.InstrContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.InstrContext,i)


        def ELSE(self):
            return self.getToken(ukeleleParser.ELSE, 0)

        def ASSIGN(self):
            return self.getToken(ukeleleParser.ASSIGN, 0)

        def COLON(self):
            return self.getToken(ukeleleParser.COLON, 0)

        def LCOR(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.LCOR)
            else:
                return self.getToken(ukeleleParser.LCOR, i)

        def RCOR(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.RCOR)
            else:
                return self.getToken(ukeleleParser.RCOR, i)

        def FOR(self):
            return self.getToken(ukeleleParser.FOR, 0)

        def forexpr(self):
            return self.getTypedRuleContext(ukeleleParser.ForexprContext,0)


        def DO(self):
            return self.getToken(ukeleleParser.DO, 0)

        def WHILE(self):
            return self.getToken(ukeleleParser.WHILE, 0)

        def RETURN(self):
            return self.getToken(ukeleleParser.RETURN, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_instr

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterInstr(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitInstr(self)




    def instr(self, ts, scope, expected_return):

        localctx = ukeleleParser.InstrContext(self, self._ctx, self.state, ts, scope, expected_return)
        self.enterRule(localctx, 12, self.RULE_instr)

        ts_son = None
        localctx.stack_out = 0
        localctx.body = ""
        localctx.locals = []
        initialize = False

        self._la = 0 # Token type
        try:
            self.state = 243
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                localctx.operation = self.print_operation(0, localctx.ts, localctx.scope)

                localctx.stack_out += localctx.operation.stack_out
                localctx.body += localctx.operation.operation

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(ukeleleParser.MATCH)
                self.state = 146
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 147
                self.match(ukeleleParser.LBRACKET)

                element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                if element:
                    #localctx.body += 'ldloc ' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                    index = 'ldloc ' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                    #localctx.stack_out += 1
                else:
                    error_message('"' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '" not defined', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))

                self.state = 149
                localctx.from_matching = self.matching(localctx.ts, localctx.scope, localctx.expected_return, index)
                self.state = 150
                self.match(ukeleleParser.RBRACKET)

                localctx.stack_out += localctx.from_matching.stack_out
                localctx.body += localctx.from_matching.body
                localctx.locals += localctx.from_matching.locals

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 154
                self.match(ukeleleParser.LPAREN)
                self.state = 155
                self.match(ukeleleParser.RPAREN)
                self.state = 156
                self.match(ukeleleParser.SEMICOLON)
                 # function definition TODO
                element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))
                if element:
                    localctx.body += 'call ' + element.stype + ' ' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '()\n'

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                localctx._POSTADDOP = self.match(ukeleleParser.POSTADDOP)
                self.state = 159
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 160
                self.match(ukeleleParser.SEMICOLON)
                 
                localctx.body += 'ldloc ' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'

                if localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).stype  == 'int':
                    localctx.body += 'ldc.i4 1\nadd\n' if (None if localctx._POSTADDOP is None else localctx._POSTADDOP.text) == '++' else 'ldc.i4 1\nsub\n'
                elif localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).stype  == 'float':
                    localctx.body += 'ldc.r4 1\nadd\n' if (None if localctx._POSTADDOP is None else localctx._POSTADDOP.text) == '++' else 'ldc.r4 1\nsub\n'

                localctx.body += 'stloc.' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                localctx.stack_out += 2
                localctx.type_out = 'int'

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 163
                localctx._POSTADDOP = self.match(ukeleleParser.POSTADDOP)
                self.state = 164
                self.match(ukeleleParser.SEMICOLON)

                localctx.body += 'ldloc ' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'

                if localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).stype  == 'int':
                    localctx.body += 'ldc.i4 1\nadd\n' if (None if localctx._POSTADDOP is None else localctx._POSTADDOP.text) == '++' else 'ldc.i4 1\nsub\n'
                elif localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).stype  == 'float':
                    localctx.body += 'ldc.r4 1\nadd\n' if (None if localctx._POSTADDOP is None else localctx._POSTADDOP.text) == '++' else 'ldc.r4 1\nsub\n'

                localctx.body += 'stloc.' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                localctx.stack_out += 2
                localctx.type_out = 'int'

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 166
                localctx.from_block = self.block(localctx.ts, localctx.scope, localctx.expected_return)

                localctx.type_out = localctx.from_block.type_out
                localctx.stack_out = localctx.from_block.stack_out
                localctx.body += localctx.from_block.body

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 169
                self.match(ukeleleParser.IF)
                self.state = 170
                localctx.condition = localctx._expr = self.expr(localctx.ts, localctx.scope)
                self.state = 171
                localctx.from_instr = self.instr(localctx.ts, localctx.scope, localctx.expected_return)

                localctx.stack_out += 1
                self.branches += 1
                localctx.locals = localctx.from_instr.locals
                localctx.body += localctx._expr.expr_out + 'ldc.i4 1\n'
                localctx.body += 'beq L' + str(self.branches) + '\n'

                self.state = 177
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 173
                    self.match(ukeleleParser.ELSE)
                    self.state = 174
                    localctx.from_another_instr = self.instr(localctx.ts, localctx.scope, localctx.expected_return)

                    localctx.stack_out += max(localctx.from_instr.stack_out, localctx.from_another_instr.stack_out)
                    localctx.body += localctx.from_another_instr.body
                    localctx.body += 'br L' + str(self.branches + 1) + '\n'




                localctx.body += 'L' + str(self.branches) + ':\n'
                self.branches += 1
                localctx.body += localctx.from_instr.body
                localctx.body += 'L' + str(self.branches) + ':\n'

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 181
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 184
                _la = self._input.LA(1)
                if _la==ukeleleParser.COLON:
                    self.state = 182
                    self.match(ukeleleParser.COLON)
                    initialize=True


                self.state = 186
                self.match(ukeleleParser.ASSIGN)
                self.state = 187
                localctx.from_expr = self.expr(localctx.ts, localctx.scope)
                self.state = 188
                self.match(ukeleleParser.SEMICOLON)

                element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                if element:
                    if not initialize:
                        localctx.stack_out += localctx.from_expr.stack_out
                        localctx.body += localctx.from_expr.expr_out + 'stloc.' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                else:
                    error_message('"' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '" not defined', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 191
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 192
                self.match(ukeleleParser.LCOR)
                self.state = 193
                localctx.pos = self.expr(localctx.ts, localctx.scope)
                self.state = 194
                self.match(ukeleleParser.RCOR)

                element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                if element:
                    array = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))
                    if array:
                        localctx.stack_out += localctx.pos.stack_out + 1
                        localctx.body += 'ldloc ' + str(array.index) + '\n' + localctx.pos.expr_out
                else:
                    error_message('"' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '" not defined', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))

                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ukeleleParser.LCOR:
                    self.state = 196
                    self.match(ukeleleParser.LCOR)
                    self.state = 197
                    localctx.another_pos = self.expr(localctx.ts, localctx.scope)
                    self.state = 198
                    self.match(ukeleleParser.RCOR)

                    if array:
                        localctx.stack_out += localctx.another_pos.stack_out
                        localctx.body += localctx.another_pos.expr_out + 'mul\n'

                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 206
                self.match(ukeleleParser.ASSIGN)
                self.state = 207
                localctx.new_value = self.expr(localctx.ts, localctx.scope)
                self.state = 208
                self.match(ukeleleParser.SEMICOLON)

                if array:
                    localctx.body += localctx.new_value.expr_out + 'stelem.'

                    if localctx.new_value.type_out == 'int' or localctx.new_value.type_out == 'bool':
                        localctx.body += 'i4\n'
                    elif localctx.new_value.type_out == 'float':
                        localctx.body += 'r4\n'
                    elif localctx.new_value.type_out == 'string':
                        localctx.body = localctx.body[:-1] + '\n'

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 211
                self.match(ukeleleParser.FOR)
                self.state = 212
                localctx.from_forexpr = self.forexpr(localctx.ts, localctx.expected_return)

                localctx.type_out = localctx.from_forexpr.type_out
                localctx.stack_out += localctx.from_forexpr.stack_out 
                localctx.body += localctx.from_forexpr.body
                localctx.locals += localctx.from_forexpr.locals

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 215
                self.match(ukeleleParser.DO)
                ts_son = SymbolsTable(localctx.ts)
                self.state = 217
                localctx.from_block = self.block(ts_son, Scope.LOOP, localctx.expected_return)
                self.state = 218
                self.match(ukeleleParser.WHILE)
                self.state = 219
                self.match(ukeleleParser.LPAREN)
                self.state = 220
                localctx.comparison = self.expr(localctx.ts, localctx.scope)
                self.state = 221
                self.match(ukeleleParser.RPAREN)

                localctx.type_out = localctx.from_block.type_out
                self.branches += 1
                localctx.locals = localctx.from_block.locals
                init_branch = self.branches
                localctx.stack_out += localctx.from_block.stack_out + 1 + localctx.comparison.stack_out
                localctx.body += 'L' + str(init_branch) + ':\n'
                localctx.body += localctx.from_block.body + localctx.comparison.expr_out + 'ldc.i4 1\nbeq L' + str(init_branch) + '\n'

                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 224
                self.match(ukeleleParser.WHILE)
                self.state = 225
                self.match(ukeleleParser.LPAREN)
                self.state = 226
                localctx.comparison = self.expr(localctx.ts, localctx.scope)
                self.state = 227
                self.match(ukeleleParser.RPAREN)
                ts_son = SymbolsTable(localctx.ts)
                self.state = 229
                localctx.from_block = self.block(ts_son, Scope.LOOP, localctx.expected_return)

                localctx.type_out = localctx.from_block.type_out
                self.branches += 1
                localctx.locals = localctx.from_block.locals
                init_branch = self.branches
                localctx.stack_out += localctx.comparison.stack_out + 1 + localctx.from_block.stack_out
                localctx.body += 'L' + str(init_branch) + ':\n'
                self.branches += 1
                localctx.body += localctx.comparison.expr_out + 'ldc.i4 1\nbne.un L' + str(self.branches) + '\n' + localctx.from_block.body + 'br L' + str(init_branch) + '\n' 
                localctx.body += 'L' + str(self.branches) + ':\n'

                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 232
                localctx._RETURN = self.match(ukeleleParser.RETURN)
                self.state = 233
                self.match(ukeleleParser.LPAREN)
                void_expr=True
                self.state = 238
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ukeleleParser.NOT) | (1 << ukeleleParser.POSTADDOP) | (1 << ukeleleParser.BOOLEANO) | (1 << ukeleleParser.TEXT) | (1 << ukeleleParser.IDENTIFIER) | (1 << ukeleleParser.INTEGER) | (1 << ukeleleParser.REAL) | (1 << ukeleleParser.LPAREN))) != 0):
                    self.state = 235
                    localctx.from_expr = self.expr(localctx.ts, localctx.scope)

                    localctx.type_out = localctx.from_expr.type_out
                    localctx.stack_out += localctx.from_expr.stack_out
                    localctx.body += localctx.from_expr.expr_out
                    void_expr = False



                self.state = 240
                self.match(ukeleleParser.RPAREN)
                self.state = 241
                self.match(ukeleleParser.SEMICOLON)

                localctx.has_return = True
                localctx.type_out = '' if not localctx.type_out else localctx.type_out

                if void_expr:
                    if localctx.expected_return == 'void':
                        pass
                    else:
                        error_message('Excepted returning "' + localctx.expected_return + '", and got "' + localctx.type_out + '"', (0 if localctx._RETURN is None else localctx._RETURN.line))
                else:
                    if localctx.expected_return == 'void':
                        error_message('Returning a not empty value while expecting void', (0 if localctx._RETURN is None else localctx._RETURN.line))
                    else:
                        if localctx.type_out != localctx.expected_return:
                            error_message('Excepted returning "' + localctx.expected_return + '", and got "' + localctx.type_out + '"', (0 if localctx._RETURN is None else localctx._RETURN.line))

                localctx.body += 'ret\n'

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DimsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ukeleleParser.DimsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.body = None
            self._INTEGER = None # Token

        def INTEGER(self):
            return self.getToken(ukeleleParser.INTEGER, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_dims

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterDims(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitDims(self)




    def dims(self):

        localctx = ukeleleParser.DimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dims)

        localctx.body = ""

        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            localctx._INTEGER = self.match(ukeleleParser.INTEGER)

            localctx.body += (None if localctx._INTEGER is None else localctx._INTEGER.text)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, expected_return=None):
            super(ukeleleParser.ForexprContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.expected_return = None
            self.stack_out = None
            self.body = None
            self.locals = None
            self.type_out = None
            self.initial_decl = None # DeclContext
            self.comparison = None # ExprContext
            self._IDENTIFIER = None # Token
            self.post_comparison = None # ExprContext
            self.body_for = None # BlockContext
            self.ts = ts
            self.expected_return = expected_return

        def LPAREN(self):
            return self.getToken(ukeleleParser.LPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ukeleleParser.SEMICOLON, 0)

        def IDENTIFIER(self):
            return self.getToken(ukeleleParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ukeleleParser.ASSIGN, 0)

        def RPAREN(self):
            return self.getToken(ukeleleParser.RPAREN, 0)

        def decl(self):
            return self.getTypedRuleContext(ukeleleParser.DeclContext,0)


        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.ExprContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.ExprContext,i)


        def block(self):
            return self.getTypedRuleContext(ukeleleParser.BlockContext,0)


        def COLON(self):
            return self.getToken(ukeleleParser.COLON, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_forexpr

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterForexpr(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitForexpr(self)




    def forexpr(self, ts, expected_return):

        localctx = ukeleleParser.ForexprContext(self, self._ctx, self.state, ts, expected_return)
        self.enterRule(localctx, 16, self.RULE_forexpr)

        ts_son = SymbolsTable(localctx.ts)
        localctx.stack_out = 0
        localctx.body = ""
        localctx.locals = []

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(ukeleleParser.LPAREN)
            self.state = 249
            localctx.initial_decl = self.decl(ts_son, Scope.LOOP)

            localctx.stack_out += localctx.initial_decl.stack_out 
            localctx.body += localctx.initial_decl.body
            localctx.locals += localctx.initial_decl.locals

            self.state = 251
            localctx.comparison = self.expr(ts_son, Scope.LOOP)
            self.state = 252
            self.match(ukeleleParser.SEMICOLON)
            self.state = 253
            localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)

            element = ts_son.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

            if not element:
                error_message('"' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '" not defined', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))

            self.state = 256
            _la = self._input.LA(1)
            if _la==ukeleleParser.COLON:
                self.state = 255
                self.match(ukeleleParser.COLON)


            self.state = 258
            self.match(ukeleleParser.ASSIGN)
            self.state = 259
            localctx.post_comparison = self.expr(ts_son, Scope.LOOP)
            self.state = 260
            self.match(ukeleleParser.RPAREN)
            self.state = 261
            localctx.body_for = self.block(ts_son, Scope.LOOP, localctx.expected_return)

            localctx.type_out = localctx.body_for.type_out
            localctx.locals += localctx.body_for.locals
            self.branches += 1
            init_branch = self.branches
            localctx.body += 'L' + str(init_branch) + ':\n'
            localctx.stack_out += localctx.comparison.stack_out + 1 + localctx.body_for.stack_out 
            self.branches += 1
            localctx.body += localctx.comparison.expr_out + 'ldc.i4 1\nbne.un L' + str(self.branches) + '\n' + localctx.body_for.body 
            localctx.body += localctx.post_comparison.expr_out + 'stloc.' + str(ts_son.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
            localctx.body += 'br L' + str(init_branch) + '\nL' + str(self.branches) + ':\n'

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignment_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ukeleleParser.Assignment_operatorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ukeleleParser.ASSIGN, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_assignment_operator

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = ukeleleParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ukeleleParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ukeleleParser.Type_specifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ukeleleParser.INT, 0)

        def VOID(self):
            return self.getToken(ukeleleParser.VOID, 0)

        def STRING(self):
            return self.getToken(ukeleleParser.STRING, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_type_specifier

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterType_specifier(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitType_specifier(self)




    def type_specifier(self):

        localctx = ukeleleParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ukeleleParser.VOID) | (1 << ukeleleParser.INT) | (1 << ukeleleParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_simpleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ukeleleParser.Type_simpleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ukeleleParser.INT, 0)

        def STRING(self):
            return self.getToken(ukeleleParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(ukeleleParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(ukeleleParser.BOOL, 0)

        def AUTO(self):
            return self.getToken(ukeleleParser.AUTO, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_type_simple

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterType_simple(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitType_simple(self)




    def type_simple(self):

        localctx = ukeleleParser.Type_simpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_simple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ukeleleParser.INT) | (1 << ukeleleParser.STRING) | (1 << ukeleleParser.FLOAT) | (1 << ukeleleParser.BOOL) | (1 << ukeleleParser.AUTO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Print_operationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, stack_in=None, ts=None, scope=None):
            super(ukeleleParser.Print_operationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.stack_in = None
            self.ts = None
            self.scope = None
            self.stack_out = None
            self.operation = None
            self.from_expr = None # ExprContext
            self.stack_in = stack_in
            self.ts = ts
            self.scope = scope

        def LPAREN(self):
            return self.getToken(ukeleleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ukeleleParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ukeleleParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(ukeleleParser.ExprContext,0)


        def PRINT(self):
            return self.getToken(ukeleleParser.PRINT, 0)

        def PRINTLN(self):
            return self.getToken(ukeleleParser.PRINTLN, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_print_operation

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterPrint_operation(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitPrint_operation(self)




    def print_operation(self, stack_in, ts, scope):

        localctx = ukeleleParser.Print_operationContext(self, self._ctx, self.state, stack_in, ts, scope)
        self.enterRule(localctx, 24, self.RULE_print_operation)

        localctx.operation = ""
        ln = False

        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            token = self._input.LA(1)
            if token in [ukeleleParser.PRINT]:
                self.state = 270
                self.match(ukeleleParser.PRINT)

            elif token in [ukeleleParser.PRINTLN]:
                self.state = 271
                self.match(ukeleleParser.PRINTLN)
                ln=True

            else:
                raise NoViableAltException(self)

            self.state = 275
            self.match(ukeleleParser.LPAREN)
            self.state = 276
            localctx.from_expr = self.expr(localctx.ts, localctx.scope)
            self.state = 277
            self.match(ukeleleParser.RPAREN)
            self.state = 278
            self.match(ukeleleParser.SEMICOLON)

            if ln:
                localctx.operation += localctx.from_expr.expr_out + "call void [mscorlib]System.Console::WriteLine( " + self.types[localctx.from_expr.type_out] + " )\n"
            else:
                localctx.operation += localctx.from_expr.expr_out + "call void [mscorlib]System.Console::Write( " + self.types[localctx.from_expr.type_out] + " )\n"
            localctx.stack_out = localctx.from_expr.stack_out

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ukeleleParser.ParametersContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.params = None

        def LPAREN(self):
            return self.getToken(ukeleleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ukeleleParser.RPAREN, 0)

        def argument_expression_list(self):
            return self.getTypedRuleContext(ukeleleParser.Argument_expression_listContext,0)


        def getRuleIndex(self):
            return ukeleleParser.RULE_parameters

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterParameters(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = ukeleleParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameters)

        localctx.params = ""

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ukeleleParser.LPAREN)
            localctx.params += "("
            self.state = 284
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ukeleleParser.VOID) | (1 << ukeleleParser.INT) | (1 << ukeleleParser.STRING))) != 0):
                self.state = 283
                self.argument_expression_list()


            self.state = 286
            self.match(ukeleleParser.RPAREN)
            localctx.params += ") "
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ukeleleParser.Argument_expression_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def definition(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.DefinitionContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.DefinitionContext,i)


        def getRuleIndex(self):
            return ukeleleParser.RULE_argument_expression_list

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterArgument_expression_list(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitArgument_expression_list(self)




    def argument_expression_list(self):

        localctx = ukeleleParser.Argument_expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argument_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.definition()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ukeleleParser.COMMA:
                self.state = 290
                self.match(ukeleleParser.COMMA)
                self.state = 291
                self.definition()
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ukeleleParser.DefinitionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(ukeleleParser.Type_specifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(ukeleleParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_definition

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterDefinition(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitDefinition(self)




    def definition(self):

        localctx = ukeleleParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.type_specifier()
            self.state = 298
            self.match(ukeleleParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, scope=None):
            super(ukeleleParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.scope = None
            self.stack_out = None
            self.expr_out = None
            self.type_out = None
            self.from_eand = None # EandContext
            self.ts = ts
            self.scope = scope

        def eand(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.EandContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.EandContext,i)


        def OR(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.OR)
            else:
                return self.getToken(ukeleleParser.OR, i)

        def getRuleIndex(self):
            return ukeleleParser.RULE_expr

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitExpr(self)




    def expr(self, ts, scope):

        localctx = ukeleleParser.ExprContext(self, self._ctx, self.state, ts, scope)
        self.enterRule(localctx, 32, self.RULE_expr)

        localctx.stack_out = 0
        localctx.expr_out = ''
        localctx.type_out = ''

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            localctx.from_eand = self.eand(ts, '', localctx.scope)

            localctx.stack_out = localctx.from_eand.stack_out
            localctx.expr_out = localctx.from_eand.expr_out
            localctx.type_out = localctx.from_eand.type_out

            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ukeleleParser.OR:
                self.state = 302
                self.match(ukeleleParser.OR)
                self.state = 303
                localctx.from_eand = self.eand(ts, localctx.type_out, localctx.scope)

                localctx.stack_out += localctx.from_eand.stack_out
                localctx.expr_out += localctx.from_eand.expr_out + 'or\n'
                localctx.type_out = localctx.from_eand.type_out

                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, type_in=None, scope=None):
            super(ukeleleParser.EandContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.type_in = None
            self.scope = None
            self.stack_out = None
            self.expr_out = None
            self.type_out = None
            self.from_erel = None # ErelContext
            self.ts = ts
            self.type_in = type_in
            self.scope = scope

        def erel(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.ErelContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.ErelContext,i)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.AND)
            else:
                return self.getToken(ukeleleParser.AND, i)

        def getRuleIndex(self):
            return ukeleleParser.RULE_eand

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterEand(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitEand(self)




    def eand(self, ts, type_in, scope):

        localctx = ukeleleParser.EandContext(self, self._ctx, self.state, ts, type_in, scope)
        self.enterRule(localctx, 34, self.RULE_eand)

        localctx.stack_out = 0
        localctx.expr_out = ''
        localctx.type_out = ''

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            localctx.from_erel = self.erel(ts, type_in, localctx.scope)

            localctx.stack_out = localctx.from_erel.stack_out
            localctx.expr_out = localctx.from_erel.expr_out
            localctx.type_out = localctx.from_erel.type_out

            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ukeleleParser.AND:
                self.state = 313
                self.match(ukeleleParser.AND)
                self.state = 314
                localctx.from_erel = self.erel(ts, localctx.type_out, localctx.scope)

                localctx.stack_out += localctx.from_erel.stack_out
                localctx.expr_out += localctx.from_erel.expr_out + 'and\n'
                localctx.type_out = localctx.from_erel.type_out

                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ErelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, type_in=None, scope=None):
            super(ukeleleParser.ErelContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.type_in = None
            self.scope = None
            self.stack_out = None
            self.expr_out = None
            self.type_out = None
            self.from_esum = None # EsumContext
            self._RELOP = None # Token
            self.ts = ts
            self.type_in = type_in
            self.scope = scope

        def esum(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.EsumContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.EsumContext,i)


        def RELOP(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.RELOP)
            else:
                return self.getToken(ukeleleParser.RELOP, i)

        def getRuleIndex(self):
            return ukeleleParser.RULE_erel

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterErel(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitErel(self)




    def erel(self, ts, type_in, scope):

        localctx = ukeleleParser.ErelContext(self, self._ctx, self.state, ts, type_in, scope)
        self.enterRule(localctx, 36, self.RULE_erel)

        localctx.stack_out = 0
        localctx.expr_out = ''
        localctx.type_out = ''

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            localctx.from_esum = self.esum(ts, type_in, localctx.scope)

            localctx.stack_out = localctx.from_esum.stack_out
            localctx.expr_out = localctx.from_esum.expr_out
            localctx.type_out = localctx.from_esum.type_out

            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ukeleleParser.RELOP:
                self.state = 324
                localctx._RELOP = self.match(ukeleleParser.RELOP)
                self.state = 325
                localctx.from_esum = self.esum(ts, localctx.type_out, localctx.scope)

                localctx.stack_out += localctx.from_esum.stack_out
                localctx.expr_out += localctx.from_esum.expr_out
                self.branches += 1

                if (None if localctx._RELOP is None else localctx._RELOP.text) == '==':
                    localctx.expr_out += 'beq L'

                elif (None if localctx._RELOP is None else localctx._RELOP.text) == '!=':
                    localctx.expr_out += 'bne.un L'

                elif (None if localctx._RELOP is None else localctx._RELOP.text) == '>':
                    localctx.expr_out += 'bgt L'

                elif (None if localctx._RELOP is None else localctx._RELOP.text) == '<':
                    localctx.expr_out += 'blt L'

                elif (None if localctx._RELOP is None else localctx._RELOP.text) == '>=':
                    localctx.expr_out += 'bge L'

                elif (None if localctx._RELOP is None else localctx._RELOP.text) == '<=':
                    localctx.expr_out += 'ble L'

                localctx.expr_out += str(self.branches) + '\n' + 'ldc.i4 0\n' + 'br L' + str(self.branches + 1) + '\n'
                localctx.expr_out += 'L' + str(self.branches) + ':\nldc.i4 1\nL' + str(self.branches + 1) + ':\n'
                self.branches += 1
                localctx.type_out = 'bool'


                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EsumContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, type_in=None, scope=None):
            super(ukeleleParser.EsumContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.type_in = None
            self.scope = None
            self.stack_out = None
            self.expr_out = None
            self.type_out = None
            self.from_term = None # TermContext
            self._ADDOP = None # Token
            self.from_another_term = None # TermContext
            self.ts = ts
            self.type_in = type_in
            self.scope = scope

        def term(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.TermContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.TermContext,i)


        def ADDOP(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.ADDOP)
            else:
                return self.getToken(ukeleleParser.ADDOP, i)

        def getRuleIndex(self):
            return ukeleleParser.RULE_esum

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterEsum(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitEsum(self)




    def esum(self, ts, type_in, scope):

        localctx = ukeleleParser.EsumContext(self, self._ctx, self.state, ts, type_in, scope)
        self.enterRule(localctx, 38, self.RULE_esum)

        localctx.stack_out = 0
        localctx.expr_out = ''
        localctx.type_out = ''

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            localctx.from_term = self.term(ts, type_in, localctx.scope)

            localctx.stack_out = localctx.from_term.stack_out
            localctx.expr_out = localctx.from_term.expr_out
            localctx.type_out = localctx.from_term.type_out

            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ukeleleParser.ADDOP:
                self.state = 335
                localctx._ADDOP = self.match(ukeleleParser.ADDOP)
                self.state = 336
                localctx.from_another_term = self.term(ts, localctx.type_out, localctx.scope)

                localctx.stack_out += localctx.from_another_term.stack_out
                localctx.expr_out += localctx.from_another_term.expr_out

                if (None if localctx._ADDOP is None else localctx._ADDOP.text) == '+':
                    localctx.expr_out += 'add' + '\n'
                else:
                    localctx.expr_out += 'sub' + '\n'
                localctx.type_out = localctx.from_another_term.type_out

                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, type_in=None, scope=None):
            super(ukeleleParser.TermContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.type_in = None
            self.scope = None
            self.stack_out = None
            self.expr_out = None
            self.type_out = None
            self.from_factor = None # FactorContext
            self._MULOP = None # Token
            self.from_another_factor = None # FactorContext
            self.ts = ts
            self.type_in = type_in
            self.scope = scope

        def factor(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.FactorContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.FactorContext,i)


        def MULOP(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.MULOP)
            else:
                return self.getToken(ukeleleParser.MULOP, i)

        def getRuleIndex(self):
            return ukeleleParser.RULE_term

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitTerm(self)




    def term(self, ts, type_in, scope):

        localctx = ukeleleParser.TermContext(self, self._ctx, self.state, ts, type_in, scope)
        self.enterRule(localctx, 40, self.RULE_term)

        localctx.stack_out = 0
        localctx.expr_out = ''
        localctx.type_out = ''

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            localctx.from_factor = self.factor(ts, type_in, localctx.scope)

            localctx.stack_out = localctx.from_factor.stack_out
            localctx.expr_out = localctx.from_factor.expr_out
            localctx.type_out = localctx.from_factor.type_out

            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ukeleleParser.MULOP:
                self.state = 346
                localctx._MULOP = self.match(ukeleleParser.MULOP)
                self.state = 347
                localctx.from_another_factor = self.factor(ts, localctx.type_out, localctx.scope)

                localctx.stack_out += localctx.from_another_factor.stack_out
                localctx.expr_out += ('conv.r8\n' if (None if localctx._MULOP is None else localctx._MULOP.text) == '/' else '') + localctx.from_another_factor.expr_out 

                if (None if localctx._MULOP is None else localctx._MULOP.text) == '*':
                    localctx.expr_out += 'mul' + '\n'
                    localctx.type_out = localctx.from_another_factor.type_out
                else:
                    if localctx.from_another_factor.type_out != 'float':
                        localctx.expr_out += 'conv.r8\n'
                    localctx.expr_out += 'div' + '\n'
                    localctx.type_out = 'float'

                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, type_in=None, scope=None):
            super(ukeleleParser.FactorContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.type_in = None
            self.scope = None
            self.stack_out = None
            self.expr_out = None
            self.type_out = None
            self.from_base = None # BaseContext
            self._ADDOP = None # Token
            self.from_factor = None # FactorContext
            self.ts = ts
            self.type_in = type_in
            self.scope = scope

        def base(self):
            return self.getTypedRuleContext(ukeleleParser.BaseContext,0)


        def NOT(self):
            return self.getToken(ukeleleParser.NOT, 0)

        def factor(self):
            return self.getTypedRuleContext(ukeleleParser.FactorContext,0)


        def LPAREN(self):
            return self.getToken(ukeleleParser.LPAREN, 0)

        def ADDOP(self):
            return self.getToken(ukeleleParser.ADDOP, 0)

        def RPAREN(self):
            return self.getToken(ukeleleParser.RPAREN, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_factor

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterFactor(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitFactor(self)




    def factor(self, ts, type_in, scope):

        localctx = ukeleleParser.FactorContext(self, self._ctx, self.state, ts, type_in, scope)
        self.enterRule(localctx, 42, self.RULE_factor)

        localctx.stack_out = 0
        localctx.expr_out = ''
        localctx.type_out = ''

        try:
            self.state = 366
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                localctx.from_base = self.base(ts, type_in, localctx.scope)

                localctx.stack_out = localctx.from_base.stack_out
                localctx.expr_out = localctx.from_base.expr_out
                localctx.type_out = localctx.from_base.type_out

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.match(ukeleleParser.NOT)
                self.state = 359
                self.factor(ts, type_in, localctx.scope)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.match(ukeleleParser.LPAREN)
                self.state = 361
                localctx._ADDOP = self.match(ukeleleParser.ADDOP)
                self.state = 362
                localctx.from_factor = self.factor(ts, type_in, localctx.scope)

                localctx.stack_out = localctx.from_factor.stack_out
                localctx.expr_out = localctx.from_factor.expr_out + 'neg\n' if (None if localctx._ADDOP is None else localctx._ADDOP.text) == '-' else ''
                localctx.type_out = localctx.from_factor.type_out

                self.state = 364
                self.match(ukeleleParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BaseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1, ts=None, type_in=None, scope=None):
            super(ukeleleParser.BaseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ts = None
            self.type_in = None
            self.scope = None
            self.stack_out = None
            self.expr_out = None
            self.type_out = None
            self._INTEGER = None # Token
            self._TEXT = None # Token
            self._REAL = None # Token
            self._BOOLEANO = None # Token
            self.from_expr = None # ExprContext
            self._IDENTIFIER = None # Token
            self.from_another_expr = None # ExprContext
            self._POSTADDOP = None # Token
            self.ts = ts
            self.type_in = type_in
            self.scope = scope

        def INTEGER(self):
            return self.getToken(ukeleleParser.INTEGER, 0)

        def TEXT(self):
            return self.getToken(ukeleleParser.TEXT, 0)

        def REAL(self):
            return self.getToken(ukeleleParser.REAL, 0)

        def BOOLEANO(self):
            return self.getToken(ukeleleParser.BOOLEANO, 0)

        def LPAREN(self):
            return self.getToken(ukeleleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ukeleleParser.RPAREN, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ukeleleParser.ExprContext)
            else:
                return self.getTypedRuleContext(ukeleleParser.ExprContext,i)


        def IDENTIFIER(self):
            return self.getToken(ukeleleParser.IDENTIFIER, 0)

        def LCOR(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.LCOR)
            else:
                return self.getToken(ukeleleParser.LCOR, i)

        def RCOR(self, i=None):
            if i is None:
                return self.getTokens(ukeleleParser.RCOR)
            else:
                return self.getToken(ukeleleParser.RCOR, i)

        def POSTADDOP(self):
            return self.getToken(ukeleleParser.POSTADDOP, 0)

        def getRuleIndex(self):
            return ukeleleParser.RULE_base

        def enterRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.enterBase(self)

        def exitRule(self, listener):
            if isinstance( listener, ukeleleListener ):
                listener.exitBase(self)




    def base(self, ts, type_in, scope):

        localctx = ukeleleParser.BaseContext(self, self._ctx, self.state, ts, type_in, scope)
        self.enterRule(localctx, 44, self.RULE_base)

        localctx.stack_out = 0
        localctx.expr_out = ''
        localctx.type_out = ''

        self._la = 0 # Token type
        try:
            self.state = 406
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                localctx._INTEGER = self.match(ukeleleParser.INTEGER)

                localctx.stack_out = 1
                localctx.expr_out = 'ldc.i4 ' + (None if localctx._INTEGER is None else localctx._INTEGER.text) + '\n'
                localctx.type_out = 'int'
                if localctx.type_in == 'float':
                    localctx.expr_out += 'conv.r8\n'
                    localctx.type_out = 'float'

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                localctx._TEXT = self.match(ukeleleParser.TEXT)

                localctx.stack_out = 1
                localctx.expr_out = 'ldstr ' + (None if localctx._TEXT is None else localctx._TEXT.text) + '\n'
                localctx.type_out = 'string'

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                localctx._REAL = self.match(ukeleleParser.REAL)

                localctx.stack_out = 1
                localctx.expr_out = 'ldc.r4 ' + (None if localctx._REAL is None else localctx._REAL.text) + '\n'
                localctx.type_out = 'float'

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 374
                localctx._BOOLEANO = self.match(ukeleleParser.BOOLEANO)

                localctx.stack_out = 1
                localctx.expr_out = 'ldc.i4 1\n' if (None if localctx._BOOLEANO is None else localctx._BOOLEANO.text) == 'True' else 'ldc.i4 0\n'
                localctx.type_out = 'bool'

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 376
                self.match(ukeleleParser.LPAREN)
                self.state = 377
                localctx.from_expr = self.expr(ts, localctx.scope)

                localctx.stack_out = localctx.from_expr.stack_out
                localctx.expr_out = localctx.from_expr.expr_out
                localctx.type_out = localctx.from_expr.type_out

                self.state = 379
                self.match(ukeleleParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 381
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)

                element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                if not element:
                    error_message('"' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '" not defined', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))
                else:
                    #if element.scope == Scope.LOOP and scope != Scope.LOOP:
                    #    error_message('"' + (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) + '" not defined in this scope', (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))
                    #else:
                    localctx.expr_out = 'ldloc ' + str(element.index) + '\n'
                    localctx.stack_out = 1
                    localctx.type_out = element.stype

                    if localctx.type_in == 'float':
                        if localctx.type_out == 'int':
                            localctx.expr_out += 'conv.r8\n'
                            localctx.type_out = 'float'

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 383
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 384
                self.match(ukeleleParser.LCOR)
                self.state = 385
                localctx.from_expr = self.expr(ts, localctx.scope)
                self.state = 386
                self.match(ukeleleParser.RCOR)

                array = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))
                if array:
                    localctx.expr_out += 'ldloc ' + str(array.index) + '\n' + localctx.from_expr.expr_out
                    localctx.stack_out += localctx.from_expr.stack_out + 1

                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ukeleleParser.LCOR:
                    self.state = 388
                    self.match(ukeleleParser.LCOR)
                    self.state = 389
                    localctx.from_another_expr = self.expr(ts, localctx.scope)
                    self.state = 390
                    self.match(ukeleleParser.RCOR)

                    if array:
                        localctx.expr_out += localctx.from_another_expr.expr_out + 'mul\n'
                        localctx.stack_out += localctx.from_another_expr.stack_out

                    self.state = 397
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)


                array = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))
                if array:
                    array_type = array.stype.split('[')[0]
                    if array_type == 'int':
                        localctx.expr_out += 'ldelem.i4' + '\n'
                        localctx.stack_out +=  1
                        localctx.type_out = 'int'

                    elif array_type == 'float':
                        localctx.expr_out += 'ldelem.r4' + '\n'
                        localctx.stack_out +=  1
                        localctx.type_out = 'float'

                    elif array_type == 'bool':
                        localctx.expr_out += 'ldelem.i4' + '\n'
                        localctx.stack_out +=  1
                        localctx.type_out = 'bool'

                    elif array_type == 'string':
                        localctx.expr_out += 'ldelem' + '\n'
                        localctx.stack_out +=  1
                        localctx.type_out = 'string'

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 400
                localctx._POSTADDOP = self.match(ukeleleParser.POSTADDOP)
                self.state = 401
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                 
                element = localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))
                if element:
                    localctx.expr_out += 'ldloc ' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'

                    if localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).stype  == 'int':
                        localctx.expr_out += 'ldc.i4 1\nadd\n' if (None if localctx._POSTADDOP is None else localctx._POSTADDOP.text) == '++' else 'ldc.i4 1\nsub\n'
                    elif localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).stype  == 'float':
                        localctx.expr_out += 'ldc.r4 1\nadd\n' if (None if localctx._POSTADDOP is None else localctx._POSTADDOP.text) == '++' else 'ldc.r4 1\nsub\n'

                    localctx.expr_out += 'stloc.' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                    localctx.expr_out += 'ldloc ' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                    localctx.stack_out += 3
                    localctx.type_out = 'int'
                else:
                    not_defined_message((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), (0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line))

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 403
                localctx._IDENTIFIER = self.match(ukeleleParser.IDENTIFIER)
                self.state = 404
                localctx._POSTADDOP = self.match(ukeleleParser.POSTADDOP)

                localctx.expr_out += 'ldloc ' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                localctx.expr_out += 'ldloc ' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'

                if localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).stype  == 'int':
                    localctx.expr_out += 'ldc.i4 1\nadd\n' if (None if localctx._POSTADDOP is None else localctx._POSTADDOP.text) == '++' else 'ldc.i4 1\nsub\n'
                elif localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).stype  == 'float':
                    localctx.expr_out += 'ldc.r4 1\nadd\n' if (None if localctx._POSTADDOP is None else localctx._POSTADDOP.text) == '++' else 'ldc.r4 1\nsub\n'

                localctx.expr_out += 'stloc.' + str(localctx.ts.get((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)).index) + '\n'
                localctx.stack_out += 3
                localctx.type_out = 'int'

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




