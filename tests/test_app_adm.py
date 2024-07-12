# pylint: disable=line-too-long
'''
Testes do fluxo principal app_adm.py
pytest tests/test_app_adm.py -vv
'''

from unittest.mock import patch, call
from unittest import TestCase



from src.app_adm import (
    admin,
    carregar_banco_de_dados
)



class Test(TestCase):
    '''
    Classe de teste para inputs.
    '''

    ################################################
     # TESTES DO FLUXO PRINCIPAL -> app_adm #
    ################################################

    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_opcao_de_entrada( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_opcao_de_entrada -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'C', 'SA'
        ]
        carregar_banco_de_dados()  
        admin()

    @patch('src.app_adm.get_input')
    @patch('src.app_adm.get_senha')
    @patch('src.app_adm.inserir_cliente')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_cl_a( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_cliente_mock,
        get_senha,
        get_input,
        ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_cl_a -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CL', 'A', 'SA'
        ]
        get_input.side_effect =  ['nome', 'sobrenome', '12706623098']
        get_senha.return_value = '123'
        inserir_cliente_mock.return_value = None
        admin()
        get_input.assert_has_calls([
            call('Nome: '),
            call('Sobrenome: '),
            call('CPF: '),
        ])
        get_senha.assert_has_calls([
            call('Senha: ')
        ])

    @patch('src.app_adm.inserir_cliente')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_cl_d( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_cliente_mock
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_cl_d -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CL', 'D', 'SA',
        ]
        inserir_cliente_mock.return_value = None
        admin()


    @patch('src.app_adm.inserir_cliente')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_cl_u( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_cliente_mock
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_cl_u -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CL', 'U', 'SA',
        ]
        inserir_cliente_mock.return_value = None
        admin()


    @patch('src.app_adm.inserir_cliente')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_cl_s( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_cliente_mock
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_cl_s -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CL', 'S', 'SA',
        ]
        inserir_cliente_mock.return_value = None
        admin()


    @patch('src.app_adm.input_int')
    @patch('src.app_adm.inserir_conta')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_co_a( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_conta_mock,
        input_int
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_co_a -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CO', 'A', 'SA'
        ]

        input_int.side_effect =  [9999, 99, 2, 2, 9]
        inserir_conta_mock.return_value = None
        admin()
        input_int.assert_has_calls([
            call('Numero da conta: '),
            call('Digito: '),
            call('Tipo (1: conta-corrente | 2: poupança): '),
            call('Agencia_id: '),
            call('Cliente_id: ')
        ])


    @patch('src.app_adm.inserir_conta')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_co_d( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_conta_mock
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_co_d -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CO', 'D', 'SA'
        ]
        inserir_conta_mock.return_value = None
        admin()
    
    @patch('src.app_adm.inserir_conta')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_co_u( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_conta_mock
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_co_u -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CO', 'U', 'SA'
        ]
        inserir_conta_mock.return_value = None
        admin()

    @patch('src.app_adm.inserir_conta')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_co_s( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_conta_mock
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_co_s -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CO', 'S', 'SA'
        ]
        inserir_conta_mock.return_value = None
        admin()

    @patch('src.app_adm.input_int')
    @patch('src.app_adm.inserir_agencia')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_ag_a( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_agencia_mock,
        input_int
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_ag_a -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'AG', 'A', 'SA'
        ]
        input_int.side_effect =  [444, 4]
        inserir_agencia_mock.return_value = None
        admin()
        input_int.assert_has_calls([
            call('Numero da agência: '),
            call('Digito: ')
        ])

    @patch('src.app_adm.inserir_agencia')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_ag_d( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_agencia_mock,
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_ag_d -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'CO', 'D', 'SA'
        ]
        inserir_agencia_mock.return_value = None
        admin()

    @patch('src.app_adm.inserir_agencia')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_ag_u( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_agencia_mock,
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_ag_u -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'AG', 'U', 'SA'
        ]
        inserir_agencia_mock.return_value = None
        admin()

    @patch('src.app_adm.inserir_agencia')
    @patch('src.app_adm.escolher_uma_opcao_do_menu_entrada')
    def test_app_adm_menu_ag_s( # pylint: disable=too-many-arguments
        self,
        escolher_uma_opcao_do_menu_entrada_mock,
        inserir_agencia_mock,
    ):
        '''
        Teste do fluxo principal - admin() 
        python -m unittest -v tests.test_app_adm.Test.test_app_adm_menu_ag_s -v
        '''
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = [
            'AG', 'S', 'SA'
        ]
        inserir_agencia_mock.return_value = None
        admin()
