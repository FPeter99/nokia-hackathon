from pathlib import Path

## str -> int
def hatvanyKezeles(num) -> int:
    if "^" in num:
        alap, kitevő = num.split("^")
        ertek = int(alap) ** int(kitevő)
        return int(ertek)
    return int(num)

## str -> bool
def kilencesek(num) -> bool:
    for i in range(len(num)):
        if num[i] != "9":
            return False
    return True


def main():
    
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    ## data = [str, str, ...]
    
    for elem in data:
        ## elem = "3^39"

        numInt = hatvanyKezeles(elem)
        ## numInt = 40525...

        numStr = str(numInt)
        ## numStr = "40525..."

        if kilencesek(numStr):
            print(numInt + 2)
            ## 99 -> 101 vagy 9 -> 11
            continue
    
        if len(numStr) % 2 == 0:
            ## páros hossz

            kozep = len(numStr) // 2 
            elsoFelStr = numStr[0:kozep]

            ##tükrözés
            magicNumStr = elsoFelStr + elsoFelStr[::-1]

            if int(magicNumStr) > numInt:
                ##megoldás
                print(magicNumStr)
            else: 
                elsoFelStr = str(int(elsoFelStr) + 1)
                magicNumStr = elsoFelStr + elsoFelStr[::-1]
                print(magicNumStr)

        else:

            hosszuKozep = len(numStr) // 2

            elejeStr = numStr[:hosszuKozep]
            kozepsoStr = numStr[hosszuKozep]

            magicNumStr = elejeStr + kozepsoStr + elejeStr[::-1]

            if int(magicNumStr) > numInt:
                print(magicNumStr)
            else:
                ##ha +1-el kibővítjük, minden esetben jót ad vissza
                bovitettElejeStr = str(int(elejeStr + kozepsoStr) + 1)

                elejeStr = bovitettElejeStr[:-1]
                kozepsoStr = bovitettElejeStr[-1]

                magicNumStr = elejeStr + kozepsoStr + elejeStr[::-1]

                print(magicNumStr)


if __name__ == "__main__":
    main()
