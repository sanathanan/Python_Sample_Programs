"""
Given different scored marks of students. We need to find grades.
The test score is an average of the respective marks scored in assignments, tests and lab-works.
The final test score is assigned using below formula.

10 % of marks scored from submission of Assignments
70 % of marks scored from Test
20 % of marks scored in Lab-Works

Grade will be calculated according to :

1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"

Also, calculate the total class average and letter grade of class.
"""

"""
Average Calculation
"""
def get_average(lst):
    total_lst = sum(lst)
    total_lst = float(total_lst)
    avg = total_lst / len(lst)
    return avg

"""
Calculating average for individual topics
"""
def average_Marks(assignment, test, lab):
    avg_assignment = get_average(assignment)
    avg_test = get_average(test)
    avg_lab = get_average(lab)
    result = (0.1*avg_assignment) + (0.7*avg_test) + (0.2*avg_lab)
    return result

"""
Student Score Calculation
"""
def student_grade(score):
    if score >= 90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'E'


"""
Driver Code --- Starts
"""
# 1. Jack's dictionary
jack = { "name":"Jack Frost",
        "assignment" : [80, 50, 40, 20],
        "test" : [75, 75],
        "lab" : [78.20, 77.20]}

# 2. James's dictionary
james = { "name":"James Potter",
        "assignment" : [82, 56, 44, 30],
        "test" : [80, 80],
        "lab" : [67.90, 78.72]}

# 3. Dylan's dictionary
dylan = { "name" : "Dylan Rhodes",
        "assignment" : [77, 82, 23, 39],
        "test" : [78, 77],
        "lab" : [80, 80]}

# 4. Jessica's dictionary
jess = { "name" : "Jessica Stone",
        "assignment" : [67, 55, 77, 21],
        "test" : [40, 50],
        "lab" : [69, 44.56]}

# 5. Tom's dictionary
tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]}

student_Name = [jack, james, dylan, jess, tom]

class_avg = []
for i in student_Name:
    print(i['name'])
    print("-----------------------------------")
    print("Average marks of", i['name'], 'is :', (average_Marks(i['assignment'], i['test'], i['lab'])))
    print("Letter Grade of", i['name'], 'is: ', (student_grade((average_Marks(i['assignment'], i['test'], i['lab'])))), end ='\n \n')
    class_avg.append((average_Marks(i['assignment'], i['test'], i['lab'])))

average_class = get_average(class_avg)
print("Class Average is: ", average_class)

class_Grade = student_grade(average_class)
print("Letter Grade of the Class is: ", class_Grade)

"""
Driver Code --- Ends
"""


