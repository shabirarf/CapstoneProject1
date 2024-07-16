# Dictionary
from tabulate import tabulate

studentGrades = [{"Name" : "Anya", "Math" : 95, "Science" : 90, "Indonesian" : 75, "English" : 88},
                 {"Name" : "Aditya", "Math" : 98, "Science" : 85, "Indonesian" : 77, "English" : 75},
                 {"Name" : "Arsen", "Math" : 90, "Science" : 82, "Indonesian" : 80, "English" : 95},
                 {"Name" : "Bagas", "Math" : 88, "Science" : 92, "Indonesian" : 78, "English" : 78},
                 {"Name" : "Damar", "Math" : 70, "Science" : 72, "Indonesian" : 82, "English" : 98},
                 {"Name" : "Nabila", "Math" : 75, "Science" : 95, "Indonesian" : 88, "English" : 80},
                 {"Name" : "Kalea", "Math" : 82, "Science" : 88, "Indonesian" : 90, "English" : 98},
                 {"Name" : "Maura", "Math" : 72, "Science" : 79, "Indonesian" : 95, "English" : 92},
                 {"Name" : "Reza", "Math" : 85, "Science" : 77, "Indonesian" : 85, "English" : 90},
                 {"Name" : "Fira", "Math" : 72, "Science" : 75, "Indonesian" : 98, "English" : 100}]

# Main Menu
def mainMenu():
    print("\n"+2*"<"+5*"="+"SMP NusaBangsa Student Report"+5*"="+2*">")
    menu = int(input('''                                      
1. Show Student Report
2. Add Student Report
3. Update Student Report
4. Delete Student Report
5. Student Rank
6. Exit
                     
Please Choose One (1-6) : '''))
    
    while True:
        try:
            user_input = menu

            if user_input == 1:
                showData()
            elif user_input == 2:
                addData()
            elif user_input == 3:
                updateData()
            elif user_input == 4:
                delData()
            elif user_input == 5:
                sortData()
            elif user_input == 6:
                print("\nThank you & Have a Nice Day")
                exit()
            else:
                mainMenu()
                
        except ValueError:
            print("\nInvalid. Please input a number (1-6)")


# Show Data
def showData():
    print()
    menu = int(input(
'''<<==Show Student Report==>>

1. Show All Student Score
2. Find Student Report
3. Back to Menu

Please Choose One (1-3) : '''))

    try:
        if menu == 1:
            title1 = "SMP NusaBangsa Student Score 2024"
            title1_centered = f"\n{title1:^55}"
            print(title1_centered)
            showAll()

        elif menu == 2:
            def findData(data, findStudents):
                for student in data:
                    if student ['Name'] == findStudents:
                        return student
                return None

            findStudents = input("Student Name : ").capitalize()
            student = findData(studentGrades, findStudents)
            if student:
                print("\nResult : \n")
                for key,value in student.items():
                    print(f"{key} : {value}")
            else:
                print("\nStudent not Found, please check again.")
        elif menu == 3:
            mainMenu()
        else:
            print("\nInvalid. Please input a number (1-3) : ")            
    except IndexError:
            print("\nStudent grades have not been input.")

def showAll():
    header = studentGrades[0].keys()
    rows = [student.values() for student in studentGrades]
    showAll = tabulate(rows, headers=header, tablefmt="grid")
    print(showAll)
        
