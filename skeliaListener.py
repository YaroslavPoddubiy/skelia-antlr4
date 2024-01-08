# Generated from skelia.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .skeliaParser import skeliaParser
else:
    from skeliaParser import skeliaParser

# This class defines a complete listener for a parse tree produced by skeliaParser.
class skeliaListener(ParseTreeListener):

    # Enter a parse tree produced by skeliaParser#program.
    def enterProgram(self, ctx:skeliaParser.ProgramContext):
        pass

    # Exit a parse tree produced by skeliaParser#program.
    def exitProgram(self, ctx:skeliaParser.ProgramContext):
        pass


    # Enter a parse tree produced by skeliaParser#expression.
    def enterExpression(self, ctx:skeliaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by skeliaParser#expression.
    def exitExpression(self, ctx:skeliaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by skeliaParser#boolExpr.
    def enterBoolExpr(self, ctx:skeliaParser.BoolExprContext):
        pass

    # Exit a parse tree produced by skeliaParser#boolExpr.
    def exitBoolExpr(self, ctx:skeliaParser.BoolExprContext):
        pass


    # Enter a parse tree produced by skeliaParser#init.
    def enterInit(self, ctx:skeliaParser.InitContext):
        pass

    # Exit a parse tree produced by skeliaParser#init.
    def exitInit(self, ctx:skeliaParser.InitContext):
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
        pass

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
        pass

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



del skeliaParser