def contador(n):
    
    if n < 0:
        return
   
    print(n)
    contador(n - 1)

def main():
  
    try:
        valor = int(input("Digite um valor: "))
        contador(valor)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")


if __name__ == "__main__":
    main()
