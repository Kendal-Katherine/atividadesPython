# -*- coding: utf-8 -*-
"""aula-08-03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/Kendal-Katherine/fc5e6bcd915a9359a3c9995dccb8a658/aula-08-03.ipynb
"""

print("Olá, mundo!")

print('Olá, mundo!')

print(7 * 5)

print(5 / 2)
print(5 // 2)

"""COM UM "/" ELE EFETUA A DIVISÃO. COM DUAS "//" ELE TE DÁ O RESULTADO SEM O DECIMAIS"""

print("Chuva " * 5)

"""Ele também multiplica strings, com aspas simples ou duplas."""

print("5" * 5)
print(5 * 5)

"""SE FOR UM NÚMERO E ESTIVER DENTRO DAS ASPAS, ELE LÊ COMO SE FOSSE STRING E NÃO NÚMERO


"""

a = 10
print(a)

"""DECLARANDO O VALOR DA VARIÁVEL 

"""

type(a)

"""DESCOBRINDO O TIPO DE VARIÁVEL

"""

b = 7.5
print(b)
type(b)

nome = "Luciano"
print(nome)
type(nome)

print("Seu nome é " + nome)

"""CONCATENAÇÃO - criamos uma frase e fizemos a concatenação da string nome"""

idade = 25
print("Sua idade é " + idade) #NÃO É POSSÍVEL CONCATENAR STRING COM NÚMERO INTEIRO

idade = 25
print("Sua idade é ", idade) #COLOCANDO A VÍRGULA AO INVÉS DE "+" SE TORNA POSSÍVEL

nome1 = "Sandra"
idade1 = 40
print("Meu nome é", nome1,", tenho",idade1, "anos") #exercício proposto pela professora

print(f"Meu nome é {nome1}, tenho {idade1} anos.") #colocando o "f" no inicio e colocando as variáveis entre {} a frase fica mais bonita e organizada

a = 10
b = 15
c = a + b
print(f"A soma é {c}") # posso fazer dessa forma ou da forma abaixo, nessa eu uso uma variável extra para fazer a soma

print(f"A soma é {a+b}") #ou dessa forma! Nessa eu faço a soma direto no texto. O ideal é dessa forma por conta de não ter que declarar uma variável de soma, se for coisa mometânea essa é suficiente!

"""EXERCÍCIO
Leia 3 notas e o nome de um aluno e mostre a média




"""

nota1= 10
nota2= 10
nota3= 7
nAluno = "Kendal Katherine"
print(f"A média do(a) aluno(a): {nAluno}, é {(nota1 + nota2 + nota3)/3:.1f}.") #calculos matemáticos lembrar de colocar o "()" isso determina a prioridade de calculo

print(5**2) #eleva a potência

"""TESTAR SE O NÚMERO É PAR

DIVIDA O NÚMERO POR 2 E TESTE O RESTO, SE FOR 0 O NÚMERO É PAR, SE FOR 1 O NÚMERO É ÍMPAR
O COMANDO USADO É O % - MOD(MÓDULO)
"""

print(4 % 2) # isso retorna o resto da divisão e dá para determinar se o número é par ou ímpar, é para todas da linguagens "%"

"""AGORA INICIAREMOS OS COMANDOS DE ENTRADA DE DADOS - INPUT"""

input("Qual é o seu nome? ")

nome3 = input("Qual é o seu nome? ")
print(f"O seu nome é {nome3}, por sinal um lindo nome!")

idade = input("Qual é a sua idade? ")
print(idade * 2) #ele repitiu o 2525 pq ele recebeu a idade como string e não como um int, é necessário fazer um casting

idade = int(input("Qual é a sua idade? "))#colocando o int antes do input, você determina o tipo de variável que deve ser usada, isso é o "casting", para float, int é necessário, mas para string não
print(idade * 2)

#IF SIMPLES
nome = input("Nome do(a) aluno(a): ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media1 = (nota1 + nota2 + nota3) / 3

print(f"A média do(a) aluno(a) é {media1:.1f}")

if media1 >= 6: #diferente das outras linguagens não precisa colocar as chaves {} para iniar o if/else, mas é uma linguagem indentada, ou seja, a posição das informações determina se o código funciona ou não, isso também é diferente das outras linguagens
  print("APROVADO(A)")
else:
  print("REPROVADO(A)")

#IFS ANINHADOS!!!!!
nome = input("Nome do(a) aluno(a): ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media1 = (nota1 + nota2 + nota3) / 3

print(f"A média do(a) aluno(a) é {media1:.1f}")

if media1 >= 6: #
  print("APROVADO(A)")
elif media <=4: #aninhados de if/else/elif = muito importante pode colocar vários elif's
  print("REPROVADO(A)")
else:
  print("ALUNO(A) FICOU DE RECUPERAÇÃO")

"""EXERCÍCIOS
01) LER DOIS NÚMEROS INTEIROS E MOSTRAR O RESULTADO DAS SEGUINTES OPERAÇÕES: ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO E DIVISÃO.
"""

A = int(input("Digite o primeiro número inteiro: "))
B = int(input("Digite o segundo número inteiro: "))
print(f"A ADIÇÃO destes número gera o seguinte resultado: {A+B}")
print(f"A SUBTRAÇÃO destes número gera o seguinte resultado: {A-B}")
print(f"A MULTIPLICAÇÃO destes número gera o seguinte resultado: {A*B}")
print(f"A DIVISÃO destes número gera o seguinte resultado: {A/B}")

"""EXECÍCIO
02)
"""

tempo = int(input("Digite o tempo gasto na viagem: "))
veloc = float(input("Digite a velocidade média durante a viagem: "))
distancia = tempo * veloc
litros_usados = distancia / 12
print(f"A velocidade média foi de {veloc}KM/h, o tempo gasto na viagem foi de {tempo} horas, a distância percorrida na viagem foi de {distancia} KM e a quantidade de litros de combustível foi de {litros_usados:.1f}.")

"""EXERCÍCIO 3
Leia a idade de uma pessoa e classifique-o em:
Criança – 0 a 12 anos
Adolescente – 13 a 17 anos
Adulto – acima de 18 anos
Se o usuário digitar um número negativo, mostra a mensagem
que a idade é inválida. 
"""

idade = int(input('Digite a idade: '))
if idade <0:
    print(f" {idade} ano(s), é uma idade INVÁLIDA")
elif idade <=12:
  print(f"A pessoa com a idade de {idade} ano(s), é uma crinça")
elif idade <=17:
    print(f"A pessoa com a idade de {idade} anos, é uma adolescente")
else:
    print(f"A pessoa com a idade de {idade} anos, é uma Adulto")

"""EXERCÍCIO 4
Faça um programa que leia o nome e três notas de um aluno, calcule
sua média e mostre uma mensagem segundo os critérios:
- Se a média for maior ou igual a 6 – APROVADO
- Se a média for menor ou igual a 4 – REPROVADO
- Se a média estiver entre 4 e 6 – RECUPERAÇÃO
"""

nome = input("Digite o nome do aluno(a): ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media= ((n1+n2+n3) / 3)

if media >=6:
  print(f"O(a) aluno(a): {nome} obteve a média de: {media:.2f} e está APROAVADO!")
elif media <= 4 :
    print(f"O(a) aluno(a): {nome} obteve a média de: {media:.2f} e está REPROVADO!")
else: 
    print(f"O(a) aluno(a): {nome} obteve a média de: {media:.2f} e está de RECUPERAÇÃO!")

