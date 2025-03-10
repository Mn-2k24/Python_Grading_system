# Grading System based on user Marks in Python

# user input
user_marks = int(input("Enter your marks: "))

# Checking if the marks are within the range of 0 to 100    
if (user_marks < 0 or user_marks > 100):
    print("Invalid input! Please enter a valid integer between 0 and 100.")
    exit()

# Grading system based on marks
if (user_marks >= 80):
    grade = "Excellent,You got A+"
elif (user_marks >= 70):
    grade = "Good, You got A"
elif (user_marks >= 60):
    grade = "Satisfactory, You got B"
elif (user_marks >= 50):
    grade = "Below Average, You got C"
elif (user_marks >= 33):
    grade = "Pass, You got D"
elif (user_marks < 33):
    grade = "opps!, You are Fail"
else:
    grade = "Invalid input! Please enter a valid integer."

# Printing the grade
print(grade)
