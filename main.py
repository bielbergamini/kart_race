from log_parser import carregar_log

def main():
    voltas = carregar_log("race.log")

    # msotra os 3 primeiros resultados para conferir novas funcionalidades
    for v in voltas[:3]:
        print(v)

if __name__ == "__main__":
    main()
