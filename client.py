import socket

def main():
    while True:
        print("Escolha uma operação: ")
        print("1. Somar (ADD)")
        print("2. Subtrair (SUB)")
        print("3. Multiplicar (MUL)")
        print("4. Dividir (DIV)")
        print("5. Sair")
        
        choice = input("Digite o número da operação desejada: ")
        
        if choice == '5':
            break
        
        operation_map = {
            '1': 'ADD',
            '2': 'SUB',
            '3': 'MUL',
            '4': 'DIV'
        }
        
        operation = operation_map.get(choice)
        if not operation:
            print("Escolha inválida!")
            continue
        
        numbers = input("Digite os números separados por espaço: ").split()
        
        message = f"{operation} {' '.join(numbers)}"
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(('endereco-do-servidor', 15000))
            client.send(message.encode())
            result = client.recv(1024).decode()
            print(f"Resultado: {result}")

if __name__ == "__main__":
    main()
