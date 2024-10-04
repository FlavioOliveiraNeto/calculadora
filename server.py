import socket

def process_operation(operation, numbers):
    try:
        numbers = list(map(float, numbers))
        if len(numbers) > 20:
            return "Erro: máximo de 20 números permitidos."
        
        if operation == "ADD":
            return str(sum(numbers))
        elif operation == "SUB":
            return str(numbers[0] - sum(numbers[1:]))
        elif operation == "MUL":
            result = 1
            for num in numbers:
                result *= num
            return str(result)
        elif operation == "DIV":
            result = numbers[0]
            try:
                for num in numbers[1:]:
                    result /= num
                return str(result)
            except ZeroDivisionError:
                return "Erro: divisão por zero."
        else:
            return "Erro: operação inválida."
    except ValueError:
        return "Erro: entrada inválida."

def handle_client(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        parts = data.split()
        operation = parts[0]
        numbers = parts[1:]
        result = process_operation(operation, numbers)
        conn.send(result.encode())
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 15000))
    server.listen(5)
    print("Servidor de calculadora distribuída iniciado...")
    
    while True:
        conn, addr = server.accept()
        print(f"Conectado a {addr}")
        handle_client(conn)

if __name__ == "__main__":
    main()
