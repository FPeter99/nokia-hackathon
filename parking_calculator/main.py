from pathlib import Path

## jegyzet:
## https://1drv.ms/o/c/480e2e0e80cfc5ea/IgA4bsiHLfKbTbkQss2gFZI6AdVfVKziCJIUlc40HisytnI

def F(Z, H) -> int:
    ## Z -> eszköz db, H -> magasság
    if Z == 1:
        return H ## -> lépés = magasság
    
    ossz = 0
    # F{Z}(H) = F{Z-1}(1) + ... + F{Z-1}(H-1) + F{Z-1}(H) 
    #                 i=1                i=2          i=n
    for i in range(1, H + 1):
        ossz += F(Z - 1, i)
    return ossz

def min_num_of_drops(Z, H) -> int:
    n = 1
    while F(Z, n) < H:
        n += 1
    return n
    
def main():
    
    data = Path("input.txt").read_text(encoding="utf-8")

    for elem in data.splitlines():
        
        Z, H = elem.split(", ")

        n = min_num_of_drops(int(Z), int(H))

        print(n)



if __name__ == "__main__":
    main()
