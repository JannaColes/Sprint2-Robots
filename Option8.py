import datetime as dt

CURR_DATE = dt.datetime.today()
currDate = CURR_DATE.date()
CURR_YEAR = CURR_DATE.year
CURR_MONTH = CURR_DATE.month
CURR_DAY = CURR_DATE.day

def DriverLicenceListing():
    # This option prints a report of HAB employees' drivers licenses.
    # It calculates the number of days until a license expires and generates a listing of drivers who must
    # submit a new license for his/her employee file -

    while True:

        # Option 8 heading

        print("HAB TAXI SERVICES")
        print(f"DRIVER'S LICENSE LISTING AS ON {currDate}")

        print()
        print("Reports available: ")
        print("1. Full Summary - Employees' Driver's Licenses")
        print("2. Exception Report - Employees with a Licence Needing Renewal")
        print()

        # User makes a choice of report

        choiceLst = ["1", "2"]

        while True:
            choice = input("Please enter your selection (1 or 2): ")
            if choice not in choiceLst:
                    print("Error - choice must be 1 (full report) or 2(exception report)!")
            else:
                break

        if choice == "1":
            report = "ALL"

            print()
            print("Employees' Driver's Licenses")
            print("Full Summary")
            print()
            print("DRIVER   DRIVER             LICENSE         LICENSE      UPDATE")
            print("NUMBER   NAME               NUMBER          EXP DATE     REQUIRED")
            print("=================================================================")

        if choice == "2":
            report = "YES"

            print()
            print("Employees with a Licence Needing Renewal")
            print("Exception Report")
            print()
            print("DRIVER   DRIVER             LICENSE       LICENSE      DAYS UNTIL")
            print("NUMBER   NAME               NUMBER        EXP DATE     EXPIRED")
            print("=================================================================")

        # Counters and Accumulators

        totListingAcc = 0
        excemptListingAcc = 0

        # Open and read Employees.dat

        f = open('Employee.dat', 'r')

        for empInfoLine in f:
            empInfo = empInfoLine.split(",")

            driverNo = empInfo[0].strip()
            empFName = empInfo[1].strip()
            empLName = empInfo[2].strip()
            stAdd = empInfo[3].strip()
            city = empInfo[4].strip()
            prov = empInfo[5].strip()
            posCode = empInfo[6].strip()
            phNum = empInfo[7].strip()
            licenseNo = empInfo[8].strip()
            lExpDate = empInfo[9].strip()
            insCompany = empInfo[10].strip()
            policyNo = empInfo[11].strip()
            carType = empInfo[12].strip()
            balDue = float(empInfo[13].strip())

        # Do all necessary calculations

            strpLicExpDate = dt.datetime.strptime(lExpDate, "%Y-%m-%d").date()

            delta = strpLicExpDate - currDate
            numDaysDiff = delta.days


            licUpdateReq = ""
            if numDaysDiff <= 30:
                licUpdateReq = "YES"
            else:
                licUpdateReq = "NO"

            fullName = empFName[0] + " " + empLName

            if report == "ALL":
                print(f"{driverNo:<4s}     {fullName:<16s}   {licenseNo:<9s}      {lExpDate:<10s}      {licUpdateReq[0]:<1s}")
                totListingAcc += 1

            if report == licUpdateReq:
                print(f"{driverNo:<4s}     {fullName:<16s}   {licenseNo:<9s}    {lExpDate:<10s}   {numDaysDiff:<2d}")
                excemptListingAcc += 1

        f.close()

        # Counters and End of Listing notes

        if report == "ALL":
            print("=================================================================")
            print(f"Total Drivers: {totListingAcc:<2d}")

            print()
            print("Note:")
            print("Drivers with an UPDATED REQUEST status of YES must submit a copy")
            print("of their renewed drivers license to the office for company records.")
            print("-----------------------------------------------------------------")
            print("                           End of listing")
            print()

        else:
            print("=================================================================")
            print(f"Total Drivers: {excemptListingAcc:<2d}")

            print()
            print("Note:")
            print("All drivers listed must submit a copy of their renewed drivers")
            print("license to the office for company records.")
            print("-----------------------------------------------------------------")
            print("                           End of listing")
            print()



        # User enters next choice - view another report or return to main menu

        contLst = ["NEXT", "MENU"]
        while True:
            cont = input("Enter NEXT to view another drivers' license report or MENU to return to the main menu.").upper()
            if cont not in contLst:
                print("Error - user must enter NEXT or MENU!")
            else:
                break
            print()

        if cont == "MENU":
            break





