## Sistema Bancário
Este é um projeto de sistema bancário que implementa funcionalidades básicas de depósito, saque, transferência e visualização de extrato. O sistema está disponível tanto como uma aplicação web usando Flask quanto como um script de linha de comando em Python.

## Funcionalidades
Depósito: Permite adicionar valores ao saldo da conta.
Saque: Permite retirar valores da conta com limites de saque e saldo.
Transferência: Permite transferir valores para outra conta.
Extrato: Visualiza o histórico de transações e o saldo atual.


## Tecnologias Utilizadas
Flask: Framework web para a aplicação web.
Python: Linguagem de programação usada para o script de linha de comando e para o backend da aplicação web.
Docker: Utilizado para criar uma imagem e contêiner para a aplicação web.


## Estrutura do Projeto
app.py: Código da aplicação web utilizando Flask.
sistema.bancario.py: Código do sistema bancário de linha de comando.
Dockerfile: Arquivo para construir a imagem Docker da aplicação web.
templates/: Diretório contendo os templates HTML index.html e extrato.html.

## Como Executar: 

Aplicação Web
Clone o repositório:
[git clone https://github.com/username/sistema-bancario.git](https://github.com/Lopeswaprojetos/Sistemabancario.git)
cd sistema-bancario

Instale as dependências:
pip install Flask

Execute a aplicação:
python app.py
Acesse a aplicação no seu navegador em http://127.0.0.1:5000.

Script de Linha de Comando
Clone o repositório:
git clone https://github.com/Lopeswaprojetos/sistema-bancario.git
cd sistema-bancario

Execute o script:
python sistema.bancario.py

## Usando Docker
Construa a imagem Docker:
docker build -t sistema-bancario .

Execute o contêiner Docker:
docker run -p 5000:5000 sistema-bancario
Acesse a aplicação no seu navegador em http://127.0.0.1:5000.

## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões, correções ou melhorias, sinta-se à vontade para abrir uma issue ou um pull request.

## Licença
Este projeto está licenciado sob a MIT License.



