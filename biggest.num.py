#!/usr/bin/env python3
# Created by: Lloyd Najac
# Created on: Oct 2022
# This program picks ask the user to enter three numbers and 
# displays the biggest one.

def main():
    # ask the user for 3 random numbers
    first = input("Enter your first number:")
    second = input("Enter your second number:")
    third = input("Enter your third number:")
# Calculate biggest number and display it
    if first > second:
        if first > third:
            print("The biggest number is", first)
        else:
            print("Biggest number is", third)
    else:
        if second > third:
            print("Biggest number is", second)
        else:
            print("Biggest number is", third)


if __name__ == "__main__":
    main()
