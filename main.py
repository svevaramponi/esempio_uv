from src.operazioni import somma, generatore_num, media

def main():
    dati = generatore_num(8)
    totale = somma(dati)
    print(totale)
    mean = media(dati)
    print(mean)


if __name__ == "__main__":
    main()
