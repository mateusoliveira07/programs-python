def mostrar_menu():
    print('''<<Menu>>
1. Cadastrar 
2. Visualizar 
3. Editar
4. Excluir 
5. Sair do programa''')

def mostrar_cadastros():
    for cad, registro in enumerate(zip(lista_nome, lista_idade, lista_email)):
        print(f'---{cad}° cadastro--- \nNome: {lista_nome[cad]} | Idade: {lista_idade[cad]} | E-mail: {lista_email[cad]}')

lista_nome = []
lista_idade = []
lista_email = []

mostrar_menu()
opcao = int(input('Digite uma opção: '))

while True:

    if opcao == 1: #Responsável por fazer o registro de um novo cadastro
        nome = input('\nDigite o seu nome: ')
        idade = int(input('Digite a sua idade: '))
        email = input('Digite o seu email: ')
        lista_nome.append(nome)
        lista_idade.append(idade)
        lista_email.append(email)
        print('\nCadastro realizado!\n')
        mostrar_menu()
        opcao = int(input('Digite uma opção: '))

    elif opcao == 2: #Será utilizado quando o usuário desejar ver a lista de cadastros
        mostrar_cadastros()
        mostrar_menu()
        opcao = int(input('Digite uma opção: '))

    elif opcao == 3: #Será usado para fazer alguma alteração de informação específica
        for i, cadastros in enumerate(zip(lista_nome, lista_idade, lista_email)):
            print(f'---{i}° Cadastro--- \nNome: {lista_nome[i]} | Idade: {lista_idade[i]} | E-mail: {lista_email[i]} | Digite {i} para editar')
        editar = int(input('Digite o cadastro que queira editar: '))

        if editar < 0 or editar >= len(lista_nome):
            print('\nCadastro inexistente!\n')
            mostrar_menu()
            opcao = int(input('Digite uma opção: '))
            continue

        print(f'---{editar}° Cadastro--- \nNome: {lista_nome[editar]} | Idade: {lista_idade[editar]} | E-mail: {lista_email[editar]}')
        edicao = int(input('(0) Nome | (1) Idade | (2) E-mail \nDigite a opção que queira editar: '))
        if edicao == 0:
            novo_nome = input('Digite o novo nome: ')
            lista_nome[editar] = novo_nome
            print('\nNome alterado com sucesso!\n')
            mostrar_menu()
            opcao = int(input('Digite uma opção: '))

        elif edicao == 1:
            nova_idade = int(input('Digite a nova idade: '))
            lista_idade[editar] = nova_idade
            print('\nIdade alterada com sucesso!\n')
            mostrar_menu()
            opcao = int(input('Digite uma opção: '))

        elif edicao == 2:
            novo_email = input('Digite o novo e-mail: ')
            lista_email[editar] = novo_email
            print('\nE-mail alterado com sucesso!\n')
            mostrar_menu()
            opcao = int(input('Digite uma opção: '))

        else:
            print('A opção digitada não é válida.')
            mostrar_menu()
            opcao = int(input('Digite uma opção: '))

    elif opcao == 4: #Remover cadastros de usuários

        for i, cadastros in enumerate(zip(lista_nome, lista_idade, lista_email)):
            print(f'---{i}° Cadastro--- \nNome: {lista_nome[i]} | Idade: {lista_idade[i]} | E-mail: {lista_email[i]} | Digite {i} para excluir')
        excluir = int(input('Digite o cadastro que deseja excluir: '))

        if excluir < 0 or excluir >= len(lista_nome):
            print('\nCadastro inexistente!\n')
            mostrar_menu()
            opcao = int(input('Digite uma opção: '))
            continue

        lista_nome.pop(excluir)
        lista_idade.pop(excluir)
        lista_email.pop(excluir)
        mostrar_menu()
        opcao = int(input('Digite uma opção: '))

    elif opcao == 5: #Executa a saída e quebra do programa
        print('Saindo do programa...')
        break

    else: #Caso o usuário digite alguma opção que não seja entre 1 e 5
        print('A opção digitada não é válida, tente novamente.')
        mostrar_menu()
        opcao = int(input('Digite uma opção válida: '))