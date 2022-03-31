# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# #print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again."

# #print(programming_dictionary)

# empty_list = []
# empty_dictionary = {}

# #Wipe a dictionary
# #programming_dictionary = {}

# #Edit a dictionary
# #programming_dictionary["Bug"] = "A moth in computer"

# #Loop through dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#-------------------------------------------#

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#     numGrade = student_scores[student]
#     grade = ''
#     if numGrade < 70:
#         grade = 'Fail'
#     elif numGrade < 80:
#         grade  = 'Acceptable'
#     elif numGrade < 90:
#         grade = 'Exceeds expectations'
#     else:
#         grade = 'Outstanding'
    
#     student_grades[student] = grade
# print(student_grades)
#-------------------------------------------#

# #nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# #nest list in dictionary
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# #nest dict in dictionary
# travel_log = {
#     "France" : {'cities visited' : ['Paris', 'Lille', 'Dijon'], 'total_visits' : 12},
#     "Germany": {'cities visited' : ["Berlin", "Hamburg", "Stuttgart"], 'total_visits' : 5},
# }
# print(travel_log)

# #nest dict in list
# travel_log = [
#     {
#      'country' : 'France',
#      'cities visited' : ['Paris', 'Lille', 'Dijon'],
#      'total_visits' : 12
#     },
#     {
#      'country' : 'Germany',
#      'cities visited' : ['Berlin', "Hamburg", "Stuttgart"],
#      'total_visits' : 5
#     },
# ]
#----------------------------------#

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    travel_log.append(
        {
            'country' : country,
            'visits' : visits,
            'cities' : cities,
        }
    )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])