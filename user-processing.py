# INET4031 Module 5
#
# User List Processing Program (simplified)
#
# Created: Nov 11, 2024
# Updated: Feb 10, 2025
#

def main():

    userFile = open("user-list.txt", "r")

    #load the lines of the file into a list
    listOfUsers = userFile.readlines()
  
    for userline in listOfUsers:

        print(userline)

main()
