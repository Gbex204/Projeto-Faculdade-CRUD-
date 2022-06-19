import time
import menu
from clientes import saveDb, loadDb, print_cor, CorAmarelo, CorAzul, CorVerde, CorVerm, CorVoltar
from clientes import validarInt, verifyName
fileProducts = 'cadastrosProdutos.json'

dicProdutos = {}
dicProdutos = loadDb(dicProdutos, fileProducts)

#Procurar jogo no sistema
def procurar(dic):
    while True:
        procurar = input('Digite o nome do jogo a ser procurado no estoque\n-> ')
        if dic == {}:
            print('Processando ...')
            time.sleep(1.2)
            return print('Não há produtos no estoque!!!!!!')
        try:
            if dic[procurar]["NomeProd"] == procurar:
                print('Procurando produto ...')
                time.sleep(1.2)
                print(f'O produto {dic[procurar]["NomeProd"]} foi encontrado no estoque')
                break
        except:
            print('Procurando produto ...')
            time.sleep(1.2)
            print('Produto nao encontrado tente novamente!!!!!')

def excluirProd():
    print('\n')
    print('==' * 15)
    print('Exclusão de Produtos')
    print('==' * 15)
    print('\n')
    print('Lista de Produtos: ')
    for keyProdutos in dicProdutos:
        print(f'[{keyProdutos}]')
        print(f'Nome: {dicProdutos[keyProdutos]["NomeProd"]}')
        print(f'Descrição produto: {dicProdutos[keyProdutos]["DescProduto"]}')
        print(f'Preço: {dicProdutos[keyProdutos]["Preço"]}')
        print(f'Desenvolvedor: {dicProdutos[keyProdutos]["Desenvolvedor"]}')
        print(f'Categoria: {dicProdutos[keyProdutos]["Categoria"]}')
        print(f'Quantidade no estoque: {dicProdutos[keyProdutos]["quant"]}')
        print('\n')
    dicPraRemover = input('Digite o nome do produto a ser removido: ')
    print(f'\nNome: {dicProdutos[dicPraRemover]["NomeProd"]}')
    print(f'Descrição produto: {dicProdutos[dicPraRemover]["DescProduto"]}')
    print(f'Preço: {dicProdutos[dicPraRemover]["Preço"]}')
    print(f'Desenvolvedor: {dicProdutos[dicPraRemover]["Desenvolvedor"]}')
    print(f'Categoria: {dicProdutos[dicPraRemover]["Categoria"]}')
    print(f'Quantidade no estoque:{dicProdutos[dicPraRemover]["quant"]}')
    print('\n')
    opcaoExcluir = input('Certeza que você quer apagar este cadastro? (S/N)\n•')
    if opcaoExcluir == 's' or opcaoExcluir == 'S':
        del dicProdutos[dicPraRemover]
        print('Cadastro removido com sucesso!')
        saveDb(dicProdutos, fileProducts)
    elif opcaoExcluir == 'n' or opcaoExcluir == 'N':
        print('Operação de excluir cancelada!')
    else:
        print(f'[{opcaoExcluir}] é uma opção inválida! Tente novamente...')

# Cadastrar um Jogo/Produto
def cadProd():
    print("="*55)
    print("                Cadastro de Produtos")
    print("=" * 55)
    nomeProduto = input("Digite o nome do Jogo:\n-> ")
    descProduto = input("Digite a descrição do produto:\n-> ")
    categoria = input("Selecione a categoria do jogo:\n-> ")
    valor = float(input("Digite o preço do jogo - R$:\n-> "))
    empresa = input(f"Digite o nome da empresa que desenvolveu o jogo ({nomeProduto}):\n-> ")
    quant = int(input('Digite a quantidade do produto:\n-> '))
    cadastroJogo = {"NomeProd": nomeProduto, "DescProduto": descProduto, "Preço": valor, "Desenvolvedor": empresa,
                    "Categoria": categoria, "quant": quant}
    dicProdutos[nomeProduto] = cadastroJogo
    print(cadastroJogo)
    print("Cadastrando produto...")
    time.sleep(1.2)
    print("Produto cadastrado!")
    saveDb(dicProdutos, fileProducts)
    return dicProdutos

