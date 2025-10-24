from log_parser import carregar_log
from race_results import gerar_resultado
from tabulate import tabulate

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

    # Exibe em formato tabular
    tabela = []
    for posicao, piloto in enumerate(resultados_ordenados, start=1):
        tabela.append([
            posicao,
            piloto["codigo"],
            piloto["nome"],
            piloto["voltas"],
            str(piloto["tempo_total"]),
        ])

    print("\n Resultado Final da Corrida \n")
    print(tabulate(
        tabela,
        headers=["Posição", "Código", "Nome", "Voltas", "Tempo Total"],
        tablefmt="grid"
    ))

if __name__ == "__main__":
    main()
