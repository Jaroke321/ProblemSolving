def reverse(x: int) -> int:
        
    if (x == 0):
        return 0
        
    upper = 2**31 - 1
    lower = (upper * -1) + 1
        
    abs_val = abs(x)
        
    val = int(str(abs_val)[::-1])
    val = val * (x / abs_val)
        
    if ((val < upper) and (val > lower)):
        return int(val)
    return 0

def main():
    n1 = 123
    n2 = -123
    n3 = 0

    a1 = reverse(n1)
    a2 = reverse(n2)
    a3 = reverse(n3)

    print(str(n1) + " -> " + str(a1))
    print(str(n2) + " -> " + str(a2))
    print(str(n3) + " -> " + str(a3))

if __name__ == "__main__":
    main()