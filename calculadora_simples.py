def start():
    print("Bem-vindo!")

def operation():
    op = float(input("1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão: "))
    numero_um = float(input("Insira um número: "))
    numero_dois = float(input("Insira outro número: "))

    if op == 1:
        resultado = float(numero_um) + float(numero_dois)
        print(f"O resultado da soma entre {numero_um} e {numero_dois} é igual a {resultado}!")

    elif op == 2:
        resultado = float(numero_um) - float(numero_dois)
        print(f"O resultado da subtração entre {numero_um} e {numero_dois} é igual a {resultado}!")
    
    elif op == 3:
        resultado = float(numero_um) * float(numero_dois)
        print(f"O resultado da multiplicação entre {numero_um} e {numero_dois} é igual a {resultado}!")

    elif op == 4:
        resultado = float(numero_um) / float(numero_dois)
        print(f"O resultado da divisão entre {numero_um} e {numero_dois} é igual a {resultado}!")
    
    else:
        resultado = "Operador não encontrado!"
        print(resultado)

# def restart(): ---- AINDA SERÁ IMPLEMENTADO ----

def finish():
    print("Goodbye!")



start()
operation()
finish()