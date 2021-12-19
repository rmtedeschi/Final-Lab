


#Function to get and verify employee ID is 7 chars or less, and ask again if it fails
def empID():
    empID = input("Enter Employee ID: ")
    verified = False
    while verified == False:
        if len(empID) <= 7 and empID.isnumeric():
            verified = True
            return empID
        else: 
            empID = input("Input invalid, enter an integer that is 7 digits or less")

#Function to get name input
def empName():
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    return first + ' ' + last

#Function to get payrate and verify that it is between 18 and 27, and ask again if it fails
def payRate():
    hourly = float(input("Enter payrate as float between 18 and 27: "))
    while hourly > 27 or hourly < 18:
        hourly = float(input("Payrate must be between 18 and 27, please enter a valid value: "))
    
    return hourly

#Function to get and verify that email input is valid
def empEmail():
    badCharsEmail = '!#$%^&*()=+,<>/?;:[]{}\)'
    email = input("Enter employee email: ")
    verified = False
    while verified == False:
        for i in email:
            if i in badCharsEmail:
                email = input("input invalid, please enter employee email: ")
            else:
                verified = True
                return email

#Function to get and verify employee address
def empAddress():
    badCharsAddress = '!"@$%^&*_=+<>?;:[]{})'
    address = input("Enter employee address, if you choose to not put in your adress enter NA: ")
    verified = False
    while verified == False:
        for i in address:
            if i in badCharsAddress:
                address = input("input invalid, please enter employee address: ")
            else:
                verified = True
                return address

#Function to get and return dictionary with an employee's information
def getEmployeeInfo():
    empDict = {"ID":[], "Name":[], "Email":[], "Address":[], "Salary":[]}

    empDict["ID"] = empID()
    empDict["Name"] = empName()
    empDict["Email"] = empEmail()
    empDict["Address"] = empAddress()
    empDict["Salary"] = payRate()

    return empDict

employeeInfo = []
employeeInfo.append(getEmployeeInfo())
while input("Would you like to enter another employee? (enter N to quit)") != 'N':
    employeeInfo.append(getEmployeeInfo())
    
print(employeeInfo)

    
