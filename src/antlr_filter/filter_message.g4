grammar filter_message
     ;
prog : stat                         # Program
     ;
stat : expr                         # Expression
     | '1'                          # All
     ;
expr : expr ' and ' expr            # And
     | expr ' or ' expr             # Or
     | val ' \u003D ' val           # Equality
     ;
val  : lit                          # ValID
     | rpl                          # ValReplace
     ;
lit  : '\u0027'STR'\u0027'          # Literal
     ;
rpl  : '\u007B'STR'\u007D'          # Replace
     ;
STR  : [a-zA-Z0-9 !@#$%^&\.]+
     ;
WS   : [\t\r\n]+ -> skip
     ;
