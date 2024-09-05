def fibonacci(posicao):
    if posicao <= 1:
        return posicao
    else:
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)

def main():
    try:
        posicao = int(input("Digite a posição na sequência de Fibonacci: "))
        if posicao < 0:
            print("A posição deve ser um número não-negativo.")
        else:
            result = fibonacci(posicao)
            print(f"O valor na posição {posicao} da sequência de Fibonacci é {result}.")
    except ValueError:
        print("Por favor, insira um número válido.")

main()
