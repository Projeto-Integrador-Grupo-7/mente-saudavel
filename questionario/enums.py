from enum import Enum

class Estratificacao(Enum):
    NAO_IDENTIFICADO = 0
    SOFRIMENTO_LEVE = 1
    SOFRIMENTO_MODERADO = 2
    SOFRIMENTO_GRAVE = 3

    @property
    def nome_formatado(self):
        return self.name.replace('_', ' ').title()