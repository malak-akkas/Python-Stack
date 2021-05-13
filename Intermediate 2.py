x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
# 1
x[1][0] = 15
print(x)
# 2
students[0]['last_name'] = 'Bryant'
print(students)

# 3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# 4

z[0]['y'] = 30
print(z)
print("_" * 30)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for student in students:
        for key, value in student.items():
            print(f"{key} - {value}", end=",")
            print("")

    # for student in students:

    #     print(
    #         f"first name - {student['first_name']}, last name - {student ['last_name']}")


def iterateDictionary2(key_name, students):
    for student in students:
        print(student[key_name])

# def iterateDictionary2(key_name, other_list):
#     for student in other_list:
#         print(student[key_name])


iterateDictionary2('first_name', students)

# Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    for key, Values in dojo.items:
        length = len(Values)
        key_Upper = key.upper()
        print(f"{key} - {value}")
        for value in values:

            print(value)


printInfo(dojo)
