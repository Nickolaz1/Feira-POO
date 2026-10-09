from app.database import barracas, feirantes, reservas
from app.models.reserva import Reserva

LIMITE_RESERVAS = 3


def _para_dicionario(reserva):
    #Converte um objeto Reserva em dicionário.#
    return {
        "id": reserva.id,
        "barraca_id": reserva.barraca.id,
        "feirante_id": reserva.feirante.id,
        "data": str(reserva.data),
        "ativa": reserva.ativa,
        "taxa_diaria": reserva.barraca.taxa_diaria,
    }


def _buscar_barraca(barraca_id):
    return next((b for b in barracas if b.id == barraca_id), None)


def _buscar_feirante(feirante_id):
    return next((f for f in feirantes if f.id == feirante_id), None)


def registrar_reserva(barraca_id, feirante_id, data):
    """
    Registra uma reserva.
    Retorna o dicionário da reserva criada, ou None se barraca/feirante
    não existirem. Lança ValueError se violar uma regra de negócio.
    """
    barraca = _buscar_barraca(barraca_id)
    feirante = _buscar_feirante(feirante_id)
    if barraca is None or feirante is None:
        return None

    if any(r.ativa and r.barraca.id == barraca_id and r.data == data
           for r in reservas):
        raise ValueError("Barraca já reservada nesta data.")

    total_feirante = len([r for r in reservas
                          if r.ativa and r.feirante.id == feirante_id])
    if total_feirante >= LIMITE_RESERVAS:
        raise ValueError(
            f"Feirante atingiu o limite de {LIMITE_RESERVAS} reservas."
        )

    nova = Reserva(len(reservas) + 1, barraca, feirante, data)
    reservas.append(nova)
    return _para_dicionario(nova)


def calcular_faturamento_total():
    #Soma a taxa diária de todas as reservas ativas.#
    return sum(r.barraca.taxa_diaria for r in reservas if r.ativa)