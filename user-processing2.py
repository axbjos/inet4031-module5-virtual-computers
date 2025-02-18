#!/usr/bin/python3

import sys

def main():
  
    #ask the user to proceed
    answer = input("\nDo you want to print out the list of users? (Y or N)")

    if answer == "Y" or answer == "y":

        for line in sys.stdin:

            print(line)

    else:

        print("\nOk not printing, ending program.")

    print("\nEnd of User Processing\n")    


if __name__ == '__main__':
    main()
