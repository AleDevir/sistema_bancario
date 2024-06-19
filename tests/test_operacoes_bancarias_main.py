# pylint: disable=line-too-long
'''
Testes do artefato operacoes_bancarias.py
pytest tests/test_operacoes_bancarias.py -vv
'''

from unittest.mock import patch
from unittest import TestCase
from operacoes_bancarias import (
    main,
)


class Test(TestCase):
    '''
    Classe de teste para inputs.
    '''
    ################################################
     # TESTES DO FLUXO PRINCIPAL -> MAIN #
    ################################################
    @patch('operacoes_bancarias.exibir_extrato')
    @patch('operacoes_bancarias.depositar')
    @patch('operacoes_bancarias.sacar')
    @patch('operacoes_bancarias.escolher_uma_opcao_do_menu_entrada')
    # @patch('operacoes_bancarias.exibir_mensagem_de_boas_vindas')
    @patch('operacoes_bancarias.obter_usuario')
    def test_main_opcao_finalizar( # pylint: disable=too-many-arguments
        self,
        obter_usuario,
        escolher_uma_opcao_do_menu_entrada,
        sacar,
        depositar,
        exibir_extrato,
    ):
        '''
        Teste do fluxo principal - main() Opção 'F' -> FINALIZAR
        python -m unittest -v tests.test_operacoes_bancarias_main.Test.test_main_opcao_finalizar -v
        '''
        obter_usuario.return_value =  {
            'id': 5,
            'nome': 'testes'
        }
        escolher_uma_opcao_do_menu_entrada.return_value = 'F'
        exibir_extrato.return_value = None
        depositar.return_value = None
        sacar.return_value = None
        main()

    @patch('operacoes_bancarias.exibir_extrato')
    @patch('operacoes_bancarias.depositar')
    @patch('operacoes_bancarias.sacar')
    @patch('operacoes_bancarias.escolher_uma_opcao_do_menu_entrada')
    # @patch('operacoes_bancarias.exibir_mensagem_de_boas_vindas')
    @patch('operacoes_bancarias.obter_usuario')
    def test_main_opcao( # pylint: disable=too-many-arguments
        self,
        obter_usuario,
        escolher_uma_opcao_do_menu_entrada,
        sacar,
        depositar,
        exibir_extrato,
    ):
        '''
        Teste do fluxo principal - main() Opção 'S' -> SACAR
        python -m unittest -v tests.test_operacoes_bancarias_main.Test.test_main_opcao -v
        '''
        obter_usuario.return_value =  {
            'id': 5,
            'nome': 'testes'
        }
        escolher_uma_opcao_do_menu_entrada.side_effect = ['D', 'E', 'S', 'F']
        exibir_extrato.return_value = None
        depositar.return_value = None
        sacar.return_value = None
        main()
