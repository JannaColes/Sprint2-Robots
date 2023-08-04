# Title: Sprint 2 - Python Project 2
# Program Description:
# Written By S9 Robot Group 6
# Date Written is August 3 - 18, 2023

# Import Required Libraries
import datetime as dt
import FormatValues as FV
import ValidationModule as VM

# Initialize Variables
BalDue = 0
NumDays = 0
TotAmt = 0
BalDueAcc = 0
TotalBal = 0
MonthFee = 0

CarType = ""
TransDate = ""
TransDesc = ""

# Before the loop: Print headings, Initialize summary data, open the file

# Open the defaults file and read the values into variables
f = open('Defaults.dat', 'r')

# Define Program Constants
NXT_TRANS_NO = int(f.readline())
NXT_DRIVER_NO = int(f.readline())
STAND_FEE = float(f.readline())
DAY_RENT_FEE = float(f.readline())
WEEK_RENT_FEE = float(f.readline())
HST_RATE = float(f.readline())
CURR_DATE = dt.datetime.today()
CURR_YEAR = CURR_DATE.year
CURR_MONTH = CURR_DATE.month
CURR_DAY = CURR_DATE.day
MONTHLY_DUE_DATE = dt.date(CURR_YEAR, CURR_MONTH + 1, 1)
f.close()

print(CURR_DATE)
print(CURR_DAY, CURR_MONTH, CURR_YEAR)
print(NXT_TRANS_NO, NXT_DRIVER_NO, STAND_FEE, DAY_RENT_FEE, WEEK_RENT_FEE, HST_RATE)

# Define functions

def EnterEmployee():
    EmpFName = "Malerie"
    EmpLName = "Earle"
    StAdd = "244 Main Street"
    City = "Bishop's Falls"
    Prov = "NL"
    PosCode = "A0H1C0"
    PhNum = "(709) 631 - 3673"
    LicenseNo = "E910322017"
    LExpDate = "2026-09-22"
    InsCompany = "Co-Operators"
    PolicyNo = "12345"
    CarType = input("Enter Car Type (Own or Rental): ").title()
    BalDue = BalDueAcc

    # Write the values to a file for future reference if any changes have been made
    f = open("Employees.dat", "a")

    f.write(f"{NXT_DRIVER_NO}, ")
    f.write(f"{EmpFName + EmpLName}, ")
    f.write(f"{StAdd}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{PosCode}, ")
    f.write(f"{PhNum}, ")
    f.write(f"{LicenseNo}, ")
    f.write(f"{LExpDate}, ")
    f.write(f"{InsCompany}, ")
    f.write(f"{PolicyNo}, ")
    f.write(f"{CarType}, ")
    f.write(f"{BalDue}\n")
    f.close()

def EnterRevenue():
    RevType = "Transaction"
    NxtTransNo = NXT_TRANS_NO + 1
    TransDate = input("Enter Date of Transaction (YYYY-MM-DD): ")
    TransDate = dt.datetime.strptime(TransDate, "%Y-%M-%d")
    TransDesc = input("Enter Description of Transaction: ")
    DriverNo = input("Enter Driver No.: ")
    TransAmt = input("Enter Transaction Amount Before Taxes ($): ")

    HST = TransAmt * HST_RATE
    TotalAmt = TransAmt + HST
    BalDue += TotalAmt
    BalDueAcc += BalDue

    # Write the values to a file for future reference if any changes have been made
    f = open("Revenue.dat", "a")

    f.write(f"{RevType}, ")
    f.write(f"{NXT_TRANS_NO}, ")
    f.write(f"{TransDate}, ")
    f.write(f"{TransDesc}, ")
    f.write(f"{DriverNo}, ")
    f.write(f"{MonthFee}, ")
    f.write(f"{HST}, ")
    f.write(f"{TotAmt}\n")
    f.close()

