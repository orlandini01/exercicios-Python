'''
1. Escreva um programa que receba 2 números de sua escolha e que depois
imprima a soma, a subtração, multiplicação, divisão, divisão inteira, o resto da
divisão do maior pelo menor e coloque na mensagem a palavra resto ao invés de
símbolo %.
'''

n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))

soma = n1 + n2
subtrair = n1 - n2 
dividir = n1 / n2
multiplicar = n1 * n2
resto = n1 % n2

print("Valor somado: ", soma)
print("Valor subtraido: ", subtrair)
print("Valor dividido: ", dividir)
print("Valor multiplicado: ", multiplicar)
print("Valor resto da divisão: ", resto)


'''-----------------------------------------------------------------------------'''

'''
2. Faça um programa que peça as 4 notas bimestrais e mostre a média do aluno
'''

nota1 = float(input("Digite o valor da AV1: "))
nota2 = float(input("Digite o valor da AV2: "))
nota3 = float(input("Digite o valor da AV3: "))
nota4 = float(input("Digite o valor da AV4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"O valor da media é: {media}")


'''-----------------------------------------------------------------------------'''

'''
3. Crie um script Python que leia o dia, mês e ano de nascimento de uma pessoa e
mostre uma mensagem com a data formatada.
'''

dia = int(input("Digite o dia que você nasceu: "))
mes = int(input("Digite o mês que você nasceu: "))
ano = int(input("Digite o ano que você nasceu: "))

print(f"Você nasceu em {dia}/{mes}/{ano}")


'''-----------------------------------------------------------------------------'''

'''
4. Organize os números 2,3,4,5,10,12 para obter a saída (resposta) 18 em uma
única operação
'''

print(12 + 10 + 5 -4 -3 -2)


'''-----------------------------------------------------------------------------'''

'''
5. Crie um programa que leia o nome completo de uma pessoa e mostre:
a) O nome com todas as letras maiúsculas e minúsculas
b) Quantas letras ao todo
c) Quantas letras tem o primeiro nome
'''
nome = input("Digite seu nome: ")

print("Nome em letras maiúsculas:", nome.upper())
print("Nome em letras minúsculas:", nome.lower())

qtd_letras = len(nome.replace(" ", ""))
print("Quantidade total de letras:", qtd_letras)

primeiro_nome = nome.split()[0]
print("Quantidade de letras no primeiro nome:", len(primeiro_nome))
