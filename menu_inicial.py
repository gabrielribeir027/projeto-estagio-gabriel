from cad_proj import cadastro_projeto
opcao = 1 
while opcao != 6:
    print(''' == MENU DE OPÇÕES ==
    [1] CADASTRAR PROJETO
    [2] CADASTRAR TAREFA 
    [3] DEFINIR RESPONSÁVEIS 
    [4] INFORMAR DATAS DE ENTREGA
    [5] ACOMPANHAR ANDAMENTO 
    [6] ENCERRAR SISTEMA''')
    opcao = int(input('Digite a sua opção: '))
    if opcao == 1:
        cadastro_projeto()
print('PROGRAMA FINALIZADO...')
