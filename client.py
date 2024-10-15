import socket
import sys

# Função para enviar solicitação ao servidor
def enviar_solicitacao(host, operacao, numeros):

    porta = 15000
    
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
    print("5. Sair\n")

# Função principal do cliente
def iniciar_cliente(host):
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

        resultado = enviar_solicitacao(host, operacao, numeros)
        print(f"\nResultado: {resultado}\n")

# Inicializa o cliente
if __name__ == "__main__":
    # Verifica se o IP do host foi passado como argumento
    if len(sys.argv) < 2:
        print("Uso: python cliente.py <IP_DO_HOST>")
        sys.exit(1)

    # Obtém o IP do host a partir dos argumentos da linha de comando
    host = sys.argv[1]
    iniciar_cliente(host)
