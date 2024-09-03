def pertence_a_fibonacci(n):
    
    if n < 0:
        return False

    
    a, b = 0, 1
    
    
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    
    return False

def main():
    try:
        
        num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        
        if pertence_a_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
