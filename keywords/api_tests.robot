
***Variables***
${httpbin_host}    https://httpbin.org

***Keywords***
#https://marketsquare.github.io/robotframework-requests/doc/RequestsLibrary.html
#https://httpbin.org/

Requisitando um GET na rota "${scenario_rota}" do httpbin
    Create Session       httpbin_host      ${httpbin_host}    headers=${headers}
    ${response}          GET On Session    httpbin_host       ${scenario_rota}      params=${parameters}
    Set Test Variable    ${response}

Requisitando um POST na rota "${scenario_rota}" do httpbin
    ${body}              Criando body de usuario e senha e retornando o json
    Create Session       httpbin_host       ${httpbin_host}    headers=${headers}
    ${response}          POST On Session    httpbin_host       ${scenario_rota}      params=${parameters}    data=${body}
    Set Test Variable    ${response}

Requisitando um PUT na rota "${scenario_rota}" do httpbin
    ${body}              Criando body de usuario e senha e retornando o json
    Create Session       httpbin_host      ${httpbin_host}    headers=${headers}
    ${response}          PUT On Session    httpbin_host       ${scenario_rota}      params=${parameters}    data=${body}
    Set Test Variable    ${response}

Requisitando um DELETE na rota "${scenario_rota}" do httpbin
    Create Session       httpbin_host         ${httpbin_host}    headers=${headers}
    ${response}          DELETE On Session    httpbin_host       ${scenario_rota}      params=${parameters}
    Set Test Variable    ${response}

StatusCode deve ser "${scenario_statusCode}"
    Status Should Be    ${scenario_statusCode}    ${response}

Criando body de usuario e senha e retornando o json
    ${body}      Create Dictionary
    Set To Dictionary    ${body}             usuario=acc01275
    Set To Dictionary    ${body}             senha=123456
    [Return]        ${body}