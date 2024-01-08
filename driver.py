import sys
from antlr4 import *
from skeliaLexer import skeliaLexer
from skeliaParser import skeliaParser


class TreePrintListener(ParseTreeListener):
    def enterEveryRule(self, ctx):
        node_type: str = type(ctx).__name__
        node_type = node_type[0:node_type.find('Context')]
        node_text = ''
        if node_type not in ('Program', 'StatementList', 'Statement'):
            node_text = ctx.getText()
        print(f"{node_type}: {node_text}")


def main(argv):
    if len(argv) > 1:
        input_stream = FileStream(argv[1])
    else:
        input_stream = FileStream('program.skelia')
    lexer = skeliaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = skeliaParser(stream)
    tree = parser.program()
    listener = TreePrintListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    main(sys.argv)
