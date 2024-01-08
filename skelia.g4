grammar skelia;

program      : statementList EOF;

INTNUM       : UnsignedInt;
DOUBLENUM    : UnsignedDouble;
UnsignedInt  : '0' | (NonzeroDigit ('0' | NonzeroDigit)*);
UnsignedDouble: ('.' ('0' | NonzeroDigit)+ | UnsignedInt '.' ('0' | NonzeroDigit)*) ('E' INTNUM)?;
BOOLCONST    : 'true' | 'false';
TYPE         : 'Int' | 'Double' | 'Boolean';
IDENT        : Letter (Letter | '0' | NonzeroDigit)*;

COMMENT      : '//' ~[\r\n]* -> skip;
Letter       : [a-zA-Z];
NonzeroDigit : [1-9];
WhiteSpace   : [ \t]+ -> skip;
EndOfLine    : '\r'? '\n' -> skip;
ADDOP        : '+' | '-';
MULTOP       : '*' | '/';
POWEROP      : '^';
RELOP        : '==' | '<=' | '<' | '>' | '>=' | '!=';
BracketsOp   : '(' | ')' | '{' | '}';
AssignOp     : '=';
Punct        : '.' | ',' | ':' | ';';

SpecSign     : '.' | ',' | ':' | ';' | '(' | ')' | '{' | '}' | '+' | '-' | '*' | '/' | '!';

expression   : arithmExpression | boolExpr;
boolExpr
        : (arithmExpression RELOP arithmExpression | BOOLCONST | BOOLCONST RELOP BOOLCONST) (('&&' | '||') boolExpr)* |
        '(' boolExpr ')';

init         : ('var' | 'val') IDENT (':' TYPE)? '=' expression;

statementList: statement+;
statement    : init ';' | assign ';' | inp ';' | out ';' | ifStatement | forStatement;
assign       : IDENT '=' expression;
ifStatement  : 'if' condition doSection ( 'elif' condition doSection )* ( 'else' doSection )?;
condition    : '(' boolExpr ')' ;

forStatement : 'for' '(' rangeExpression ( 'if' condition (';' 'if' condition)* )? ')' doSection;
rangeExpression: IDENT '<-' arithmExpression1 ('to' | 'until') arithmExpression2 ('by' arithmExpression3)?;
arithmExpression1: arithmExpression;
arithmExpression2: arithmExpression;
arithmExpression3: arithmExpression;

doSection    : '{' statementList '}';
inp          : ('val' | 'var')? IDENT (':' TYPE)? '=' 'readline' '()';
out          : 'println' '(' expression ')';

arithmExpression: term (('+' | '-') term)*;
term          : chunk (MULTOP chunk)*;
chunk         : factor (POWEROP factor)*;
factor       : '-'? IDENT | '-'? INTNUM | '-'? DOUBLENUM | '-'? '(' arithmExpression ')';