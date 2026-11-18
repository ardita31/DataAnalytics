# LAB 5 

# Create a script that defines two variables for a student: 
# student_name and student_major. The student_major variable will 
# contain a code for the student’s major (e.g. ENG). 
# What should your program do if a major code is not included in the table? 
# Include an alternative to display <unknown> for the major name and nothing for location.

# Major Code    Name of Major      Department Office
# ---------------------------------------------------
# BIOL          Biology            Science Bldg, Room 310
# CSCI          Computer Science   Sheppard Hall, Room 314
# ENG           English            Kerr Hall, Room 201
# HIST          History            Kerr Hall, Room 114
# MKT           Marketing          Westly Hall, Room 310

student_name = (input('Enter your name: ')).title()
student_major = (input('Enter your major code: ')).strip().upper()

major_name = ''
location = ''

if student_major == 'BIOL':
    major_name = 'Biology'
    location ='Science Bldg, Room 310'
elif student_major == 'CSCI':
    major_name = 'Computer Science'
    location = 'Sheppard Hall, Room 314'
elif student_major == 'ENG':
    major_name = 'English'
    location = 'Kerr Hall, Room 201'
elif student_major == 'HIST':
    major_name = 'History'
    location = 'Kerr Hall, Room 114'
elif student_major == 'MKT':
    major_name = 'Marketing'
    location = 'Westly Hall, Room 310'
else : 
    print('ERROR: Invalid major code. Please re-enter.')

if major_name != '':
    print(f'Hello, {student_name}! Your major is {major_name}. Your class is at {location}.')

# Output with invalid major code: 
# Enter your name: arbER
# Enter your major code: data
# ERROR: Invalid major code. Please re-enter.

# Output with valid major code
# Enter your name: ArdITA
# Enter your major code: BIOL
# Hello, Ardita! Your major is Biology. Your class is at Science Bldg, Room 310.