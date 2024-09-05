def contador(atual, n):
    if atual > n:
        return
   
    print(atual)
    contador(atual + 1, n)

def main():
    try:
        valor = int(input("Digite um valor: "))
       
        contador(0, valor)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")


if __name__ == "__main__":
    main()