def MonthlyFees():
   while True:
        if CURR_DAY == 1:
            RevType = "Monthly Fees"
            if CarType == "Own":
                StandFee = STAND_FEE
                MonthFee = StandFee
            elif CarType == "Rental":
                if NumDays < 7:
                    RentFee = DAY_RENT_FEE * NumDays
                elif NumDays >= 7:
                    RentFee = (NumDays / 7) * WEEK_RENT_FEE
                else:
                    RentFee = 0
            MonthFee = RentFee
            BalDueAcc += MonthFee
        else:
            break

        # Write the values to a file for future reference if any changes have been made
        f = open("MonthlyFees.dat", "a")

        f.write(f"{RevType}, ")
        f.write(f"{NXT_TRANS_NO}, ")
        f.write(f"{TransDate}, ")
        f.write(f"{TransDesc}, ")
        f.write(f"{DriverNo}, ")
        f.write(f"{MonthFee}, ")
        f.write(f"{HST}, ")
        f.write(f"{TotAmt}\n")
        f.close()

def EnterExpenses():
    InvoiceNo = 12345
    # Would make InvoiceNo an accumulator if code written
    InvDate = "2023-08-03"
    DriverNo = "1924"
    ItemNo = "4321"
    ItemDesc = "Office Supplies"
    ItemCost = 19.99
    Quantity = 2

    ItemTotal = ItemCost * Quantity
    SubTotal = ItemTotal
    HST = SubTotal * HST_RATE
    TotalBal = SubTotal + HST

    # Write the values to a file for future reference.
    f = open("Expenses.dat", "a")

    f.write(f"{InvoiceNo}, ")
    f.write(f"{InvDate}, ")
    f.write(f"{ItemNo}, ")
    f.write(f"{ItemDesc}, ")
    f.write(f"{ItemCost}, ")
    f.write(f"{Quantity}, ")
    f.write(f"{ItemTotal}, ")
    f.write(f"{SubTotal}, ")
    f.write(f"{HST}, ")
    f.write(f"{TotalBal}\n ")
    f.close()

def MainMenu():
    # Main program to return to, another menu for program start is located on bottom

    print(" " * 10, "HAB Taxi Services")
    print(" " * 10, "Company Services System")
    print()
    while True:
        print("1. Enter a New Employee (Driver)")
        print("2. Enter Company Revenues")
        print("3. Enter Company Expenses")
        print("4. Track Car Rentals")
        print("5. Record Employee Payment")
        print("6. Print Company Profit Listing")
        print("7. Print Driver Financial Listing")
        print("8. Your Report - Add Description")
        print("9. Quit Program")
        print()

        # Date
        if CURR_DAY == 1:
            MonthlyFees()
        else:
            continue

        # Inputs
        try:
            Choice = int(input(" " * 10, "Enter Choice (1-9): "))
        except:
            print("Error - Choice cannot be blank!")
            if len(Choice) > 1:
                print("Error - Choice cannot be more than one character!")
            elif not Choice.isdigit():
                print("Error - Choice must be numeric!")
            elif 1 < Choice <= 9:
                print("Error - Choice must be a number between 1 and 9!")
            else:
                break


        # Menu Choices
        if Choice == 1:
            EnterEmployee()
        elif Choice == 2:
            EnterRevenue()
        elif Choice == 3:
            EnterExpenses()
        # elif Choice == 4:
        # elif Choice == 5:
        # elif Choice == 6:
        # elif Choice == 7:
        # elif Choice == 8:
        elif Choice == 9:
            print("Thank you for using the NL Chocolate Company Travel Claims Processing System, Goodbye!")
            break
        else:
            print("Error - Invalid choice! Please select a number between 1 and 5!")

        # Provide an option to return to the main menu
        input("Press Enter to return to the main menu...")

# ***
#
# BalDue += MonthFee
# BalDueAcc += BalDue
# NXT_TRANS_NO += 1
# NXT_DRIVER_NO += 1
#
# # # Write the current values back to the default file. Note the use of “w” to overwrite and the use of the \n so that each value is placed on a separate line.
# f = open('defaults.dat', 'w')
#
# f.write(f"{NXT_TRANS_NO}, ")
# f.write(f"{NXT_DRIVER_NO}, ")
# f.write(f"{STAND_FEE}, ")
# f.write(f"{DAY_RENT_FEE}, ")
# f.write(f"{WEEK_RENT_FEE}, ")
# f.write(f"{HST_RATE}\n")
# f.close()
