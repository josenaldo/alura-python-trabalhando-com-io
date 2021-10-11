import pytest
from unittest.mock import (patch, MagicMock, mock_open)
from src.contato import Contato
from src.contatos_utils import csv_para_contatos

@pytest.fixture
def lista_de_contatos():
    lista_de_contatos = [
        Contato('1', 'Guilherme', 'guilherme@guilherme.com.br'),
        Contato('2', 'Elias', 'elias@elias.com.br'),
        Contato('3', 'Gabriel', 'gabriel@gabriel.com.br'),
        Contato('4', 'Anderson', 'anderson@anderson.com.br'),
        Contato('5', 'Alex', 'alex@alex.com.br'),
        Contato('6', 'Vini', 'vini@vini.com.br'),
        Contato('7', 'Letícia', 'leticia@leticia.com.br'),
        Contato('8', 'Giulia', 'giulia@giulia.com.br'),
        Contato('9', 'Felipe', 'felipe@felipe.com.br'),
        Contato('10', 'Luísa', 'luisa@luisa.com.br'),
    ]
    return lista_de_contatos

@pytest.fixture
def linhas():

    linhas = "1,Guilherme,guilherme@guilherme.com.br\n"\
    "2,Elias,elias@elias.com.br\n"\
    "3,Gabriel,gabriel@gabriel.com.br\n"\
    "4,Anderson,anderson@anderson.com.br\n"\
    "5,Alex,alex@alex.com.br\n"\
    "6,Vini,vini@vini.com.br\n"\
    "7,Letícia,leticia@leticia.com.br\n"\
    "8,Giulia,giulia@giulia.com.br\n"\
    "9,Felipe,felipe@felipe.com.br\n"\
    "10,Luísa,luisa@luisa.com.br\n"

    return linhas


def test_deve_retornar_uma_lista_de_contatos(lista_de_contatos, linhas):

    fp = mock_open(read_data=linhas)

    with patch("src.contatos_utils.open", fp):
        contatos = csv_para_contatos('arquivo')

    assert contatos == lista_de_contatos