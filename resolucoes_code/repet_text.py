# Solicita uma string ao usuário
string = input("Digite uma string: ").strip()

# Solicita um número inteiro ao usuário com validação
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# Repete a string o número de vezes especificado e exibe o resultado
resultado = (string + ' ') * numero
print(f"O resultado é:\n{resultado.strip()}")
