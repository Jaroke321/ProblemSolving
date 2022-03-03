import math


def permutate(s):

    final_list = []

    # Represent the digits from the problem, These are different than the ones from the original problem
    f0 = []
    f1 = ["q", "a"]
    f2 = ["z"]
    f3 = ["w", "e", "s", "x", "c"]
    f4 = ["d", "f", "v", "g"]
    f5 = []
    f6 = ["h", "y", "t", "j", "u"]
    f7 = ["i", "k", "b", "n"]
    f8 = ["l", "o", "p", "m"] 
    f9 = ["r"]

    all_list = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9]

    # Get all of the relevant digits
    digits = [ int(v) for v in s if v not in ["0", "5"] ]
    
    rel_list = [ all_list[i] for i in digits ] # Get only the relevant lists

    # Calculate the total number of strings that the result will have
    total_strings = math.prod([ len(l) for l in rel_list ])
    #print("total_strings: " + str(total_strings))

    new_lists = []  # Holds the final lists to create the final strings

    # Cycle through every digit list except the last (Done seperately)
    for i in range(len(rel_list)-1):
        rel_l = rel_list[i]
        pattern_val = math.prod([ len(l) for l in rel_list[i+1:] ])            # Product of the lengths of the lists to the right of the current list
        tmp_substring = ""                                                     # Holds the first iteration of the pattern

        # Cycle through each character in the current digit list
        for c in rel_l:
            tmp_substring += (c * pattern_val)                                 # Get the correct number of characters according to pattern val

        final_string = tmp_substring * (total_strings // len(tmp_substring))   # Each pattern repeats until the total is reached
        expanded = [ s for s in final_string ]                                 # Expand into a list and add to the new lists, represents a column to the output
        new_lists.append(expanded)
        

    # Manually do the last list
    tmp_string = "".join(rel_list[-1])
    multiples = total_strings // len(tmp_string)
    expanded = tmp_string * multiples
    expanded_list = [ s for s in expanded ]
    new_lists.append(expanded_list)

    # Create the output by combining the lists on there columns
    for col in range(total_strings):
        tmp_output = ""
        for row in new_lists:
            tmp_output += row[col]

        final_list.append(tmp_output)

    return final_list


def main():

    s1 = "98013" # Example digits

    # Used to check for unique values at the end
    check_dict = {}

    f1 = permutate(s1) # Perform the permutation. (IDK if its actually called a permutation technically, but its related)
    
    # Put each value into the dictionary
    for i, f in enumerate(f1):
        print(str(i) + ": " + f)
        check_dict[f] = check_dict.setdefault(f, 0) + 1

    # Spaces
    print()
    print()

    # Check for repeats
    for k, v in check_dict.items():
        print(k + " <-> " + str(v))

if __name__ == "__main__": 
    main()