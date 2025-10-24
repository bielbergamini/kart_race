from log_parser import carregar_log
from race_results import (
    gerar_resultado,
    melhor_volta_por_piloto,
    melhor_volta_geral,
    diferenca_para_vencedor
)
from tabulate import tabulate

# Separa visalmente a saída no terminal e evita repetição de prints no código
def print_titulo(titulo: str):
    print("=" * 70)
    print(f"{titulo}".center(70))
    print("=" * 70)


def main():
    # Lê o log e cria os objetos Volta
    voltas = carregar_log("race.log")
    print(f"Total de voltas processadas: {len(voltas)}")

    # Gera o resultado consolidado (por piloto)
    resultados = gerar_resultado(voltas)
    
    # Filtra apenas quem completou as 4 voltas
    resultados_filtrados = [r for r in resultados if r["voltas"] == 4]

    # Ordena os pilotos por tempo total
    resultados_ordenados = sorted(resultados_filtrados, key=lambda x: x["tempo_total"])

    # Gera o resultado com diferença de tempo para o vencedor 
    resultados_com_diferenca = diferenca_para_vencedor(resultados_ordenados)

    # Gera a melhor volta de cada piloto
    melhores = melhor_volta_por_piloto(voltas)

    # Gera a melhor volta de toda a corrida
    melhor = melhor_volta_geral(voltas)

    
    print_titulo("Resultado Final da Corrida")

    tabela = []
    for posicao, piloto in enumerate(resultados_com_diferenca, start=1):
        tabela.append([
            posicao,
            piloto["codigo"],
            piloto["nome"],
            piloto["voltas"],
            str(piloto["tempo_total"]),
            str(piloto["diferenca_vencedor"]),
            f"{piloto['velocidade_media_total']:.3f}",
        ])

    # Exibe em formato tabular
    print(tabulate(
        tabela,
        headers=[
            "Posição",
            "Código",
            "Nome",
            "Voltas",
            "Tempo Total",
            "Diferença p/ Vencedor",
            "Velocidade Média (km/h)",
        ],
        tablefmt="grid"
    ))

    # Exibe a melhor volta de cada piloto
    print_titulo("Melhor volta de cada piloto")
    for codigo, volta in melhores.items():
        print(f"{codigo} - {volta.nome}: {volta.tempo_volta}")

    # Exibe a melhor volta geral
    print_titulo("Melhor volta da corrida")
    print(f"Melhor volta geral: {melhor.nome} - {melhor.tempo_volta} (Volta {melhor.numero_volta})")


if __name__ == "__main__":
    main()