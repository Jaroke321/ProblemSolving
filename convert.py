def convert(s: str, rows: int):
    
    string_arr = [ [] for i in range(rows) ]

    idx = 0                 # Holds current array position
    isIncreasing = True     # Determines the direction of the idx

    # Cycle through each of the characters
    for c in s:
        string_arr[idx].append(c)

        # Increment of decrement idx accordingly
        if(isIncreasing and (idx < rows-1)):
            idx += 1
        elif((not isIncreasing) and (idx > 0)):
            idx -= 1
        else:
            isIncreasing = not isIncreasing
            if(isIncreasing):
                idx += 1
            else:
                idx -= 1

    # Compile final string with arrays
    final_string = ""
    for s in string_arr:
        tmp = "".join(s)
        final_string += tmp

    # Return the finalized string
    return final_string



def main():
    s = "PAYPALISHIRING"
    expected = "PAHNAPLSIIGYIR"

    converted = convert(s, 3)

    print(converted)
    print(expected)


if __name__ == "__main__":
    main()