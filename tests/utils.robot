***Settings***
Resource    ../keywords/utils2.robot

***Test Cases***

keywords
    [tags]      done
    chamando variavelpy
    keyword com argumento obrigatorio       teste
    #keyword com argumento obrigatorio
    keyword com argumento opcional
    keyword com argumento opcional          mandando argumento
    keyword com muitos argumentos            teste1      teste2      teste3
    keyword com um ou mais argumentos       primeiro argumento      demais argumento1       demais argumento2       demais argumento3
    logando retorno de keyword

condicionais
    [Tags]      aoba
    condicional if elseif else
    condicional for loop numa lista
    condicional for loop numa dict
    condicional for loop in range
    condicional for loop in range com comeco fim
    condicional for loop in range com comeco fim step
    condicional com muitos for loop
    condicional for loop com exit
    condicional for loop com continue
    acessar variaveis de diferentes formas