lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add functions below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    # print total
    return total

# this function is calling the average() function above
# and processing an individual student's grades
# the student is being passed in down below on the last line
def get_average(student):
    homework = average(student['homework']) * .1
    quizzes = average(student['quizzes']) * .3
    tests = average(student['tests']) * .6

    return homework + quizzes + tests

# this function uses the result of the function above
# that result is passed into this function as an argument
# that call can be seen at the bottom of the page
def get_letter_grade(grade):
    message = "F"
    if grade > 89:
        message = "A"
    elif grade > 79:
        message = 'B'
    elif grade > 69:
        message = 'C'
    elif grade > 59:
        message = 'D'

    return message

# this function is calling get letter grade
# the argument is the output of get_average
# it's argument is a students name from above
print get_letter_grade(get_average(alice))


