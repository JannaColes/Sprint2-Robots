# Title: QAP 4
# Written By Malerie Earle
# Date Written is July 17 - 26, 2023

# Imports
# Definitions
allowed_Char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwyz0123456789")
allowed_Let = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwyz")
allowed_Num = set("0123456789")


# Functions
# Individual Validations
def BlankCheck(Variable):
    # function accepts a variable and checks to see if it is blank
    if Variable == "":
        print(f"Error - {Variable} cannot be blank!")
    else:
        return Variable

def LengthCheck(Variable, Number):
    # function accepts a variable and checks to see if it is the length of second variable
    if len(Variable) != Number:
        print(f"Error - Length of {Variable} must be at least {Number} characters!")
    else:
        return Variable


def NumberCheck(Variable):
    # function accepts a variable and checks to see if it is numeric
    if not Variable.isdigit():
        print(f"Error - {Variable} must be numeric!")
    else:
        return Variable


def InputCheck(Variable, Input1, Input2):
    # function accepts a variable and checks to see if it is between the second and third variable
    if Variable != Input1 and Variable != Input2:
        print(f"Error - {Variable} should be {Input1} or {Input2}!")

    return Variable


def ProvCheck(Prov):
    ProvLst = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "NT", "YT", "NU"]
    if Prov not in ProvLst:
        print("Error - Province must be valid abbreviation!")
    else:
        return Prov


def ListCheck(Variable, List):
    if Variable not in List:
        print(f"Error - {Variable} must be a valid choice!")
    else:
        return Variable


def CharCheck(Variable):
    # Check if variable has allowed characters
    Allowed_Characters = ["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-.' "]
    if Variable not in Allowed_Characters:
        print("Error - invalid character entered, try again!")
    else:
        return Variable


# Validation Categories

def PostalCodeCheck(PosCode):
    # Function to validate postal codes
    if PosCode != "":
        if len(PosCode) == 6:
            for i, v in enumerate(PosCode):
                if i % 2 == 0:
                    if not v.isalpha():
                        print("Error - Must be in valid A1A1A1 format!")
                        return None
                else:
                    if not v.isdigit():
                        print("Error - Must be in valid A1A1A1 format!")
                        return None
            return PosCode
        else:
            print("Error - invalid entry, Postal Code must be 6 characters with no spaces.")
            return None
    else:
        print("Error - Postal Code cannot be blank")
        return None


def PhNumCheck(PhNum):
    # Function to validate phone numbers
    if PhNum == "":
        print("Error - Phone number cannot be blank")
    elif len(PhNum) != 10:
        print("Error - Phone number must have 10 digits")
    elif not PhNum.isdigit():
        print(f"Error - Phone number must be numeric!")
    else:
        return PhNum


def ProvFullCheck(Prov):
    ProvLst = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "NT", "YT", "NU"]
    if Prov != "":
        if len(Prov) == 2:
            if Prov not in ProvLst:
                print("Error - Province must be valid abbreviation!")
            else:
                return Prov
        else:
            print("Error - invalid length, Province abbreviation must be 2 letters!")
    else:
        print("Error - Province cannot be blank!")
    return Prov