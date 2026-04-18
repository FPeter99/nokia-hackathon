from pathlib import Path
from datetime import datetime, timedelta
import math

def parkoloOra(idotartam) -> int:

    if(idotartam <= timedelta(minutes=30)):
        return 0
    
    parkoltIdo = idotartam.total_seconds()

    parkoltNapok = parkoltIdo // 86400
    maradekIdo = parkoltIdo % 86400
    fizetendoIdoOraban = math.ceil((maradekIdo - 1800) / 3600)
    
    if maradekIdo <= 1800:
        return int(parkoltNapok * 10000)  

    if fizetendoIdoOraban <= 3:
        return int(parkoltNapok * 10000 + fizetendoIdoOraban * 300)

    return int(parkoltNapok * 10000 + 3 * 300 + (fizetendoIdoOraban - 3) * 500)
  
def main():
    data = Path("input.txt").read_text(encoding="utf-8")

    print(f"RENDSZAM\tDIJ")

    for sor in data.splitlines()[2:]:
        resz = sor.split()

        erkezes = datetime.strptime(resz[1] + " " + resz[2], "%Y-%m-%d %H:%M:%S")
        tavozas = datetime.strptime(resz[3] + " " + resz[4], "%Y-%m-%d %H:%M:%S")

        print(f"{resz[0]}\t\t{parkoloOra(tavozas - erkezes)}")


if __name__ == "__main__":
    main()
