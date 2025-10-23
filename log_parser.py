from dataclasses import dataclass
from datetime import timedelta
import re


@dataclass(frozen=True)
class Volta:
    hora: str
    codigo: str
    nome: str
    numero_volta: int
    tempo_volta: timedelta
    velocidade_media: float


def carregar_log(caminho: str) -> list[Volta]:
    voltas = []

    padrao = re.compile(
        r"(\d{2}:\d{2}:\d{2}\.\d{3})\s+(\d{3})\s+-\s+([A-Z]\.[A-Z]+)\s+(\d+)\s+(\d+:\d+\.\d+)\s+([\d,]+)"
    )

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip().replace("–", "-")
            match = padrao.match(linha)
            if match:
                hora, codigo, nome, volta, tempo, velocidade = match.groups()

                # Conversões de tipo
                minuto, segundos = tempo.split(":")
                segundos = float(segundos)
                tempo_volta = timedelta(minutes=int(minuto), seconds=segundos)
                velocidade_media = float(velocidade.replace(",", "."))
                numero_volta = int(volta)

                # Retorna os valores processados para o objeto
                volta_obj = Volta(
                    hora=hora,
                    codigo=codigo,
                    nome=nome,
                    numero_volta=numero_volta,
                    tempo_volta=tempo_volta,
                    velocidade_media=velocidade_media,
                )

                voltas.append(volta_obj)

    return voltas
