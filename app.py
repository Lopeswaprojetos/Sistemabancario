from flask import Flask, request, render_template

app = Flask(__name__)

# Inicializando variáveis
saldo = 0
limite = 500
limite_transferencia = 10000000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/depositar', methods=['POST'])
def depositar():
    global saldo, extrato
    try:
        valor = request.form['valor'].replace(',', '.')  # Substitui vírgula por ponto
        valor = float(valor)
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            return "✅ Depósito realizado com sucesso!"
        else:
            return "⚠ Operação falhou! O valor informado é inválido."
    except ValueError:
        return "⚠ Operação falhou! Valor inválido."

@app.route('/sacar', methods=['POST'])
def sacar():
    global saldo, extrato, numero_saques
    try:
        valor = request.form['valor'].replace(',', '.')  # Substitui vírgula por ponto
        valor = float(valor)
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            return "⚠ Operação falhou! Você não tem saldo suficiente."
        elif excedeu_limite:
            return "⚠ Operação falhou! O valor do saque excede o limite."
        elif excedeu_saques:
            return "⚠ Operação falhou! Número máximo de saques excedido."
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            return "✅ Saque realizado com sucesso!"
        else:
            return "⚠ Operação falhou! O valor informado é inválido."
    except ValueError:
        return "⚠ Operação falhou! Valor inválido."

@app.route('/extrato')
def mostrar_extrato():
    return render_template('extrato.html', extrato=extrato, saldo=saldo)

@app.route('/transferir', methods=['POST'])
def transferir():
    global saldo, extrato
    try:
        valor = request.form['valor'].replace(',', '.')  # Substitui vírgula por ponto
        valor = float(valor)
        conta = request.form['conta']
        
        excedeu_saldo = valor > saldo
        excedeu_limite_transferencia = valor > limite_transferencia

        if excedeu_saldo:
            return "⚠ Operação falhou! Você não tem saldo suficiente."
        elif excedeu_limite_transferencia:
            return "⚠ Operação falhou! O valor da transferência excede o limite."
        elif valor > 0:
            saldo -= valor
            extrato += f"Transferência para {conta}: R$ {valor:.2f}\n"
            return "✅ Transferência realizada com sucesso!"
        else:
            return "⚠ Operação falhou! O valor informado é inválido."
    except ValueError:
        return "⚠ Operação falhou! Valor inválido."

if __name__ == '__main__':
    app.run(debug=True)
