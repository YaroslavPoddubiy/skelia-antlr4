import sys
from antlr4 import *
from skeliaLexer import skeliaLexer
from skeliaParser import skeliaParser
from skeliaListener import skeliaListener

postfixCode = {'.target': 'Postfix Machine', '.version': 0.2, '.vars': [], '.labels': [], '.constants': [], '.code': []}


def failParse(str, tuple):
    if str == 'неочікуваний кінець програми':
        (lexeme, token, numRow) = tuple
        raise SyntaxError(
            'Parser ERROR: \n\t Неочікуваний кінець програми - в таблиці символів (розбору) немає запису з номером {1}. \n\t Очікувалось - {0}'.format(
                (lexeme, token), numRow))
    # if str == 'getSymb(): неочікуваний кінець програми':
    #     numRow = tuple
    #     raise SyntaxError(
    #         'Parser ERROR: \n\t Неочікуваний кінець програми - в таблиці символів (розбору) немає запису з номером {0}. \n\t Останній запис - {1}'.format(
    #             numRow, tableOfSymb[numRow - 1]))
    elif str == 'невідповідність токенів':
        (numLine, lexeme, token, lex, tok) = tuple
        raise SyntaxError(
            'Parser ERROR: \n\t В рядку {0} неочікуваний елемент ({1},{2}). \n\t Очікувався - ({3},{4}).'.format(
                numLine, lexeme, token, lex, tok))
    elif str == 'невідповідність інструкцій':
        (numLine, lex, tok, expected) = tuple
        raise SyntaxError(
            'Parser ERROR: \n\t В рядку {0} неочікуваний елемент ({1},{2}). \n\t Очікувався - {3}.'.format(numLine, lex,
                                                                                                           tok,
                                                                                                           expected))
    elif str == 'невідповідність у Expression.Factor':
        (numLine, lex, tok, expected) = tuple
        raise SyntaxError(
            'Parser ERROR: \n\t В рядку {0} неочікуваний елемент ({1},{2}). \n\t Очікувався - {3}.'.format(numLine, lex,
                                                                                                           tok,
                                                                                                           expected))

    elif str == 'повторне оголошення змінної':
        numLine, var = tuple
        raise SyntaxError('Parser ERROR: \n\t В рядку {0} повторне оголошення змінної {1}.'.format(numLine, var))

    elif str == 'використання неоголошеної змінної':
        numLine, var = tuple
        raise SyntaxError('Parser ERROR: \n\t В рядку {0} використана неоголошена змінна {1}.'.format(numLine, var))

    elif str == 'перевизначення константної змінної':
        numLine, var = tuple
        raise SyntaxError('Parser ERROR: \n\t В рядку {0} перевизначення константної змінної {1}.'.format(numLine, var))

    elif str == 'невідповідність типів':
        numLine, value_type, expected_type = tuple
        raise SyntaxError(
            'Parser ERROR: \n\t В рядку {0} неочікуваний тип значення {1}. \n\t Очікувався {2}.'.format(numLine,
                                                                                                              value_type,
                                                                                                              expected_type)
        )


def serv():
    code = postfixCode
    text = ""
    for key in code:
        if isinstance(code[key], list | tuple):
            text += '\n' + key + '(\n'
            if code[key]:
                for item in code[key]:
                    text += f'\t{item[0]} {" " *  (20 - len(item[0]))} {item[1]}\n'
            text += ')\n'
        else:
            text += f'{key}: {code[key]}\n'
    return text


def savePostfixCode(fileName: str):
    fileName = fileName.split('/')[-1] + '.postfix'
    with open(fileName, 'w') as file:
        file.write(serv())
        print('------------')


def postfixCodeGen(case, toTran):
    if case == 'lval':
        lex, tok = toTran
        postfixCode['.code'].append((lex, 'l-val'))
    elif case == 'rval':
        lex, tok = toTran
        postfixCode['.code'].append((lex, 'r-val'))
    else:
        lex, tok = toTran
        postfixCode['.code'].append((lex, tok))


class Listener(skeliaListener):
    __variables = {}
    __local_variables = {}
