def soma_impares(n):
    if n < 0:
        return 0
    if n % 2 != 0:
        return n + soma_impares(n - 2)
    else:
        return soma_impares(n - 1)

def main():
    try:
        valor = int(input("Digite um valor N: "))
        resultado = soma_impares(valor)
        print(f"A soma dos números ímpares menores ou iguais a {valor} é {resultado}.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
