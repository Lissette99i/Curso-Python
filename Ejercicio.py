def EvaluacionNumero (numero):
    if numero == 10 :
        print("El Numero Ingresado Es 10")
    elif numero == 7 :
        print("Se Ha Ingresado Un Comodin")
    elif numero % 2 == 0 :
        print("El Numero Ingresado Es Par")
    else:
        print("El Numero Ingresado Es Impar")
        
def main():
    numero= int(input("Ingrese Un Numero: "))
    EvaluacionNumero (numero)

if __name__ == "__main__":
    main()  
