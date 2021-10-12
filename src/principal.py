from src import contatos_utils

try:
    contatos = contatos_utils.csv_para_contatos("../dados/contatos.csv")
    # contatos_utils.contatos_para_pickle(contatos, "dados/contatos.pickle")

    contatos_utils.contatos_para_json(contatos, "../dados/contatos.json")

    contatos_importados = contatos_utils.json_para_contato("../dados/contatos.json")

    for contato in contatos_importados:
        print(contato)

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')

