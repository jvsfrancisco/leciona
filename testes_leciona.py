import unittest
from leciona import *

# Códigos de erro
OPERACAO_REALIZADA_COM_SUCESSO = 0

ARQUIVO_NAO_ENCONTRADO = 30
ARQUIVO_EM_FORMATO_INVALIDO = 31
ERRO_NA_ESCRITA_DO_ARQUIVO = 32

PROFESSOR_NAO_ENCONTRADO = 25
TURMA_NAO_ENCONTRADA = 24

LECIONA_JA_ADICIONADO = 23

class TestesFuncoesLeciona(unittest.TestCase):
    def teste_add_leciona(self):
        resultado = add_leciona(1, 2)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)

    def teste_add_leciona_leciona_ja_adicionado(self):
        add_leciona(1, 2)
        resultado = add_leciona(1, 2)
        self.assertEqual(resultado, LECIONA_JA_ADICIONADO)

    def teste_get_prof_by_turma(self):
        add_leciona(1, 2)
        resultado, id_prof = get_prof_by_turma(2)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertEqual(id_prof, 1)

    def teste_get_prof_by_turma_turma_nao_encontrada(self):
        resultado, id_prof = get_prof_by_turma(-1)
        self.assertEqual(resultado, TURMA_NAO_ENCONTRADA)

    def teste_get_turmas_by_prof(self):
        add_leciona(1, 2)
        add_leciona(1, 3)
        resultado = get_turmas_by_prof(1)
        self.assertEqual(resultado, (OPERACAO_REALIZADA_COM_SUCESSO, [2, 3]))

    def teste_set_leciona(self):
        resultado = set_leciona(2, 2)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertEqual(get_prof_by_turma(2), (OPERACAO_REALIZADA_COM_SUCESSO, 2))

    def teste_set_leciona_turma_nao_encontrada(self):
        resultado = set_leciona(1, -1)
        self.assertEqual(resultado, TURMA_NAO_ENCONTRADA)

if __name__ == '__main__':
    unittest.main()
