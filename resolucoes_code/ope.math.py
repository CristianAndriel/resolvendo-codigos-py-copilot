# Função para mostrar o menu de operações
def mostrar_menu():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

# Função principal para realizar as operações
def calculadora():
    while True:
        mostrar_menu()
        
        # Solicita ao usuário qual operação ele deseja realizar
        escolha = input("Digite o número da operação desejada (1/2/3/4/5): ")
        
        if escolha == '5':
            print("Saindo da calculadora...")
            break
        
        # Solicita os números para a operação
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        
        # Realiza a operação com base na escolha do usuário
        if escolha == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif escolha == '4':
            if num2 == 0:
                print("Erro: Não é possível dividir por zero.")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Opção inválida! Tente novamente.")

# Chama a função da calculadora
calculadora()
