def cadastro_projeto():
    while True:
        print('====== CADASTRO PROJETO ======')
        opcao = input('Deseja cadastrar um novo projeto? (S/N) ').upper()
        if opcao == 'N':
            break
        elif opcao != 'S':
            print('OPÇÃO INVÁLIDA! DIGITE S OU N.')
            continue
        id = int(input('ID: '))
        nome = input('NOME: ')
        print('Seja breve com a sua descrição!')
        desc = input('DESCRIÇÃO: ')
        data_inicio = input('INÍCIO PREVISTO (DD/MM/AAAA): ')
        data_fim = input('CONCLUSÃO PREVISTA (DD/MM/AAAA): ')
        print('='*30)
