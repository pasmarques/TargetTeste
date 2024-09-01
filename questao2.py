def is_fibonacci(n):
    # Função para verificar se um número pertence à sequência de Fibonacci.
    
    # Os dois primeiros números na sequência de Fibonacci
    fib1, fib2 = 0, 1
    
    # Verifica se o número informado é um dos primeiros da sequência
    if n == fib1 or n == fib2:
        return True
    
    # Gera números na sequência de Fibonacci até que o número gerado seja igual ou maior que o número informado
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2
    
    # Se o número gerado é igual ao número informado, ele pertence à sequência
    return n == fib2

# Solicita ao usuário para inserir um número
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência de Fibonacci e exibe o resultado
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
