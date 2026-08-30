# Define a function to calculate and print the grade based on the CGPA score
def calculate_grade(score):
    if score < 0.0 or score > 5.0:
        print("Error: CGPA score must be between 0.0 and 5.0")
    elif score >= 4.5:
        print("Grade: 1st Class")
    elif score >= 3.5:
        print("Grade: 2nd Class Upper")
    elif score >= 2.5:
        print("Grade: 2nd Class Lower")
    elif score >= 1.5:
        print("Grade: 3rd Class")
    else:
        print("Grade: Pass")

def main():
    try:
        score = float(input("Enter your CGPA score: "))
        
        calculate_grade(score)
    except ValueError:
        print("Error: Please enter a numeric value for CGPA score.")

if __name__ == "__main__":
    main()