# Excluir produto




def editarProd():
    print('==' * 15)
    print('            Edição')
    print('==' * 15)
    print('\n')
    print('Lista de produtos: ')
    for keyProdutos in dicProdutos:
        print(f'[{keyProdutos}]')
        print(f'Nome: {dicProdutos[keyProdutos]["NomeProd"]}')
        print(f'Descrição produto: {dicProdutos[keyProdutos]["DescProduto"]}')
        print(f'Preço: {dicProdutos[keyProdutos]["Preço"]}')
        print(f'Desenvolvedor: {dicProdutos[keyProdutos]["Desenvolvedor"]}')
        print(f'Categoria: {dicProdutos[keyProdutos]["Categoria"]}')
        print(f'Quantidade no estoque: {dicProdutos[keyProdutos]["quant"]}')
        print('\n')
    dicPraEdit = input('Digite o nome do produto a ser editado: ')
    print(f'\n[1] Nome: {dicProdutos[dicPraEdit]["NomeProd"]}')
    print(f'[2] Descrição produto: {dicProdutos[dicPraEdit]["DescProduto"]}')
    print(f'[3] Preço produto: {dicProdutos[dicPraEdit]["Preço"]}')
    print(f'[4] Desenvolvedora: {dicProdutos[dicPraEdit]["Desenvolvedor"]}')
    print(f'[5] Categoria: {dicProdutos[dicPraEdit]["Categoria"]}')
    print(f'[6] Quantidade: {dicProdutos[dicPraEdit]["quant"]}')

    opEdit = validarInt('Qual das informações você gostaria de editar?: ')
    if opEdit == 1:
        novoNome = input('Novo nome: ')
        novoNome = verifyName(novoNome)
        dicProdutos[dicPraEdit]['NomeProd'] = novoNome
        print('\nEdição de nome concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 2:
        novaDesc = input('Nova Descrição:')
        novaDesc = verifyName(novaDesc)
        dicProdutos[dicPraEdit]['DescProduto'] = novaDesc
        print('Processando ...\n')
        time.sleep(1.2)
        print('\nEdição de Descrição concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 3:
        novoPreco = float(input('Novo preço: '))
        dicProdutos[dicPraEdit]["Preço"] = novoPreco
        print('Processando ...\n')
        time.sleep(1.2)
        print('\nEdição de preço concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 4:
        novaDesenvolvedora = input('Nova desenvolvedora: ')
        novaDesenvolvedora = verifyName(novaDesenvolvedora)
        dicProdutos[dicPraEdit]['Desenvolvedor'] = novaDesenvolvedora
        print('Processando ...\n')
        time.sleep(1.2)
        print('Edição de desenvolvedora concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 5:
        novaCategoria = input('Nova categoria')
        novaCategoria = verifyName(novaCategoria)
        dicProdutos[dicPraEdit]['Categgoria'] = novaCategoria
        print('Processando ...\n')
        time.sleep(1.2)
        print('Edição de categoria concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 6:
        novaQuantidade = int(input('Nova quantidade'))
        dicProdutos[dicPraEdit]['quant'] = novaQuantidade
        print('Processando ...\n')
        time.sleep(1.2)
        print('Edição de quantidade concluída!')
        saveDb(dicProdutos, fileProducts)

    else:
        print(f'[{opEdit}] é uma opção inválida! Tente novamente...')


def menuProd():
    while True:
        print("=" * 55)
        print("                Setor de Produtos")
        print("=" * 55)
        print("[ 1 ] Cadastrar Jogo/Produto")
        print("[ 2 ] Procurar Jogo/Produto")
        print("[ 3 ] Editar Jogo/Produto")
        print("[ 4 ] Excluir Jogo/Produto")
        print("[ 5 ] Voltar para o menu principal")
        op = int(input("Escolha uma opção:\n"))
        if op == 1:
            cadProd()
        if op == 2:
            procurar(dicProdutos)
        if op == 3:
            editarProd()
        if op == 4:
            excluirProd()
        if op == 5:
            menu.menuPrincipal()