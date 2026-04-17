from pathlib import Path
from datetime import datetime, timedelta
import math

def parkoloOra(idotartam) -> int:

    if(idotartam <= timedelta(minutes=30)):
        return 0
    
    fizetendoIdoOraban = math.ceil((idotartam.total_seconds() - 1800) / 3600)

    if fizetendoIdoOraban <= 3:
        return fizetendoIdoOraban * 300

    if idotartam < timedelta(days=1):
        return 3 * 300 + (fizetendoIdoOraban - 3) * 500
    else: ## több mint 1 nap, ezért minden megkezdett óra + 500 forint mert régebb óta prakol mint 3 óra
        return idotartam.days * 10000 + math.ceil(((idotartam.total_seconds() % 86400) - 1800) / 3600) * 500

  
def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    for sor in data.splitlines()[2:]:
        resz = sor.split()

        erkezes = datetime.strptime(resz[1] + " " + resz[2], "%Y-%m-%d %H:%M:%S")
        tavozas = datetime.strptime(resz[3] + " " + resz[4], "%Y-%m-%d %H:%M:%S")

        print(f"{resz[0]}: {parkoloOra(tavozas - erkezes)}")


if __name__ == "__main__":
    main()
