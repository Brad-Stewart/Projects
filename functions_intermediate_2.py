# 1. UPDATE VALUES IN DICTIONARIES AND LISTS
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def update_values(x, students, sports_directory, z):
    # CHANGE THE VALUE 10 IN X TO BE 15
    x[1][0] = 15
    #CHANGE LAST NAME OF THE FIRST STUDENT
    students[0]['last_name'] = 'Bryant'

    sports_directory['soccer'][0] = 'Andres'

    z[0]['y'] = 30

update_values(x, students, sports_directory, z)

#2 ITERATE THROUGH A LIST OF DICTIONARIES
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(student): 
# LOOP THROUGH THE LIST
    print_string = ""
    for i in range(len(student)):
    # PRINT THE KEYS AND VALUES
        for key in student[i]:
            print_string += f"{key} - {student[i][key]}"
    print(print_string)
    print_string = ""
iterate_dictionary(students)


#3 GET VALUES FROM A LIST OF DICTIONARIES
def iterate_dictionary2(key_value, student):
    for i in range(len(student)):
        if key_value not in student[i]:
            print("Key is not in dictionary")
        else: 
            print(student[i][key_value])

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    #LOOP THROUGH THE DICTIONARY
    for key in some_dict:
        #PRINT LENGTH OF THE LIST AND THE KEY
        print(f"{len(some_dict[key])} {key.upper()}")
        #LOOP TO PRINT EACH ITEM IN THE LIST
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
print_info(dojo)

