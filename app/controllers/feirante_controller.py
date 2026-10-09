from app.database import feirantes, reservas


def _para_dicionario(feirante):
    #Converte um objeto Feirante em dicionário.#
    return {
        "id": feirante.id,
        "nome": feirante.nome,
    }


def _reserva_para_dicionario(reserva):
    return {
        "id": reserva.id,
        "barraca_id": reserva.barraca.id,
        "feirante_id": reserva.feirante.id,
        "data": str(reserva.data),
        "ativa": reserva.ativa,
    }


def listar_feirantes():
    #Retorna a lista de todos os feirantes.#
    return [_para_dicionario(f) for f in feirantes]


def buscar_feirante_por_id(feirante_id):
    #Retorna o feirante como dicionário, ou None se não existir.#
    for feirante in feirantes:
        if feirante.id == feirante_id:
            return _para_dicionario(feirante)
    return None


def historico_reservas(feirante_id):
    #Retorna as reservas do feirante, ou None se o feirante não existir.#
    if buscar_feirante_por_id(feirante_id) is None:
        return None
    return [
        _reserva_para_dicionario(r)
        for r in reservas
        if r.feirante.id == feirante_id
    ]