import csv, pickle, json
from contato import Contato


def csv_para_contatos(caminho, encoding="latin_1"):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id, nome, email = linha

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos

def contatos_para_pickle(contatos, caminho):
    with open(caminho, "wb") as arquivo:
        pickle.dump(contatos, arquivo)

def pickle_para_contato(caminho):
    with open(caminho, mode="rb") as arquivo:
        contatos = pickle.load(arquivo)

    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, "w") as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)

def _contato_para_json(contato):
    return {key.replace('_Contato__', ''):value for key, value in contato.__dict__.items()}

def json_para_contato(caminho):

    contatos = []

    with open(caminho, mode="r") as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            c = Contato(**contato)
            contatos.append(c)

    return contatos