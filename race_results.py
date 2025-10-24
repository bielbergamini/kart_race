from datetime import timedelta
from typing import List, Dict
from log_parser import Volta


def gerar_resultado(voltas: List[Volta]) -> List[Dict]:

    # Agrupar voltas por piloto.
    agrupado_por_piloto: Dict[str, List[Volta]] = {}

    for v in voltas:
        if v.codigo not in agrupado_por_piloto:
            agrupado_por_piloto[v.codigo] = []
        agrupado_por_piloto[v.codigo].append(v)

    # Para cada piloto, calcular o resumo.
    tabela_resumo: List[Dict] = []

    for codigo_piloto, voltas_piloto in agrupado_por_piloto.items():
        nome_piloto = voltas_piloto[0].nome

        voltas_completadas = len(voltas_piloto)

        tempo_total = timedelta()
        for volta in voltas_piloto:
            tempo_total += volta.tempo_volta

        resumo_piloto = {
            "codigo": codigo_piloto,
            "nome": nome_piloto,
            "voltas": voltas_completadas,
            "tempo_total": tempo_total,
        }
        
        tabela_resumo.append(resumo_piloto)

    return tabela_resumo
