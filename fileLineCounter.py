import os
import sys

def countTotalLines():
    '''This function will count all of the lines in each of the files in the current directory.
    Returns nothing, all results will be printed to the console.'''

    totalLines = {}     # Holds the line counts for all files

    longestFile = ""    # Holds the name of the longest file in the directory
    shortestFile = ""   # Holds the name of the shortest file in the directory
    directory = os.getcwd()
    min_count = sys.maxsize
    max_count = 0
    count = 0
    fileCount = 0

    # Cycle through each file in the directory
    for filename in os.listdir(directory):
        
        # Open the file given the filename
        with open(filename, 'r') as f:

            currentTotal = len(f.readlines())        # Get the line count for the current file
            totalLines[filename] = currentTotal      # Add to the dictionary with the filename

    # Update all of the values
    for k, v in totalLines.items():
        count += v
        fileCount += 1
        if(v > max_count):
            longestFile = k
            max_count = v

        if (v < min_count):
            shortestFile = k
            min_count = v

    # Print all of the values
    print("\nInformation for the current directory: " + directory)
    print("Number of files: " + str(fileCount))
    print("Total Lines of code: " + str(count))
    print("Longest File is " + longestFile + " with " + str(max_count) + " lines of code.")
    print("Shortest File is " + shortestFile + " with " + str(min_count) + " lines of code")
        


def main():
   
    countTotalLines()


if __name__ == "__main__":
    main()