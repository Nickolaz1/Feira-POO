from app.data.feirante_mock import FEIRANTES


class Feirante:
    LIMITE_RESERVAS = 2

    def __init__(self, id, nome, documento, telefone):
        self._id = id
        self.alterar_nome(nome)
        self.alterar_documento(documento)
        self.alterar_telefone(telefone)

    # --- Leitura ---
    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def mostrar_documento(self):
        return self._documento

    def mostrar_telefone(self):
        return self._telefone

    # --- Alteração e Validação ---
    def alterar_nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("Nome do feirante não pode ser vazio.")
        self._nome = novo_nome.strip()

    def alterar_documento(self, novo_documento):
        if not isinstance(novo_documento, str):
            raise ValueError("Documento deve ser uma string.")
        doc_limpo = novo_documento.strip()
        if not doc_limpo.isdigit() or len(doc_limpo) not in (11, 14):
            raise ValueError("Documento deve ter exatamente 11 (CPF) ou 14 (CNPJ) dígitos numéricos.")
        self._documento = doc_limpo

    def alterar_telefone(self, novo_telefone):
        if not isinstance(novo_telefone, str) or not novo_telefone.strip():
            raise ValueError("Telefone do feirante não pode ser vazio.")
        self._telefone = novo_telefone.strip()

    def __repr__(self):
        return f"Feirante({self._nome})"


def carregar_feirantes():
    return [
        Feirante(
            f["id"],
            f["nome"],
            f["documento"],
            f["telefone"]
        )
        for f in FEIRANTES
    ]
