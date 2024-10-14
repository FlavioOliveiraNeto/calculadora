import socket

# Funções para operações aritméticas
def somar(numeros):
    return sum(numeros)

def subtrair(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicar(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def dividir(numeros):
    resultado = numeros[0]
    try:
        for num in numeros[1:]:
            resultado /= num
        return resultado
    except ZeroDivisionError:
        return "Erro: divisão por zero."

# Função para processar a solicitação do cliente
def processar_solicitacao(solicitacao):
    try:
        dados = solicitacao.split()
        operacao = dados[0]
        numeros = list(map(float, dados[1:]))

        if len(numeros) > 20:
            return "Erro: máximo de 20 números permitidos."

        if operacao == 'soma':
            return somar(numeros)
        elif operacao == 'subtrair':
            return subtrair(numeros)
        elif operacao == 'multiplicar':
            return multiplicar(numeros)
        elif operacao == 'dividir':
            return dividir(numeros)
        else:
            return "Erro: operação inválida."
    except Exception as e:
        return f"Erro: {str(e)}"

# Configurações do servidor
def iniciar_servidor():
    # host = colocar o IP de host aqui
    # porta = colocar a porta aqui

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(5)
    print(f"Servidor iniciado na porta {porta}...")

    while True:
        conexao, endereco = servidor_socket.accept()
        print(f"Conexão estabelecida com {endereco}")

        dados = conexao.recv(1024).decode()
        if not dados:
            break
        
        print(f"Solicitação recebida: {dados}")
        resposta = str(processar_solicitacao(dados))
        conexao.send(resposta.encode())

        conexao.close()

# Inicializa o servidor
if __name__ == "__main__":
    iniciar_servidor()
