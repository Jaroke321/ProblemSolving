from multiprocessing.dummy import current_process


def longestPalindrome(s: str) -> list():

    length = len(s)
    start = 0
    end = start + length
    count = 1

    while(length > 1):

        for i in range(count):
            substring = s[start:end]
            if(isValid(substring)):
                return substring
            
            start += 1
            end += 1

        count += 1
        length -= 1
        start = 0
        end = start + length

    return s[0]

def isValid(s:str) -> bool:

    reversed = s[::-1]
    return s == reversed


def main():
    s1 = "babad"
    s2 = "cbbd"

    ans1 = longestPalindrome(s1)
    ans2 = longestPalindrome(s2)

    print(ans1)
    print(ans2)

if __name__ == "__main__":
    main()



    # 1 = 1
    # 2 = 1
    # 3 = 3
    # 4 = 6
    # 5 = 10