from audioop import reverse


def isPalindrome(x: int) -> bool:

    a = str(x)
    r_a = a[::-1]
    return (a == r_a)


def main():
    x = 121
    a = 1221
    y = -121
    z = 93028

    print(isPalindrome(x))
    print(isPalindrome(y))
    print(isPalindrome(z))
    print(isPalindrome(a))


if __name__ == "__main__":
    main()