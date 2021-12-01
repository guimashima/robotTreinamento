***Variables***
${text}     teste
${number}   ${10}
${number20}   ${20}

***Keywords***
rodando keywords de run keyword if

    Run Keyword If      '${text}' == 'teste'     Log     valor em string de variavel e texto retornou true
    Run Keyword If      ${number < 20}          Log     valor em numero de variavel e numero retornou true
    Run Keyword If      ${number < ${20}}          Log     valor em numero de variavel e numero entre chaves retornou true
    Run Keyword If      ${number < ${number20}}          Log     valor em numero de variavel e outro valor de variavel com numero retornou true
    #Run Keyword If      ${number < number20}          Log     valor em numero de variavel e outro valor de variavel com numero retornou true
    #Run Keyword If      Should Be Equal        ${text}     teste          Log     valor em numero de variavel e outro valor de variavel com numero retornou true
    Run Keyword If      '${text}' == 'teste'     
    ...                 Log     log primeira linha
    #...                 Log     log segunda linha

rodando keywords de run keyword unless
    Run Keyword Unless      not('${text}' == 'teste')     Log     valor em string de variavel e texto retornou true
    Run Keyword Unless      not(${number < 20})          Log     valor em numero de variavel e numero retornou true
    Run Keyword Unless      not(${number < ${20}})          Log     valor em numero de variavel e numero entre chaves retornou true
    Run Keyword Unless      not(${number < ${number20}})          Log     valor em numero de variavel e outro valor de variavel com numero retornou true
    #Run Keyword Unless     not(${number < number20})          Log     valor em numero de variavel e outro valor de variavel com numero retornou true
    #Run Keyword Unless     not(Should Be Equal        ${text}     teste)          Log     valor em numero de variavel e outro valor de variavel com numero retornou true
    Run Keyword Unless      not('${text}' == 'teste')
    ...                 Log     log primeira linha
    #...                 Log     log segunda linha

rodando keywords de run keyword and return status
    ${status1}       Run Keyword And Return Status       Convert To Title Case       ${text}
    ${status2}       Run Keyword And Return Status      Get Text     ${text}
    #${status}       Run Keyword And Return Status      Click Element
    Run Keyword If      ${status1}       Log         realiza acao dependendo do status
    Run Keyword Unless  ${status2}       Log         realiza acao dependendo do status

rodando keywords de evaluate
    ${var}      Evaluate        '${number}' + '${number20}'        #string
    #${var}      Evaluate        ${number} + '${number20}'        #error
    ${var}      Evaluate        ${number} + ${number20}        #number
    ${var}      Evaluate        ${number} * ${number20}        #number
    ${var}      Evaluate        ${number} / ${number20}        #number
    ${var}      Evaluate        ${number} == ${number20}        #boolean
    ${var}      Evaluate        ${number} <= ${number20}        #boolean
    ${path}=    Evaluate    os.environ.get("PATH")

rodando keywords de catenate
    ${var}      Catenate        SEPARATOR=|     ${text}     teste2
    ${var}      Catenate        SEPARATOR=|     
    ...         ${text}     
    ...         teste2
    ${var}      Catenate        SEPARATOR=|     ${number}     teste2

rodando keywords de set variable if
    ${var}        Set Variable If     ${number} <= ${number20}        se der true vai setar esse      se der false vai setar esse
    ${var}        Set Variable If     not(${number} <= ${number20})        se der true vai setar esse      se der false vai setar esse
    ${var} =  Set Variable If
    ...  "${var}"=="None"  value1
    ...  "${var}"=="True"  value2
    ...  "${var}"=="False"  value3
    ...  Final else!