# Add Data
def addData():
    print()
    menu = int(input(
'''<<==Add Student Report==>>

1. Add New
2. Back to Menu

Please Choose One Sub-Menu (1/2) : '''))
    
    try:
        if menu == 1:
            while True:
                insName = input("\nName : ").strip().title()
                if insName.isalpha():
                    break
                else:
                    print("\nInvalid. Please input alphabetic characters only.")
            
            while True:
                insMath = int(input("Math : "))
                if isinstance(insMath, int) and 0 <= insMath <= 100:
                    break
                else:
                    print("\nInvalid. Please input the right value")
                    addData()
            
            while True:
                insScience = int(input("Science : "))
                if isinstance(insScience, int) and 0 <= insScience <= 100:
                    break
                else:
                    print("\nInvalid. Please input the right value")
                    addData()
            
            while True:
                insIndo = int(input("Indonesian : "))
                if isinstance(insIndo, int) and 0 <= insIndo <= 100:
                    break
                else:
                    print("\nInvalid. Please input the right value")
                    addData()
            
            while True:
                insEnglish = int(input("English : "))
                if isinstance(insEnglish, int) and 0 <= insEnglish <= 100:
                    break
                else:
                    print("\nInvalid. Please input the right value")
                    addData()
            

            studentGrades.append({
                "Name" : insName,
                "Math" : insMath,
                "Science" : insScience,
                "Indonesian" : insIndo,
                "English" : insEnglish
            })

            print("\nNew Student Report successfully added.\n")
            showAll()

        elif menu == 2:
            mainMenu()
        else:
            print("\nInvalid. Please input a number (1/2) : ")

    except ValueError:
        print("\nInvalid. Please input the right value.")


# Update Data
def updateData():
    print()
    menu = int(input(
'''<<==Update Student Report==>>

1. Update Score
2. Back to Menu

Please Choose One Sub-Menu (1/2) : '''))
    
    try:
        if menu == 1:
            findName = input("Name : ").capitalize()
            findSubject = input("Subject : ").capitalize()
            insValue = int(input("Score : "))

            subList = ["Math", "Science", "Indonesian", "English"]
            studentFound = False

            for student in studentGrades:
                if student["Name"] == findName:
                    studentFound = True
                    if findSubject in subList: 
                        student[findSubject] = int(insValue)
                        print(f"\n{findName}'s {findSubject} score has been updated.")
                        showAll()
                    else:
                        print("\nInvalid Subject. Please input Math / Science / Indonesian / English")
                    break
                            
            if not studentFound:
                print("\nStudent not found.")
            
            updateData()

        elif menu == 2:
            mainMenu()

        else:
            print("\nInvalid. Please input a number (1/2) : ")

    except ValueError:
            print("\nInvalid. Please input the right value.")

# Delete Data
def delData():
    print()
    menu = int(input(
'''<<==Delete Report==>>

1. Delete Student Score
2. Delete ALL Student Report
3. Back to Menu

Please Choose One Sub-Menu (1-3) : '''))
    
    try:
        if menu == 1:
            findName = input("Name : ").capitalize()
            nameFound = False

            for student in studentGrades:
                if student['Name'] == findName:
                    studentGrades.remove(student)
                    print(f"\n{findName}'s Score successfully deleted")
                    nameFound = True
                    showAll()
                    break
                    
            if not nameFound:
                print("\nStudent not found, please check again.")
                showAll()

        elif menu == 2:
            studentGrades.clear()
            print("\nALL Student Report successfully deleted.")

        elif menu == 3:
            mainMenu()

        else:
            print("\nInvalid. Please input a number (1-3) : ")

    except ValueError:
            print("\nInvalid. Please input the right value.")

# Sort Data
def sortData():
    print()
    menu = int(input(
'''<<==Student Rank==>>

1. Cumulative Student Rank
2. Back to Menu

Please Choose One Sub-Menu (1/2) : '''))
     
    if menu == 1:
        average_scores = []
        for student in studentGrades:
            name = student["Name"]
            math = student["Math"]
            science = student["Science"]
            indonesian = student["Indonesian"]
            english = student["English"]

            average_score = (math + science + indonesian + english) / 4
            average_scores.append({"Name": name, "AVG Score": average_score})
            
        avgRank = sorted(average_scores, key=lambda x: (-x["AVG Score"], x["Name"]))
        print("\nCumulative Student Rank :\n")
        
        rank = 1
        previous_score = None
        previous_rank = 0 
        for idx, student in enumerate(avgRank, start=1):
            if previous_score is None or student["AVG Score"] < previous_score:
                rank = idx
            else:
                rank = previous_rank + 1
            print(f"{rank}. {student['Name']} - Average Score : {student['AVG Score']:.2f}")
            previous_score = student["AVG Score"]
            previous_rank = rank
        print()

    elif menu == 2:
        mainMenu()

    else:
        print("\nInvalid. Please input a number (1/2) : ")

mainMenu()