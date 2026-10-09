from app.database import barracas
 
 
def _para_dicionario(barraca):
    #Converte um objeto Barraca em dicionário.#
    return {
        "id": barraca.id,
        "nome": barraca.nome,
        "taxa_diaria": barraca.taxa_diaria,
        "disponivel": barraca.disponivel,
    }
 
 
def listar_barracas():
    #Retorna a lista de todas as barracas.#
    return [_para_dicionario(b) for b in barracas]
 
 
def buscar_barraca_por_id(barraca_id):
    #Retorna a barraca como dicionário, ou None se não existir.#
    for barraca in barracas:
        if barraca.id == barraca_id:
            return _para_dicionario(barraca)
    return None
 
 
def listar_barracas_disponiveis():
    #Retorna somente as barracas disponíveis (list comprehension).#
    return [_para_dicionario(b) for b in barracas if b.disponivel]
 