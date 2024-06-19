__all__ = [ 'inicializar', 'finalizar', 'add_leciona', 'set_leciona', 'get_prof_by_turma', 'get_turmas_by_prof' ]

import json, atexit

# Leciona:
#   id_prof: int
#   id_turma: int

lecionamentos = []
PATH = 'data_leciona/leciona.json'

# Códigos de erro
OPERACAO_REALIZADA_COM_SUCESSO = 0

ARQUIVO_NAO_ENCONTRADO = 30
ARQUIVO_EM_FORMATO_INVALIDO = 31
ERRO_NA_ESCRITA_DO_ARQUIVO = 32

PROFESSOR_NAO_ENCONTRADO = 25
TURMA_NAO_ENCONTRADA = 24

LECIONA_JA_ADICIONADO = 23

def inicializar() -> int:
    global lecionamentos

    try:
        with open(PATH, 'r') as arquivo:
            try:
                lecionamentos = json.load(arquivo)
            except json.JSONDecodeError: return ARQUIVO_EM_FORMATO_INVALIDO
    except FileNotFoundError: return ARQUIVO_NAO_ENCONTRADO

    return OPERACAO_REALIZADA_COM_SUCESSO

def finalizar() -> int:
    try:
        with open(PATH, 'w') as arquivo:
            json.dump(obj = lecionamentos, fp = arquivo, indent = 4)
    except OSError: return ERRO_NA_ESCRITA_DO_ARQUIVO

    return OPERACAO_REALIZADA_COM_SUCESSO

def add_leciona(id_prof: int, id_turma: int) -> int:
    novo_lecionamento = { 'id_prof': id_prof, 'id_turma': id_turma }

    if novo_lecionamento in lecionamentos:
        return LECIONA_JA_ADICIONADO

    lecionamentos.append({ 'id_prof': id_prof, 'id_turma': id_turma, })
    return OPERACAO_REALIZADA_COM_SUCESSO

def set_leciona(id_prof: int, id_turma: int) -> int:
    for lecionamento in lecionamentos:
        if id_turma == lecionamento['id_turma']:
            lecionamento['id_prof'] = id_prof
            return OPERACAO_REALIZADA_COM_SUCESSO

    return TURMA_NAO_ENCONTRADA

def get_prof_by_turma(id_turma: int) -> tuple[int, int]:
    for lecionamento in lecionamentos:
        if lecionamento['id_turma'] == id_turma:
            return OPERACAO_REALIZADA_COM_SUCESSO, lecionamento['id_prof']

    return TURMA_NAO_ENCONTRADA, 0

def get_turmas_by_prof(id_prof: int) -> tuple[int, list[int]]:
    turmas = []

    for lecionamento in lecionamentos:
        if lecionamento['id_prof'] == id_prof:
            turmas.append(lecionamento['id_turma'])

    if len(turmas) == 0: return PROFESSOR_NAO_ENCONTRADO, turmas
    return OPERACAO_REALIZADA_COM_SUCESSO, turmas

inicializar()
atexit.register(finalizar)
