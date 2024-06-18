# Task 1: Code a function to calculate the average grade.
# Task 2: Implement a function to find the highest and lowest grade.
# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

grades = [90, 100, 20, 37, 39, 78]

def class_grades():
    print("The average grade is: ", average_grade(grades))
    print("The highest grade is: ", highest_grade(grades))
    print("The lowest grade is: ", lowest_grade(grades))
    print("The letter grades for the class are:", ", ".join(letter_grade(grade) for grade in grades))
    
def average_grade(grades):
    return sum(grades) / len(grades)

def highest_grade(grades):
    return max(grades)

def lowest_grade(grades):
    return min(grades)

def letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"  

class_grades()