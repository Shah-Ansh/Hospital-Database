import subprocess as sp
from unittest import result
import pymysql
import pymysql.cursors
from colorama import Fore, Style


def printdict(dict):
    # print in a nice format
    max_key_length = max(len(key) for key in dict.keys())
    for key, value in dict.items():
        print(f"{key.ljust(max_key_length)}: {value}")


def printdictlist(dictlist):
    print("-------------------------------------------")
    for dict in dictlist:
        printdict(dict)
        print("-------------------------------------------")
    print()
    # print()


def delete_dept():
    """
    Function to implement option 1
    """
    try:
        dept_id = input("Enter Department ID: ")
        query = "DELETE FROM Department WHERE Department_ID = {}".format(dept_id)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_nurse():
    """
    Function to implement option 1
    """
    try:
        Nurse_id = input("Enter Nurse_id: ")
        query = "DELETE FROM Nurse WHERE Nurse_ID = {}".format(Nurse_id)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_patient():
    """
    Function to implement option 1
    """
    try:
        Patient_ID = input("Enter Patient_ID: ")
        query = "DELETE FROM Patient WHERE Patient_ID = {}".format(Patient_ID)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Alma_Mater_Nurse():
    """
    Function to implement option 1
    """
    try:
        Nurse_id = input("Enter Nurse_id: ")
        query = "DELETE FROM Alma_Mater_Nurse WHERE Nurse_ID = {}".format(Nurse_id)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Alma_Mater_Doctor():
    """
    Function to implement option 1
    """
    try:
        Doctor_ID = input("Enter Doctor_ID: ")
        query = "DELETE FROM Alma_Mater_Doctor WHERE Doctor_ID = {}".format(Doctor_ID)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_bill():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        query = "DELETE FROM Bill WHERE Case_ID = {}".format(Case_id)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_cases():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        query = "DELETE FROM Cases WHERE Case_ID = {}".format(Case_id)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Medical_History():
    """
    Function to implement option 1
    """
    try:
        Patient_ID = input("Enter Patient_ID: ")
        query = "DELETE FROM Medical_History WHERE Patient_ID = {}".format(Patient_ID)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Prerequisite_test():
    """
    Function to implement option 1
    """
    try:
        Test_type = input("Enter Test_type: ")
        query = "DELETE FROM Prerequisite_test WHERE Test_Type = '{}'".format(Test_type)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Prescription():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        query = "DELETE FROM Prescription WHERE Case_ID = {}".format(Case_id)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Previous_Cases():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        Patient_ID = input("Enter Patient_ID: ")
        query = (
            "DELETE FROM Previous_Cases WHERE Case_ID = {} AND Patient_ID = {}".format(
                Case_id, Patient_ID
            )
        )

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Receptionist():
    """
    Function to implement option 1
    """
    try:
        Receptionist_id = input("Enter Receptionist_id: ")
        query = "DELETE FROM Receptionist WHERE Receptionist_ID = {}".format(
            Receptionist_id
        )

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Tests():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        query = "DELETE FROM Tests WHERE Case_ID = {}".format(Case_id)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to     delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Workers():
    """
    Function to implement option 1
    """
    try:
        Worker_id = input("Enter Worker_id: ")
        query = "DELETE FROM Workers WHERE Worker_ID = {}".format(Worker_id)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to     delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_Doctor():
    """
    Function to implement option 1
    """
    try:
        Doctor_ID = input("Enter Doctor_ID: ")
        query = "DELETE FROM Doctor WHERE Doctor_ID = {}".format(Doctor_ID)

        cur.execute(query)
        con.commit()
        print("Deleted from database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_dept():
    """
    Function to implement option 1
    """
    try:
        # dept_id = input("Enter Department ID: ")
        dept_name = input("Enter Department Name: ")
        hod_id = input("Enter HOD ID: ")
        dept_location = input("Enter Department Location: ")
        query = "INSERT INTO Department(Department_Name,HOD_ID,Department_Location) VALUES('{}',{},'{}')".format(
            dept_name, hod_id, dept_location
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_nurse():
    """
    Function to implement option 1
    """
    try:
        # Nurse_id = input("Enter Nurse_id: ")
        Nurse_name = input("Enter Nurse_name: ")
        Gender = input("Enter Gender: ")
        Salary = input("Enter Salary: ")
        print("Enter number of alma mater")
        num = int(input())
        alma = []
        for i in range(num):
            alma.append(input("Enter Alma_Mater: "))

        query = (
            "INSERT INTO Nurse(Nurse_name,Gender,Salary) VALUES('{}','{}',{})".format(
                Nurse_name,
                Gender,
                Salary,
            )
        )

        cur.execute(query)
        con.commit()

        query = "SELECT Nurse_id FROM Nurse WHERE Nurse_name = '{}'".format(Nurse_name)

        cur.execute(query)
        con.commit()
        Nurse_id = cur.fetchone()["Nurse_id"]

        for al in alma:
            query = "INSERT INTO Alma_Mater_Nurse VALUES({},'{}')".format(
                Nurse_id,
                al,
            )

            cur.execute(query)
            con.commit()

        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_patient():
    """
    Function to implement option 1
    """
    try:
        # Patient_ID = input("Enter Patient_ID: ")
        Patient_Name = input("Enter Patient_Name: ")
        Gender = input("Enter Gender: ")
        Mobile_Number = input("Enter Mobile_Number: ")
        Blood_Group = input("Enter Blood_Group: ")
        query = "INSERT INTO Patient(Patient_Name,Gender,Mobile_Number,Blood_Group) VALUES('{}','{}',{},'{}')".format(
            # Patient_ID,
            Patient_Name,
            Gender,
            Mobile_Number,
            Blood_Group,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Alma_Mater_Nurse():
    """
    Function to implement option 1
    """
    try:
        Nurse_id = input("Enter Nurse_id: ")
        Alma_Mater = input("Enter Alma_Mater: ")
        query = "INSERT INTO Alma_Mater_Nurse VALUES({},'{}')".format(
            Nurse_id,
            Alma_Mater,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Alma_Mater_Doctor():
    """
    Function to implement option 1
    """
    try:
        Doctor_ID = input("Enter Doctor_ID: ")
        Alma_Mater = input("Enter Alma_Mater: ")
        query = "INSERT INTO Alma_Mater_Doctor VALUES({},'{}')".format(
            Doctor_ID,
            Alma_Mater,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_bill():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        Consultation_charges = input("Enter Consultation_charges: ")
        Operation_charges = input("Enter Operation_charges: ")
        other_charges = input("Enter other_charges: ")
        Transaction_id = input("Enter Transaction id: ")
        query = "INSERT INTO Bill VALUES({},{},{},{},{})".format(
            Case_id,
            Consultation_charges,
            Operation_charges,
            other_charges,
            Transaction_id,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_cases():
    """
    Function to implement option 1
    """
    try:
        # Case_id = input("Enter Case_id: ")
        Patient_Name = input("Enter Patient_Name: ")
        query = "SELECT Patient_ID FROM Patient WHERE Patient_Name = '{}'".format(
            Patient_Name
        )

        cur.execute(query)
        con.commit()

        result = cur.fetchall()
        # Patient_ID = result[0]['Patient_ID']
        if result == ():
            Gender = input("Enter Gender: ")
            Mobile_Number = input("Enter Mobile_Number: ")
            Blood_Group = input("Enter Blood_Group: ")
            query = "INSERT INTO Patient(Patient_Name,Gender,Mobile_Number,Blood_Group) VALUES('{}','{}',{},'{}')".format(
                Patient_Name,
                Gender,
                Mobile_Number,
                Blood_Group,
            )

            cur.execute(query)
            con.commit()
            query = "SELECT Patient_ID FROM Patient WHERE Patient_Name = '{}'".format(
                Patient_Name
            )

            cur.execute(query)
            con.commit()
            result = cur.fetchone()
            Patient_ID = result["Patient_ID"]

            # Doctor_name = input("Enter Doctor name: ")
            doc_name = input("Enter Doctor name: ")
            query = "SELECT Doctor_ID FROM Doctor WHERE Doctor_Name = '{}'".format(
                doc_name
            )

            cur.execute(query)
            con.commit()
            result = cur.fetchone()
            Doctor_ID = result["Doctor_ID"]
            Case_Since = "2023-12-03"
            Number_of_visits = 1
            Last_visit = "2023-12-03"
            Next_Appointment = "2023-12-10"
            Status = "Active"
            query = "INSERT INTO Cases(Patient_ID,Doctor_ID,Case_Since,Number_of_visits,Last_visit,Next_Appointment,Status) VALUES({},{},'{}',{},'{}','{}','{}')".format(
                # Case_id,
                Patient_ID,
                Doctor_ID,
                Case_Since,
                Number_of_visits,
                Last_visit,
                Next_Appointment,
                Status,
            )

            cur.execute(query)
            con.commit()

            query = "SELECT MAX(Case_ID) FROM Cases"

            cur.execute(query)
            con.commit()
            result = cur.fetchone()
            Case_id = result["MAX(Case_ID)"]
            print("------------------------------------------")
            print("New Case with ID: ", Case_id)
            print("------------------------------------------")
            print()
            # print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)
        else:
            # result= cur.fetchone()
            Patient_ID = result["Patient_ID"]

            # Doctor_name = input("Enter Doctor name: ")
            doc_name = input("Enter Doctor name: ")
            query = "SELECT Doctor_ID FROM Doctor WHERE Doctor_Name = '{}'".format(
                doc_name
            )

            cur.execute(query)
            con.commit()
            result = cur.fetchone()
            Doctor_ID = result["Doctor_ID"]
            Case_Since = "2023-12-03"
            Number_of_visits = 1
            Last_visit = "2023-12-03"
            Next_Appointment = "2023-12-10"
            Status = "Active"
            query = "INSERT INTO Cases(Patient_ID,Doctor_ID,Case_Since,Number_of_visits,Last_visit,Next_Appointment,Status) VALUES({},{},'{}',{},'{}','{}','{}')".format(
                # Case_id,
                Patient_ID,
                Doctor_ID,
                Case_Since,
                Number_of_visits,
                Last_visit,
                Next_Appointment,
                Status,
            )

            cur.execute(query)
            con.commit()

            query = "SELECT MAX(Case_ID) FROM Cases"

            cur.execute(query)
            con.commit()
            result = cur.fetchone()
            Case_id = result["MAX(Case_ID)"]
            print("------------------------------------------")
            print("New Case with ID: ", Case_id)
            print("------------------------------------------")

            # print("Inserted Into Database New Case with ID: ",Case_id)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Medical_History():
    """
    Function to implement option 1
    """
    try:
        Patient_ID = input("Enter Patient_ID: ")
        Diabetic = input("Enter Diabetic: ")
        Blood_pressure = input("Enter Blood_Pressure: ")
        Description_of_past_conditions = input("Enter Description_of_past_conditions: ")
        query = "INSERT INTO Medical_History VALUES({},{},{},'{}')".format(
            Patient_ID,
            Diabetic,
            Blood_pressure,
            Description_of_past_conditions,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Prerequisite_test():
    """
    Function to implement option 1
    """
    try:
        Test_type = input("Enter Test_type: ")
        Prerequisite_tests = input("Enter Prerequisite_tests: ")
        query = "INSERT INTO Prerequisite_test VALUES('{}','{}')".format(
            Test_type,
            Prerequisite_tests,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Prescription():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        Prescription_no = input("Enter Prescription_no: ")
        Medicines = input("Enter Medicines: ")
        query = "INSERT INTO Prescription VALUES({},{},'{}')".format(
            Case_id,
            Prescription_no,
            Medicines,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Previous_Cases():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        Patient_ID = input("Enter Patient_ID: ")
        query = "INSERT INTO Previous_Cases VALUES({},{})".format(
            Case_id,
            Patient_ID,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Receptionist():
    """
    Function to implement option 1
    """
    try:
        # Receptionist_id = input("Enter Receptionist_id: ")
        Receptionist_name = input("Enter Receptionist_name: ")
        Gender = input("Enter Gender: ")
        DOB = input("Enter DOB: ")
        Salary = input("Enter Salary: ")
        query = "INSERT INTO Receptionist(Receptionist_Name,Gender,DOB,Salary) VALUES({},'{}','{}','{}',{})".format(
            Receptionist_name,
            Gender,
            DOB,
            Salary,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Tests():
    """
    Function to implement option 1
    """
    try:
        Case_id = input("Enter Case_id: ")
        Test_type = input("Enter Test_type: ")
        Test_result = input("Enter Tesst_result: ")
        query = "INSERT INTO Tests VALUES({},'{}','{}')".format(
            Case_id,
            Test_type,
            Test_result,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to     insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def new_Workers():
    """
    Function to implement option 1
    """
    try:
        # Worker_id = input("Enter Worker_id: ")
        Worker_name = input("Enter Worker_name: ")
        Gender = input("Enter Gender: ")
        DOB = input("Enter DOB: ")
        salary_per_hour = input("Enter salary_per_hour: ")
        Shift = input("Enter Shift: ")
        Number_of_hours_worked_in_current_week = input(
            "Enter Number_of_hours_worked_in_current_week: "
        )
        query = "INSERT INTO Workers(Worker_name,Gender,DOB,Salary_per_hour,Shift,Number_of_hours_worked_in_current_week) VALUES('{}','{}','{}',{},{},{})".format(
            Worker_name,
            Gender,
            DOB,
            salary_per_hour,
            Shift,
            Number_of_hours_worked_in_current_week,
        )

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def search():
    """
    Function to implement updation
    """
    try:
        print("1. Search for a doctor")
        print("2. Search for a nurse")
        print("3. Search for a receptionist")
        print("4. Search for a worker")
        print("5. Search for a patient")
        print("6. Search for a department")
        print("7. Search for a case")
        print("8. Search for a bill")
        print("9. Search for a prescription")
        print("10. Search for a test")
        print("11. Search for a medical history")
        print("12. Search for a prerequisite test")
        print("13. Search for a previous case")
        print("14. Search for a alma mater doctor")
        print("15. Search for a alma mater nurse")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)
        from_where = ""
        to_search = ""
        query = ""
        if ch == 1:
            print("Enter Name of Doctor to search")
            to_search = input()
            query = f"SELECT * FROM Doctor WHERE Doctor_Name LIKE '{to_search}%'"
        elif ch == 2:
            print("Enter Name of Nurse to search")
            to_search = input()
            query = f"SELECT * FROM Nurse WHERE Nurse_Name LIKE '{to_search}%'"
        elif ch == 3:
            print("Enter Name of Receptionist to search")
            to_search = input()
            query = f"SELECT * FROM Receptionist WHERE Receptionist_Name LIKE '{to_search}%'"
        elif ch == 4:
            print("Enter Name of Worker to search")
            to_search = input()
            query = f"SELECT * FROM Workers WHERE Worker_Name LIKE '{to_search}%'"
        elif ch == 5:
            print("Enter Name of Patient to search")
            to_search = input()
            query = f"SELECT * FROM Patient WHERE Patient_Name LIKE '{to_search}%'"
        elif ch == 6:
            print("Enter Name of Department to search")
            to_search = input()
            query = (
                f"SELECT * FROM Department WHERE Department_Name LIKE '{to_search}%'"
            )
        elif ch == 7:
            print("Enter Case ID to search")
            to_search = input()
            query = f"SELECT * FROM Cases WHERE Case_ID = {to_search}"
        elif ch == 8:
            print("Enter Case ID to search")
            to_search = input()
            query = f"SELECT * FROM Bill WHERE Case_ID = {to_search}"
        elif ch == 9:
            print("Enter Case ID to search")
            to_search = input()
            query = f"SELECT * FROM Prescription WHERE Case_ID = {to_search}"
        elif ch == 10:
            print("Enter Case ID to search")
            to_search = input()
            query = f"SELECT * FROM Tests WHERE Case_ID = {to_search}"
        elif ch == 11:
            print("Enter Patient Name to search")
            to_search = input()
            query = f"SELECT * FROM Medical_History WHERE Patient_Name = {to_search}"
        elif ch == 12:
            print("Enter Test Type to search")
            to_search = input()
            query = (
                f"SELECT * FROM Prerequisite_test WHERE Test_Type LIKE '{to_search}%'"
            )
        elif ch == 13:
            print("Enter Patient Name to search")
            to_search = input()
            print("Enter Case ID to search")
            to_search_2 = input()
            query = f"SELECT * FROM Previous_Cases WHERE Patient_Name = {to_search} AND Case_ID = {to_search_2}"
        elif ch == 14:
            print("Enter Name of Doctor to search")
            to_search = input()
            query = f"SELECT * FROM Alma_Mater_Doctor join Doctor on Alma_Mater_Doctor.Doctor_ID = Doctor.Doctor_ID WHERE Doctor_Name = '{to_search}'"
        elif ch == 15:
            print("Enter Name of Nurse to search")
            to_search = input()
            query = f"SELECT * FROM Alma_Mater_Nurse join Nurse on Alma_Mater_Nurse.Nurse_ID = Nurse.Nurse_ID WHERE Nurse_Name = '{to_search}'"
        else:
            print("Error: Invalid Option")
            return

        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        printdictlist(result)
        print(Fore.GREEN + "Search Sucessfull" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to Search from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def hireAnEmployee():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """

    alma_list = []
    try:
        # Doctor_ID = input("Enter Doctor ID: ")
        Name = input("Enter Name of Doctor: ")
        num_alma = int(input("Enter number of educational institutions: "))
        while num_alma > 0:
            alma = input("Enter alma mater: ")
            alma_list.append(alma)
            num_alma = num_alma - 1
        Speciality = input("Enter Speciality: ")
        DOB = input("Enter DOB: ")
        DOJ = input("Enter DOJ: ")
        Age = input("Enter Age: ")
        Designation = input("Enter Designation: ")
        Salary = input("Enter Salary: ")
        print("Enter 1 for Cardiology")
        print("Enter 2 for Neurology")
        print("Enter 3 for Dermatology")
        print("Enter 4 for Pathology")
        print("Enter 5 for Ophtalmology")
        dept_name = int(input())
        query = ""
        if dept_name == 1:
            query = "SELECT Department_ID FROM Department WHERE Department_Name = 'Cardiology'"
        elif dept_name == 2:
            query = "SELECT Department_ID FROM Department WHERE Department_Name = 'Neurology'"
        elif dept_name == 3:
            query = "SELECT Department_ID FROM Department WHERE Department_Name = 'Dermatology'"
        elif dept_name == 4:
            query = "SELECT Department_ID FROM Department WHERE Department_Name = 'Pathology'"
        elif dept_name == 5:
            query = "SELECT Department_ID FROM Department WHERE Department_Name = 'Ophtalmology'"
        print(query)
        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        Department_ID = result[0]["Department_ID"]
        # Department_ID = input("Enter Department ID: ")

        query = "INSERT INTO Doctor(Doctor_Name,Speciality,DOB,Date_of_Joining,Age,Designation,Salary,Department_ID) VALUES('{}','{}','{}','{}',{},'{}',{},{})".format(
            Name,
            Speciality,
            DOB,
            DOJ,
            Age,
            Designation,
            Salary,
            Department_ID,
        )

        # Doctor_Name     | varchar(255) | NO   |     | NULL    |       |
        # | Speciality      | varchar(255) | NO   |     | NULL    |       |
        # | DOB             | date         | NO   |     | NULL    |       |
        # | Date_of_Joining | varchar(255) | NO   |     | NULL    |       |
        # | Age             | varchar(255) | NO   |     | NULL    |       |
        # | Designation     | varchar(255) | NO   |     | NULL    |       |
        # | Salary          | int          | NO   |     | NULL    |       |
        # | Department_ID

        cur.execute(query)
        con.commit()

        query = "SELECT Doctor_ID FROM Doctor WHERE Doctor_Name = '{}'".format(Name)
        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        doctorid = result[0]["Doctor_ID"]

        while alma_list:
            query = "INSERT INTO Alma_Mater_Doctor(Doctor_ID,Alma_Mater) VALUES({},'{}')".format(
                doctorid,
                alma_list.pop(),
            )

        cur.execute(query)
        con.commit()

        print(Fore.GREEN + "Inserted Into Database" + Style.RESET_ALL)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)

    return


def insert_into_table():
    """
    Function to implement updation
    """
    try:
        print("1. Insert for a doctor")
        print("2. Insert for a nurse")
        print("3. Insert for a receptionist")
        print("4. Insert for a worker")
        print("5. Insert for a patient")
        print("6. Insert for a department")
        print("7. Insert for a case")
        print("8. Insert for a bill")
        print("9. Insert for a prescription")
        print("10. Insert for a test")
        print("11. Insert for a medical history")
        print("12. Insert for a prerequisite test")
        print("13. Insert for a previous case")
        print("14. Insert for a alma mater doctor")
        print("15. Insert for a alma mater nurse")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)

        if ch == 1:
            hireAnEmployee()
        elif ch == 2:
            new_nurse()
        elif ch == 3:
            new_Receptionist()
        elif ch == 4:
            new_Workers()
        elif ch == 5:
            new_patient()
        elif ch == 6:
            new_dept()
        elif ch == 7:
            new_cases()
        elif ch == 8:
            new_bill()
        elif ch == 9:
            new_Prescription()
        elif ch == 10:
            new_Tests()
        elif ch == 11:
            new_Medical_History()
        elif ch == 12:
            new_Prerequisite_test()
        elif ch == 13:
            new_Previous_Cases()
        elif ch == 14:
            new_Alma_Mater_Doctor()
        elif ch == 15:
            new_Alma_Mater_Nurse()
        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def search_case(id):
    """
    Function to implement updation
    """
    try:
        query = f"SELECT Patient.Patient_id,Patient_Name,Doctor.Doctor_ID,Doctor_Name,Bill.Consultation_charges,Bill.Operation_charges,Bill.other_charges,Bill.Transaction_id FROM (Cases JOIN Patient ON Patient.Patient_ID=Cases.Patient_ID) JOIN Doctor ON Doctor.Doctor_ID=Cases.Doctor_id JOIN Bill ON Cases.Case_ID=Bill.Case_ID  WHERE Cases.Case_ID={id}"

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Query Executed Generated Sucessfully" + Style.RESET_ALL)
        result = cur.fetchall()
        # print(result)
        printdictlist(result)
        query = f"SELECT Medicines FROM Prescription WHERE Case_ID={id}"

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Query Executed Generated Sucessfully" + Style.RESET_ALL)
        result = cur.fetchall()
        # print(result)
        printdictlist(result)
    except:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def all_details_of_case():
    """
    Function to implement updation
    """
    try:
        ch = int(input("Entre Case ID:> "))
        tmp = sp.call("clear", shell=True)
        search_case(ch)
    except:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def all_details_of_patient():
    """
    Function to implement updation
    """
    try:
        ch = int(input("entre patient id:> "))
        query = f"SELECT Case_ID FROM Cases WHERE Patient_ID={ch}"

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Query Executed Generated Sucessfully" + Style.RESET_ALL)
        result = cur.fetchall()
        for i in result:
            search_case(i["Case_ID"])
        # tmp = sp.call("clear", shell=True)

    except:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def find_avg(param):
    try:
        query = ""
        if param == 1:
            query = f"SELECT AVG(Salary) FROM Doctor"
        elif param == 2:
            query = f"SELECT AVG(Salary) FROM Nurse"
        elif param == 3:
            query = f"SELECT AVG(Salary) FROM Receptionist"
        elif param == 4:
            query = f"SELECT AVG(salary_per_hour) FROM Workers"
        elif param == 5:
            query = f"SELECT AVG(Consultation_charges+Operation_charges+other_charges) FROM Bill"
        elif param == 6:
            query = f"SELECT AVG(Age) FROM Doctor"
        elif param == 7:
            query = f"SELECT AVG(Age) FROM Nurse"
        elif param == 8:
            query = f"SELECT AVG(Age) FROM Receptionist"
        elif param == 9:
            query = f"SELECT AVG(Age) FROM Workers"
        elif param == 10:
            query = f"SELECT Doctor_id,COUNT(*) AS Number_of_Cases FROM Cases GROUP BY Doctor_id"

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Executed Successfully" + Style.RESET_ALL)
        ans = cur.fetchall()
        printdictlist(ans)

    except:
        con.rollback()
        print(Fore.RED + "Failed to insert into database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def delete_handle():
    """
    Function to implement updation
    """
    try:
        print("1. Delete for a doctor")
        print("2. Delete for a nurse")
        print("3. Delete for a receptionist")
        print("4. Delete for a worker")
        print("5. Delete for a patient")
        print("6. Delete for a department")
        print("7. Delete for a case")
        print("8. Delete for a bill")
        print("9. Delete for a prescription")
        print("10. Delete for a test")
        print("11. Delete for a medical history")
        print("12. Delete for a prerequisite test")
        print("13. Delete for a previous case")
        print("14. Delete for a alma mater doctor")
        print("15. Delete for a alma mater nurse")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)

        if ch == 1:
            delete_Doctor()
        elif ch == 2:
            delete_nurse()
        elif ch == 3:
            delete_Receptionist()
        elif ch == 4:
            delete_Workers()
        elif ch == 5:
            delete_patient()
        elif ch == 6:
            delete_dept()
        elif ch == 7:
            delete_cases()
        elif ch == 8:
            delete_bill()
        elif ch == 9:
            delete_Prescription()
        elif ch == 10:
            delete_Tests()
        elif ch == 11:
            delete_Medical_History()
        elif ch == 12:
            delete_Prerequisite_test()
        elif ch == 13:
            delete_Previous_Cases()
        elif ch == 14:
            delete_Alma_Mater_Doctor()
        elif ch == 15:
            delete_Alma_Mater_Nurse()
        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to Delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def details_of_all_avg():
    print("1. option 1 for avg salary of doctor:")
    print("2. option 2 for avg salary of nurse:")
    print("3. option 3 for avg salary of receptionist:")
    print("4. option 4 for avg salary of worker:")
    print("5. option 5 for avg bill:")
    print("6. option 6 for avg age of doctor:")
    print("7. option 7 for avg age of nurse:")
    print("8. option 8 for avg age of receptionist:")
    print("9. option 9 for avg age of worker:")
    print("10. option 10 for no_of_cases of doctors:")

    ch = int(input("entre choice:> "))
    tmp = sp.call("clear", shell=True)
    find_avg(ch)


def details_of_doctor_in_dept(dept_id):
    try:
        query = f"SELECT * FROM Doctor WHERE Department_id={dept_id}"

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Query Executed Successfully" + Style.RESET_ALL)
        ans = cur.fetchall()
        printdictlist(ans)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to Delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def details_doct_department():
    ch = int(input("entre department id:> "))
    tmp = sp.call("clear", shell=True)
    details_of_doctor_in_dept(ch)


def details_of_suc_case_of_doctor(doctor_id):
    try:
        query = f"SELECT Cases.Case_id,Cases.Patient_id FROM Doctor join Cases on Cases.Doctor_id=Doctor.Doctor_id WHERE Cases.Doctor_id={doctor_id} AND Cases.Status='SUCCESS'"
        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Query Executed Successfully" + Style.RESET_ALL)
        ans = cur.fetchall()
        printdictlist(ans)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to Delete from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def details_success_case():
    ch = int(input("entre doctor id:> "))
    tmp = sp.call("clear", shell=True)
    details_of_suc_case_of_doctor(ch)


def update_Doctor():
    """
    Function to implement updation
    """
    try:
        print("Enter the Field to Update: ")
        print("1. Salary")
        print("2. Designation")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)
        Doctor_ID = input("Enter Doctor_ID: ")
        if ch == 1:
            Salary = input("Enter Salary: ")
            query = "UPDATE Doctor SET Salary = {} WHERE Doctor_ID = {}".format(
                Salary,
                Doctor_ID,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        elif ch == 2:
            Designation = input("Enter Designation: ")
            query = "UPDATE Doctor SET Designation = '{}' WHERE Doctor_ID = {}".format(
                Designation,
                Doctor_ID,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def update_nurse():
    """
    Function to implement updation
    """
    try:
        print("Enter the Field to Update: ")
        print("1. Salary")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)
        Nurse_id = input("Enter Nurse_id: ")
        if ch == 1:
            Salary = input("Enter Salary: ")
            query = "UPDATE Nurse SET Salary = {} WHERE Nurse_id = {}".format(
                Salary,
                Nurse_id,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)

        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def update_Receptionist():
    """
    Function to implement updation
    """
    try:
        print("Enter the Field to Update: ")
        print("1. Salary")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)
        Receptionist_id = input("Enter Receptionist_id: ")
        if ch == 1:
            Salary = input("Enter Salary: ")
            query = (
                "UPDATE Receptionist SET Salary = {} WHERE Receptionist_id = {}".format(
                    Salary,
                    Receptionist_id,
                )
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)

        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def update_Workers():
    """
    Function to implement updation
    """
    try:
        print("Enter the Field to Update: ")
        print("1. Salary per hour")
        print("2. Number of hours workin in current week")
        print("3. Shift")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)
        Worker_id = input("Enter Worker_id: ")
        if ch == 1:
            salary_per_hour = input("Enter salary_per_hour: ")
            query = (
                "UPDATE Workers SET salary_per_hour = {} WHERE Worker_id = {}".format(
                    salary_per_hour,
                    Worker_id,
                )
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        elif ch == 2:
            Number_of_hours_worked_in_current_week = input(
                "Enter Number_of_hours_worked_in_current_week: "
            )
            query = "UPDATE Workers SET Number_of_hours_worked_in_current_week = {} WHERE Worker_id = {}".format(
                Number_of_hours_worked_in_current_week,
                Worker_id,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        elif ch == 3:
            Shift = input("Enter Shift: ")
            query = "UPDATE Workers SET Shift = {} WHERE Worker_id = {}".format(
                Shift,
                Worker_id,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def update_patient():
    """
    Function to implement updation
    """
    try:
        print("Enter the Field to Update: ")
        print("1. Mobile Number")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)
        Patient_ID = input("Enter Patient_ID: ")
        if ch == 1:
            Mobile_Number = input("Enter Mobile_Number: ")
            query = (
                "UPDATE Patient SET Mobile_Number = {} WHERE Patient_ID = {}".format(
                    Mobile_Number,
                    Patient_ID,
                )
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def update_cases():
    """
    Function to implement updation
    """
    try:
        print("Enter the Field to Update: ")
        print("1. Number of visits")
        print("2. Last visit")
        print("3. Next Appointment")
        print("4. Status")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)
        Case_id = input("Enter Case_id: ")
        if ch == 1:
            Number_of_visits = input("Enter Number_of_visits: ")
            query = "UPDATE Cases SET Number_of_visits = {} WHERE Case_id = {}".format(
                Number_of_visits,
                Case_id,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        elif ch == 2:
            Last_visit = input("Enter Last_visit: ")
            query = "UPDATE Cases SET Last_visit = '{}' WHERE Case_id = {}".format(
                Last_visit,
                Case_id,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        elif ch == 3:
            Next_Appointment = input("Enter Next_Appointment: ")
            query = (
                "UPDATE Cases SET Next_Appointment = '{}' WHERE Case_id = {}".format(
                    Next_Appointment,
                    Case_id,
                )
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        elif ch == 4:
            Status = input("Enter Status: ")
            query = "UPDATE Cases SET Status = '{}' WHERE Case_id = {}".format(
                Status,
                Case_id,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def update_Medical_History():
    """
    Function to implement updation
    """
    try:
        print("Enter the Field to Update: ")
        print("1. Diabetic")
        print("2. Blood_pressure")
        print("3. Description_of_past_conditions")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)
        Patient_ID = input("Enter Patient_ID: ")
        if ch == 1:
            Diabetic = input("Enter Diabetic(0 for no and 1 for yes): ")
            query = (
                "UPDATE Medical_History SET Diabetic = {} WHERE Patient_ID = {}".format(
                    Diabetic,
                    Patient_ID,
                )
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        elif ch == 2:
            Blood_pressure = input(
                "Enter Blood_pressure(0 for normal and 1 for high or low): "
            )
            query = "UPDATE Medical_History SET Blood_pressure = {} WHERE Patient_ID = {}".format(
                Blood_pressure,
                Patient_ID,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        elif ch == 3:
            Description_of_past_conditions = input(
                "Enter Description_of_past_conditions: "
            )
            query = "UPDATE Medical_History SET Description_of_past_conditions = '{}' WHERE Patient_ID = {}".format(
                Description_of_past_conditions,
                Patient_ID,
            )

            cur.execute(query)
            con.commit()
            print(Fore.GREEN + "Updated Sucessfully" + Style.RESET_ALL)
        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def update_handle():
    """
    Function to implement updation
    """
    try:
        print("1. Update for a Doctor")
        print("2. Update for a Nurse")
        print("3. Update for a Receptionist")
        print("4. Update for a Worker")
        print("5. Update for a Patient")
        print("6. Update for a Case")
        print("7. Update for a Medical history")

        ch = int(input("Enter choice> "))
        tmp = sp.call("clear", shell=True)

        if ch == 1:
            update_Doctor()
        elif ch == 2:
            update_nurse()
        elif ch == 3:
            update_Receptionist()
        elif ch == 4:
            update_Workers()
        elif ch == 5:
            update_patient()
        elif ch == 6:
            update_cases()
        elif ch == 7:
            update_Medical_History()
        else:
            print("Error: Invalid Option")

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def list_of_patient_for_specific_blood_group(blood_group):
    try:
        query = f"SELECT DISTINCT(Patient_Name) ,Last_visit FROM Patient JOIN Cases ON Cases.Patient_id=Patient.Patient_id WHERE Blood_Group='{blood_group}' AND DATEDIFF(CURDATE(), Cases.Last_visit) <= 180"

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Query Executed Successfully" + Style.RESET_ALL)
        ans = cur.fetchall()
        print(ans)
        printdictlist(ans)

    except Exception as e:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def list_patient_blood_group():
    print("enter blood group:")
    blood_group = ""
    blood_group = input()
    list_of_patient_for_specific_blood_group(blood_group)


def list_of_workers():
    ch = int(input("Enter shift> "))
    tmp = sp.call("clear", shell=True)

    query = f"select Worker_name from Workers where Shift={ch}"

    cur.execute(query)
    con.commit()
    # print("Query Executed Successfully")
    ans = cur.fetchall()
    printdictlist(ans)


def max_salary():
    ch = int(input("Enter department id> "))
    tmp = sp.call("clear", shell=True)

    query = f"select max(Salary) from Doctor where Department_id={ch}"

    cur.execute(query)
    con.commit()
    # print("Query Executed Successfully")
    ans = cur.fetchall()
    printdictlist(ans)


def next_month():
    try:
        query = "SELECT Patient_Name,Mobile_Number FROM Patient JOIN Cases ON Cases.Patient_id=Patient.Patient_id WHERE DATEDIFF(Cases.Next_Appointment,CURDATE())<= 30 AND DATEDIFF(Cases.Next_Appointment,CURDATE())>=0"

        cur.execute(query)
        con.commit()
        print(Fore.GREEN + "Query Executed Successfully" + Style.RESET_ALL)
        ans = cur.fetchall()
        printdictlist(ans)

    except:
        con.rollback()
        print(Fore.RED + "Failed to update from database" + Style.RESET_ALL)
        print(">>>>>>>>>>>>>", e)


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if ch == 1:
        insert_into_table()
    elif ch == 2:
        delete_handle()
    elif ch == 3:
        search()
    elif ch == 4:
        all_details_of_case()
    elif ch == 5:
        all_details_of_patient()
    elif ch == 6:
        details_of_all_avg()
    elif ch == 7:
        details_doct_department()
    elif ch == 8:
        details_success_case()
    elif ch == 9:
        update_handle()
    elif ch == 10:
        list_patient_blood_group()
    elif ch == 11:
        list_of_workers()
    elif ch == 12:
        next_month()
    elif ch == 13:
        max_salary()
    else:
        print("Error: Invalid Option")


# Global
while 1:
    tmp = sp.call("clear", shell=True)

    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(
            host="localhost",
            port=3306,
            user="newadmin",
            password='Divyaraj@123',
            db="Hospital",
            cursorclass=pymysql.cursors.DictCursor,
        )
        tmp = sp.call("clear", shell=True)

        if con.open:
            print(Fore.YELLOW + "Connected" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed to connect")

        tmp = input(Fore.BLUE + "Enter any key to CONTINUE>" + Style.RESET_ALL)

        with con.cursor() as cur:
            while 1:
                tmp = sp.call("clear", shell=True)
                # Here taking example of Employee Mini-world
                print("1. Option 1 for Insert")
                print("2. Option 2 for Delete")  # Fire an Employee
                print("3. Option 3 for Search")  # Promote Employee
                print("4. Option 4 for all details of case")
                print("5. Option 5 for all details of patient")
                print("6. Option 6 for all details of average salary")
                print("7. Option 7 for all details of doctor in Department")
                print("8. Option 8 for all details of SUCCESS case of doctor")
                print("9. Option 9 for Update")
                print("10. Option 10 for list of patient for specific blood group")
                print("11. Option 11 for list of current working workers")
                print(
                    "12. option 12 for list of patient whose appointment within next month"
                )
                print("13. For displaying maximum salary of doctor in a department")
                print("16. option 16 for logout")
                ch = int(input(Fore.YELLOW + "Enter choice> " + Style.RESET_ALL))
                tmp = sp.call("clear", shell=True)
                if ch == 16:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input(
                        Fore.BLUE + "Enter any key to CONTINUE>" + Style.RESET_ALL
                    )

    except Exception as e:
        tmp = sp.call("clear", shell=True)
        print(e)
        print(
            Fore.RED
            + "Connection Refused: Either username or password is incorrect or user doesn't have access to database"
            + Style.RESET_ALL
        )
        tmp = input("Enter any key to CONTINUE>")