# Enter a parse tree produced by skeliaParser#program.

    @staticmethod
    def __get_tokens(ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]
        start = ctx.start.tokenIndex
        stop = ctx.stop.tokenIndex
        tokens = ctx.parser._input
        tokens = tokens.tokens[start:stop + 1]
        return tokens

    @staticmethod
    def __get_expr_type(value):
        if isinstance(value, int):
            return 'intnum'
        elif isinstance(value, float):
            return 'doublenum'
        elif isinstance(value, bool):
            return 'boolval'
        elif isinstance(value, str):
            if value.isdecimal():
                return 'intnum'
            elif value == 'true' or value == 'false':
                return 'boolval'
            else:
                try:
                    float(value)
                    return 'doublenum'
                except ValueError:
                    pass

    def enterProgram(self, ctx:skeliaParser.ProgramContext):
        pass

    # Exit a parse tree produced by skeliaParser#program.
    def exitProgram(self, ctx:skeliaParser.ProgramContext):
        pass


    # Enter a parse tree produced by skeliaParser#expression.
    def enterExpression(self, ctx:skeliaParser.ExpressionContext):
        tokens = self.__get_tokens(ctx)
        expression = ''
        for token in tokens:
            value = ''
            if token.type == 30:
                value = str(self.__variables[token.text])
            elif token.type == 28:
                if token.text == 'true':
                    value = 'True'
                else:
                    value = 'False'
            elif token.type == 37:
                value = '**'
            elif token.text == '&&':
                value = 'and'
            elif token.text == '||':
                value = 'or'
            else:
                value = token.text
            expression += value
        return eval(expression)

    # Exit a parse tree produced by skeliaParser#expression.
    def exitExpression(self, ctx:skeliaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by skeliaParser#boolExpr.
    def enterBoolExpr(self, ctx:skeliaParser.BoolExprContext):
        pass

    # Exit a parse tree produced by skeliaParser#boolExpr.
    def exitBoolExpr(self, ctx: skeliaParser.BoolExprContext):
        pass


    # Enter a parse tree produced by skeliaParser#init.
    def enterInit(self, ctx: skeliaParser.InitContext):
        var_name = str(ctx.IDENT())
        tokens = self.__get_tokens(ctx)
        mutable = tokens[0].text
        if var_name in self.__variables:
            raise SyntaxError(f"У рядку {ctx.start.line} повторне оголошення змінної {var_name}")
        var_type = ctx.TYPE()
        print(f'VAR_TYPE = {var_type}')
        var_value = self.enterExpression(ctx.expression())
        expr_type = self.__get_expr_type(var_value)
        if var_type:
            var_type = str(var_type)
            if var_type == 'Int':
                var_type = 'intnum'
            elif var_type == 'Double':
                var_type = 'doublenum'
            else:
                var_type = 'boolval'
            if var_type != expr_type:
                raise SyntaxError(f"У рядку {ctx.start.line} неочікуваний тип {expr_type}. Очікувався {var_type}.")
        else:
            var_type = expr_type
        self.__variables[str(var_name)] = (mutable, var_type, var_value)

    # Exit a parse tree produced by skeliaParser#init.
    def exitInit(self, ctx: skeliaParser.InitContext):
        pass


    # Enter a parse tree produced by skeliaParser#statementList.
    def enterStatementList(self, ctx:skeliaParser.StatementListContext):
        pass

    # Exit a parse tree produced by skeliaParser#statementList.
    def exitStatementList(self, ctx:skeliaParser.StatementListContext):
        pass


    # Enter a parse tree produced by skeliaParser#statement.
    def enterStatement(self, ctx:skeliaParser.StatementContext):
        pass

    # Exit a parse tree produced by skeliaParser#statement.
    def exitStatement(self, ctx:skeliaParser.StatementContext):
        pass


    # Enter a parse tree produced by skeliaParser#assign.
    def enterAssign(self, ctx:skeliaParser.AssignContext):
        var_name = str(ctx.IDENT())
        if var_name not in self.__variables:
            raise SyntaxError(f"У рядку {ctx.start.line} використання неоголошеної змінної {var_name}")
        if self.__variables[var_name][0] == 'val':
            raise SyntaxError(f"У рядку {ctx.start.line} переприсвоєння значення константній змінній {var_name}.")
        expr_value = self.enterExpression(ctx.expression())
        expr_type = self.__get_expr_type(expr_value)
        if self.__variables[var_name][1] != expr_type:
            raise SyntaxError(f"У рядку {ctx.start.line} неочікуваний тип {expr_type}. Очікувався {self.__variables[var_name][1]}.")
        self.__variables[str(var_name)][2] = expr_value

    # Exit a parse tree produced by skeliaParser#assign.
    def exitAssign(self, ctx:skeliaParser.AssignContext):
        pass


    # Enter a parse tree produced by skeliaParser#ifStatement.
    def enterIfStatement(self, ctx:skeliaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by skeliaParser#ifStatement.
    def exitIfStatement(self, ctx:skeliaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by skeliaParser#condition.
    def enterCondition(self, ctx:skeliaParser.ConditionContext):
        pass

    # Exit a parse tree produced by skeliaParser#condition.
    def exitCondition(self, ctx:skeliaParser.ConditionContext):
        pass


    # Enter a parse tree produced by skeliaParser#forStatement.
    def enterForStatement(self, ctx:skeliaParser.ForStatementContext):
        pass

    # Exit a parse tree produced by skeliaParser#forStatement.
    def exitForStatement(self, ctx:skeliaParser.ForStatementContext):
        pass


    # Enter a parse tree produced by skeliaParser#rangeExpression.
    def enterRangeExpression(self, ctx:skeliaParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by skeliaParser#rangeExpression.
    def exitRangeExpression(self, ctx:skeliaParser.RangeExpressionContext):
        pass


    # Enter a parse tree produced by skeliaParser#arithmExpression1.
    def enterArithmExpression1(self, ctx:skeliaParser.ArithmExpression1Context):
        pass

    # Exit a parse tree produced by skeliaParser#arithmExpression1.
    def exitArithmExpression1(self, ctx:skeliaParser.ArithmExpression1Context):
        pass


    # Enter a parse tree produced by skeliaParser#arithmExpression2.
    def enterArithmExpression2(self, ctx:skeliaParser.ArithmExpression2Context):
        pass

    # Exit a parse tree produced by skeliaParser#arithmExpression2.
    def exitArithmExpression2(self, ctx:skeliaParser.ArithmExpression2Context):
        pass


    # Enter a parse tree produced by skeliaParser#arithmExpression3.
    def enterArithmExpression3(self, ctx:skeliaParser.ArithmExpression3Context):
        pass

    # Exit a parse tree produced by skeliaParser#arithmExpression3.
    def exitArithmExpression3(self, ctx:skeliaParser.ArithmExpression3Context):
        pass


    # Enter a parse tree produced by skeliaParser#doSection.
    def enterDoSection(self, ctx:skeliaParser.DoSectionContext):
        pass

    # Exit a parse tree produced by skeliaParser#doSection.
    def exitDoSection(self, ctx:skeliaParser.DoSectionContext):
        pass


    # Enter a parse tree produced by skeliaParser#inp.
    def enterInp(self, ctx:skeliaParser.InpContext):
        pass

    # Exit a parse tree produced by skeliaParser#inp.
    def exitInp(self, ctx:skeliaParser.InpContext):
        pass


    # Enter a parse tree produced by skeliaParser#out.
    def enterOut(self, ctx:skeliaParser.OutContext):
        print(self.enterExpression(ctx.expression()))

    # Exit a parse tree produced by skeliaParser#out.
    def exitOut(self, ctx:skeliaParser.OutContext):
        pass


    # Enter a parse tree produced by skeliaParser#arithmExpression.
    def enterArithmExpression(self, ctx:skeliaParser.ArithmExpressionContext):
        pass

    # Exit a parse tree produced by skeliaParser#arithmExpression.
    def exitArithmExpression(self, ctx:skeliaParser.ArithmExpressionContext):
        pass


    # Enter a parse tree produced by skeliaParser#term.
    def enterTerm(self, ctx:skeliaParser.TermContext):
        pass

    # Exit a parse tree produced by skeliaParser#term.
    def exitTerm(self, ctx:skeliaParser.TermContext):
        pass


    # Enter a parse tree produced by skeliaParser#chunk.
    def enterChunk(self, ctx:skeliaParser.ChunkContext):
        pass

    # Exit a parse tree produced by skeliaParser#chunk.
    def exitChunk(self, ctx:skeliaParser.ChunkContext):
        pass


    # Enter a parse tree produced by skeliaParser#factor.
    def enterFactor(self, ctx:skeliaParser.FactorContext):
        pass

    # Exit a parse tree produced by skeliaParser#factor.
    def exitFactor(self, ctx:skeliaParser.FactorContext):
        pass


def main(argv):
    # input_stream = FileStream(argv[1])
    input_stream = FileStream('test_program.skelia')
    lexer = skeliaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = skeliaParser(stream)
    # parser.getTokenStream()
    tree = parser.program()
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    # savePostfixCode(argv[1].split('.')[0])


if __name__ == '__main__':
    main(sys.argv)
