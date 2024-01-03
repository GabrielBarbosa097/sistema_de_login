#Sitema de Login
from getpass import getpass
print('-='*20)
print('BEM-VINDO AO SISTEMA')
print('-='*20)

print('''
[ 1 ] FAZER LOGIN
[ 2 ] CRIAR NOVO USUARIO''')

escolha = input('Escolha sua opção: ')

if escolha == '1':
    while True:
        nome = str(input('Digite o usuario: '))
        senha = getpass('Digite sua senha: ')
        escolha_usuario = nome + ',' + senha + '\n'
        with open ('usuario.txt') as arquivo:
            conteudo = arquivo.readline()
            if escolha_usuario in conteudo:
                print(f'Bem vindo {nome}, o seu login foi feito com sucesso!')
            else:
                print('Usuario/senha incorreta')

elif escolha == '2':
    while True:
        nome = str(input('Digite o nome do novo usario: '))
        senha = getpass('Digite sua senha')
        escolha_usuario = nome + ',' + senha + '\n'
        with open ('usuario.txt', 'a') as arquivo:
            arquivo.write(escolha_usuario)
        print(f'O Usario {nome} foi criado com sucesso')             
