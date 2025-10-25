# 🏎️ Observações do Desafio – Corrida de Kart | Grupo CRIAR

## Comentários Gerais

- Projeto desenvolvido em **Python 3.10+**, com foco em clareza, tipagem explícita e boas práticas.
- Utilização de `@dataclass(frozen=True)` para garantir **imutabilidade** dos dados da corrida.
- Todas as funções possuem **responsabilidade única** e **tipagem declarada** (`List`, `Dict`, `timedelta`).
- Todos os bônus opcionais foram implementados.
- O código foi estruturado em módulos independentes para facilitar leitura e manutenção:
  - `log_parser.py` → leitura e parsing do log
  - `race_results.py` → cálculos e regras de negócio
  - `main.py` → ponto de execução principal

## Decisões Técnicas

- A leitura do log é feita via **expressões regulares**, garantindo robustez e compatibilidade com variações de espaçamento.
- O tempo das voltas é tratado com `datetime.timedelta` para evitar erros de conversão e permitir operações aritméticas diretas.
- O cálculo da **velocidade média total por piloto** considera todas as voltas completadas, representando a média geral de desempenho durante a corrida.
- O uso da biblioteca **pandas** foi evitado propositalmente para manter o projeto **leve e independente de dependências externas**, já que o volume de dados é pequeno e pode ser manipulado de forma eficiente apenas com estruturas nativas do Python.

---

**Autor:** Gabriel Bergamini
