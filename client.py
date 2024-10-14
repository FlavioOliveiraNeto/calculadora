import socket

# Função para enviar solicitação ao servidor
def enviar_solicitacao(operacao, numeros):
    # host = colocar o IP de host aqui
    # porta = colocar a porta aqui
    
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, porta))

    solicitacao = f"{operacao} {' '.join(map(str, numeros))}"
    cliente_socket.send(solicitacao.encode())

    resposta = cliente_socket.recv(1024).decode()
    cliente_socket.close()
    
    return resposta

# Menu do cliente
def menu():
    print("Calculadora Distribuída")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

# Função principal do cliente
def iniciar_cliente():
    while True:
        menu()
        opcao = input("Escolha uma operação: ")

        if opcao == '5':
            print("Encerrando o programa...")
            break

        numeros = input("Digite os números separados por espaço (máximo de 20 números): ").split()
        numeros = list(map(float, numeros[:20]))  # Limita a 20 números

        if opcao == '1':
            operacao = 'soma'
        elif opcao == '2':
            operacao = 'subtrair'
        elif opcao == '3':
            operacao = 'multiplicar'
        elif opcao == '4':
            operacao = 'dividir'
        else:
            print("Opção inválida!")
            continue

        resultado = enviar_solicitacao(operacao, numeros)
        print(f"Resultado: {resultado}")

# Inicializa o cliente
if __name__ == "__main__":
    iniciar_cliente()
