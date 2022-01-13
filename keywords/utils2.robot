***Settings***
Variables       ../resources/variables.py

***Variables***
@{listaVariable}        um      dois        tres

***Keywords***
chamando variavelpy
    Log     ${VARIAVEL_PY_STRING}
    Log     ${VARIAVEL_PY_INT}
    Log     ${int_com_conta}
    Log     ${numero}

Given that user is in publisher "${usuario}" "${senha}"
    ${token}        logar       ${usuario}      ${senha}
    Set token em algum lugar

logar
    [Arguments]     ${usuario}      ${senha}
    kajshfasdlaksdkajshd
    [Return]        token


keyword com argumento obrigatorio
    [Arguments]     ${arg1}
    Log             argumento obrigatorio: ${arg1}

keyword com argumento opcional
    [Arguments]     ${arg1}=argumento default
    Log             argumento opcional: ${arg1}

keyword com muitos argumentos
    [Arguments]     @{args}
    Log             todos argumentos enviados: @{args}

keyword com um ou mais argumentos
    [Arguments]     ${arg1}        @{args}
    Log             primeiro argumento enviado: ${arg1}
    Log             todos argumentos enviados depois do primeiro @{args}

logando retorno de keyword
    ${var}      pegando retorno de keyword
    Log         ${var}

pegando retorno de keyword
    Log             faço oq tiver a fazer e depois retorno um valor
    [Return]        retorno

condicional if elseif else
    ${var}      Set Variable        10
    IF    ${var} > 1
        Log    Greater than one.
    ELSE IF    "${var}" == "dog"
        Log    It's a dog!
    ELSE
        Log    Probably a cat. 🤔
    END

condicional for loop numa lista
    @{lista}        Create List     um      dois        tres
    Log    ${lista}
    FOR    ${item}    IN    @{lista}
        Log    ${item}
    END
    FOR    ${item}    IN    um      dois        tres
        Log    ${item}
    END

condicional for loop numa dict
    &{dict}     Create Dictionary       key1=value1     key2=value2     key3=value3       key4=@{listaVariable}      #key4=['um', 'dois', 'tres']
    FOR    ${key_value_tuple}    IN    &{dict}
        Log    ${key_value_tuple}
    END

    FOR    ${key}    IN    @{dict}
        Log    ${key}=${dict}[${key}]
        IF      '${key}' == 'key4'
            FOR     ${item}     IN      @{dict['key4']}
                Log     ${item}
            END
        END
    END

condicional for loop in range
    FOR    ${index}    IN RANGE    10
        Log    ${index}
    END

condicional for loop in range com comeco fim
    FOR    ${index}    IN RANGE    1    10
        Log    ${index}
    END

condicional for loop in range com comeco fim step
    FOR    ${index}    IN RANGE    0    10    2
        Log    ${index}
    END

condicional com muitos for loop
    @{alfabeto}=    Create List    a    b    c
    @{numeros}=    Create List    ${1}    ${2}    ${3}
    FOR    ${alfabeto}    IN    @{alfabeto}
        FOR    ${nuemro}    IN    @{numeros}
            Log    ${alfabeto}${nuemro}
        END
    END

condicional for loop com exit
    FOR    ${i}    IN RANGE    5
        Exit For Loop If    ${i} == 2
        Log    ${i}
    END

condicional for loop com continue
    FOR    ${i}    IN RANGE    3
        Continue For Loop If    ${i} == 1
        Log    ${i}
    END

acessar variaveis de diferentes formas
    ${string}=    Set Variable    Hello world!
    Log    ${string}[0]    # H
    Log    ${string}[:5]    # Hello
    Log    ${string}[6:]    # world!
    Log    ${string}[-1]    # !
    @{list}=    Create List    one    two    three    four    five
    Log    ${list}    # ['one', 'two', 'three', 'four', 'five']
    Log    ${list}[0:6:2]    # ['one', 'three', 'five']