***Settings***
Resource    ../resources/helpers.robot
Test Setup  Criando Headers e Parameters

***Test Cases***
#Envia informação ao serviço. EX: Cadastro de usuario num site. Envia todos os dados da pessoa ao banco de dados
POST on a service
    [tags]      apiTest
    Requisitando um POST na rota "/post" do httpbin
    StatusCode deve ser "200"

#Requisita informação do serviço. EX: saber se usuário esta cadastrado no banco de dados à partir de um Email enviado 
GET on a service
    [tags]      apiTest
    Requisitando um GET na rota "/get" do httpbin
    StatusCode deve ser "200"

#Envia informação ao serviço, porém serve mais para ATUALIZAR os dados. EX: Modificação dps dados do usuario num site. Envia todos os dados da pessoa ao banco de dados para atualizar
PUT on a service
    [tags]      apiTest
    Requisitando um PUT na rota "/put" do httpbin
    StatusCode deve ser "200"

#Deleta informação. EX: Deletar usuário de um banco de dados à partir de um Email enviado.
DELETE on a service
    [tags]      apiTest
    Requisitando um DELETE na rota "/delete" do httpbin
    StatusCode deve ser "200"