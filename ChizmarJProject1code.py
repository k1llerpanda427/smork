#Program by Jacob Chizmar
#This program will tell the user how many hours they should study based on what grade they want and how many credits they are taking, it will also average the credits and study hours of all users and keep track of the total number of students
#Last modified September 24, 2019

runAgain = 'Y'

while runAgain == 'Y' or runAgain == 'y':

    #str
    null = ''
    userName = ""
    runAgain = 'Y'
    userGradeapprox = ''


    #int
    initialStudent = 0
    userGradewant = 0
    userCredits = 0
    userHoursweekly = 0
    totalStudents = 0
    totalStudyhours = 0
    totalCredits = 0
    averageCredits = 0
    averageStudyhours = 0
    userClass = 0
    userGrade = 0

    #constant
    CREDITAMOUNT = 3




    #welcome screen for the user to read while the code loads
    print('This program will tell you how many hours you should study based on what grade you want and how many credits you are taking. It will also average the credits and study hours of all users and keep track of the total number of students. Created by Jacob Chizmar')

    #asks user for first and last name
    userName = input(str('Please enter your first and last name such as Jacob Chizmar: \n'))
    #validate that the user actually entered a username
    while userName is null:
        userName = input(str('The value you input is not acceptable. Please enter a valid first and last name such as Jacob chizmar: \n'))
    #ask the user to enter the grade they want
    userGradewant = str(input('Please enter the grade you want, assuming the same grade for all classes, such as A, B, C, D, or F: \n'))
    #printing out their grade and also setting the values equal to the number of study hours required to get that grade
    if userGradewant == 'A':
        print('The grade you would like is an A')
        userGradewant = int(15)
        userGrade = str('A')
        
    elif userGradewant == 'B':
        print('The grade you would like is a B')
        userGradewant = int(12)
        userGrade = str('B')
    elif userGradewant == 'C':
        print('the grade you would like is a C')
        userGradewant = int(9)
        userGrade = str('C')
    elif userGradewant == 'D':
        print('The grade you would like is a D')
        userGradewant = int(6)
        userGrade = str('D')
    elif userGradewant == 'F':
        print('The grade you would like is an F')
        userGradewant = int(0)
        userGrade = str('F')
    else:
        while userGradewant is null:
            userGradewant = str(input('The grade you entered is not a real grade,please enter a real grade, such as A, B, C, D, or F: \n'))
            
    #asking the user for the number of credits they are taking
    userCredits = int(input('Please enter the number of credits you are taking, such as 15, 12, 9, 6, or 0: \n'))
    #verifying that they do not enter a number less than 0
    if userCredits <0:
        userCredits = int(input('The value you entered is not a legitimate amount of credits. Please enter the number of credits you are taking, such as 15, 12, 9, 6, or 0: \n'))
        
        
    #calculations
    userClass = userCredits / CREDITAMOUNT
    userHoursweekly = userGradewant * userClass
    
    #printing out their results
    print('Name:', userName, '\nCredits:', userCredits, '\nStudy Hours:', userHoursweekly, '\nGrade:', userGrade,'')

    #calculations
    totalStudent = initialStudent + 1
    totalCredits += userCredits
    totalStudyhours += userHoursweekly
    averageCredits = totalCredits / totalStudent
    averageStudyhours = totalStudyhours / totalStudent

    runAgain = input('Would you like to use this program again? If so, enter Y, if not, enter any other key: \n')

    
    

    print('Total Students:', totalStudent, '\nAverage Credits:', averageCredits ,'\nAverage Study Hours:', averageStudyhours,'')

    

    


        





    









    



