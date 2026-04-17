from pathlib import Path

def F(db, magassag) -> int:

    if db == 1:
        return magassag ## lépés = magasság
    if magassag == 0:
        return 0
    
    return F(db - 1, magassag - 1) + F(db, magassag - 1) + 1

def min_num_of_drops(Z, H) -> int:
    n = 1
    while F(Z, n) < H:
        n += 1
    return n
    
def main():
    
    data = Path("input.txt").read_text(encoding="utf-8")

    for elem in data.splitlines():

        N, H = elem.split(", ")

        x = 0
        
        while F(int(N), int(x)) < int(H):
            x += 1

        print(x)



if __name__ == "__main__":
    main()
