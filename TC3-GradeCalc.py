# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.

#Student Name:  Mathew Akunyili

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # dDeclare variables
    modify = 0.3

    print("Grade Point Calculator")
    print("")
    print("Valid letter grades that can be entered: A, B, C, D, F")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.")
    print("")
    grade = input("Please enter a letter grade: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing): ")
    if grade == "A" and modifier == "+":
        numericvalue = 4.0
        print("The numeric value is:",numericvalue)
    elif grade == "A" and modifier == "":
        numericvalue = 4.0
        print("The numeric value is:",numericvalue)
    elif grade == "A" and modifier == "-":
        numericvalue = 4.0 - modify
        print("The numeric value is:",numericvalue)
    elif grade == "B" and modifier == "+":
        numericvalue = 3.0 + modify
        print("The numeric value is:",numericvalue)
    elif grade == "B" and modifier == "":
        numericvalue = 3.0
        print("The numeric value is:",numericvalue)
    elif grade == "B" and modifier == "-":
        numericvalue = 3.0 - modify
        print("The numeric value is:",numericvalue)
    elif grade == "C" and modifier == "+":
        numericvalue = 2.0 + modify
        print("The numeric value is:",numericvalue)
    elif grade == "C" and modifier == "":
        numericvalue = 2.0
        print("The numeric value is:",numericvalue)
    elif grade == "C" and modifier == "-":
        numericvalue = 2.0 - modify
        print("The numeric value is:",numericvalue)
    elif grade == "D" and modifier == "+":
        numericvalue = 1.0 + modify
        print("The numeric value is:",numericvalue)
    elif grade == "D" and modifier == "":
        numericvalue = 1.0
        print("The numeric value is:",numericvalue)
    elif grade == "D" and modifier == "-":
        numericvalue = 1.0 - modify
        print("The numeric value is:",numericvalue)
    elif grade == "F" and modifier == "":
        numericvalue = 0
        print("The numeric value is:",numericvalue)
    else:
        print("You entered an invalid letter grade")
    

    
    









    # YOUR CODE ENDS HERE

main()
