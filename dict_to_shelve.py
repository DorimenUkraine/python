import shelve

university = shelve.open('university_file')

# university['schedules'] =  {
#         'monday_schedule': ['Math', 'English', 'System programming', 'Python'],
#         'tuesday_schedule': ['English', 'Foorball', 'HTML'],
#         'wednesday_schedule': ['Physics', 'System programming', 'Python'],
#         'thursday_schedule': ['Java', 'Python'],
#         'friday_schedule': ['Running', 'Math', 'System programming', 'Python']
#     }
#
# university['tutors'] = {
#        'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allkhverdov', 'Jane Smith']
#     }

# x = university['schedules']
# print(type(x))
print(university['schedules']['wednesday_schedule'])
print(university['tutors']['Math'])

university.close()





# university =  {
#     'schedules': {
#         'monday_schedule': ['Math', 'English', 'System programming', 'Python'],
#         'tuesday_schedule': ['English', 'Foorball', 'HTML'],
#         'wednesday_schedule': ['Physics', 'System programming', 'Python'],
#         'thursday_schedule': ['Java', 'Python'],
#         'friday_schedule': ['Running', 'Math', 'System programming', 'Python']
#     },
#
#     'tutors': {
#        'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allkhverdov', 'Jane Smith']
#     }
# }
#
# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['Math'])
#
