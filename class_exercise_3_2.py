# This script calculates and prints the grade based on a given CGPA score.
# It contains two functions:
# 1. computegrade(score): Takes a CGPA score as input and returns the corresponding grade.
#    - If the score is less than 0.0 or greater than 5.0, it returns an error message.
def computegrade(score):
    if score < 0.0 or score > 5.0:
        return "Error: CGPA score must be between 0.0 and 5.0"
    elif score >= 4.5:
        return "1st Class"
    elif score >= 3.5:
        return "2nd Class Upper"
    elif score >= 2.5:
        return "2nd Class Lower"
    elif score >= 1.5:
        return "3rd Class"
    else:
        return "Pass"

def main():
    try:
        score = float(input("Enter your CGPA score: "))
        
        grade = computegrade(score)
        print("Grade:", grade)
    except ValueError:
        print("Error: Please enter a numeric value for CGPA score.")

if __name__ == "__main__":
    main()
