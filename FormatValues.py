# Title: QAP 4
# Written By Malerie Earle
# Date Written is July 17 - 26, 2023

# Imports
import datetime

# Format Dates

def FormatDateCommaBdY(StrDate, StrFormat):
    # function will accept a date and format it to Month ##, ####

    FormatDateMdY = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%B %d, %Y")

    return StrDate


def FormatDateCommaWBdY(StrDate, StrFormat):
    # Function will accept a date and format it to Weekday, Month dd, yyyy.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%A, %B %d, %Y")

    return StrDate


def FormatDateCommabdY(StrDate, StrFormat):
    # Function will accept a date and format it to Weekday, Month dd, yyyy.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%b %d, %Y")

    return StrDate


def FormatDateCommadbY(StrDate, StrFormat):
    # Function will accept a date and format it to Weekday, Month dd, yyyy.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%d %b, %Y")

    return StrDate

def FormatDateCommaAmdY(StrDate, StrFormat):
    # Function will accept a date and format it to Weekday, Month dd, yyyy.
    FormatDateDashWYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%A %m %d, %Y")

    return StrDate


def FormatDateCommamdY(StrDate, StrFormat):
    # Function will accept a date and format it to Weekday, Month dd, yyyy.

    FormatDateDashWYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%m %d, %Y")

    return StrDate


def FormatDateDashYmd(StrDate, StrFormat):
    # Function will accept a date and format it to yyyy-mm-dd.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%Y-%m-%d")

    return StrDate


def FormatDateDashmdY(StrDate, StrFormat):
    # Function will accept a date and format it to yyyy-mm-dd.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%m-%d-%Y")

    return StrDate

def FormatDateDashdby(StrDate, StrFormat):
    # Function will accept a date and format it to dd-Mon-yy.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%d-%b-%y")

    return StrDate


def FormatDateSlashYmd(StrDate, StrFormat):
    # Function will accept a date and format it to yyyy-mm-dd.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%Y/%m/%d")

    return StrDate


def FormatDateSlashmdY(StrDate, StrFormat):
    # Function will accept a date and format it to yyyy-mm-dd.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%m/%d/%Y")

    return StrDate

def FormatDateSlashdby(StrDate, StrFormat):
    # Function will accept a date and format it to dd-Mon-yy.

    FormatDateYmd = datetime.datetime.strftime(StrDate, StrFormat)
    StrDate = datetime.datetime.strftime(StrDate, "%d/%b/%y")

    return StrDate


# Format Dollars, Numbers, Floats



def FormatDollar2d(Variable):
    # function will accept a variable and format it to $###,###.##

    Variable = (f'${Variable:,.2f}')

    return Variable


def FormatDollar0d(Variable):
    # function will accept a variable and format it to $###,###

    Variable = float(f'${Variable:,.0f}')

    return Variable


def FormatNumberComma(Variable):
    # function will accept variable and add a comma to the number #,###

    Variable = f"{Variable:,}"

    return Variable


def FormatNumberComma1d(Variable):
    # function will accept variable and add a comma to the number #,###.##

    Variable = f"{Variable:,.1f}"

    return Variable


def FormatNumberComma2d(Variable):
    # function will accept variable and add a comma to the number #,###.##

    Variable = f"{Variable:,.2f}"

    return Variable


# Format Name, Address, Personal details

def FormatName(FirstName, LastName):
    # function will accept variables and concatenate them together

    FullName = f"{FirstName}" + " " + f"{LastName}"

    return FullName


def FormatPhoneNum(PhoneNum):
    # Function to format the phone number as (###) ###-####

    FormattedPhoneNum = f"({PhoneNum[:3]}) {PhoneNum[3:6]}-{PhoneNum[6:]}"

    return FormattedPhoneNum


def FormatAddress(StAdd, City, Prov, PosCode):
    # Function to format mailing address

    MailingAddress = f"""
    {StAdd:<20s}
    {City:<10s}, {Prov:<2s}
    {PosCode:<7s}    
    """

    return MailingAddress


def FormatAddressPhNum(StAdd, City, Prov, PosCode, PhNum):
    # Function to format mailing address

    MailingAddress = f"""
    {StAdd:<20s}
    {City:<10s}, {Prov:<2s}
    {PosCode:<7s}    
    {PhNum:<16s}
    """

    return MailingAddress