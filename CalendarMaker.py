import datetime, random
import calendar

Months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

def ChooseYear():
    Year = input(">")

    try:
        Year = int(Year)
        #1582

        if Year < 1582:
            Year = 1583
        elif Year > 9999:
            Year = 9999

    except:
        Year = ChooseYear()

    return Year

def ChooseMonth():
    Month = input(">")

    try:
        Month = int(Month)

        if Month < 1:
            Month = 1
        elif Month > 12:
            Month = 12

    except:
        Month = ChooseMonth()

    return Month

print("Enter the year for the calendar:")
Year = int(ChooseYear())
print("Enter the month for the calendar, 1-12:")
Month = ChooseMonth()

Date = datetime.datetime(int(Year), int(Month), 1)
WeekDay = Date.weekday()

def GetOldDate():
    OldMonth = int(Month) - 1
    OldYear = int(Year)

    if OldMonth == 0: 
        OldMonth = 12
        OldYear -= 1

    return datetime.datetime(OldYear, OldMonth, 1)

LastDate = GetOldDate()

_, DaysInOldMonth = calendar.monthrange(LastDate.year, LastDate.month)
_, DaysInMonth = calendar.monthrange(Date.year, Date.month)

print(WeekDay)
print(DaysInOldMonth)

Calender = """
---Sunday-----Monday-----Tuesday---Wednesday--Thursday----Friday----Saturday--  

+----------+----------+----------+----------+----------+----------+----------+
|       x  |       x  |       x  |       x  |       x  |       x  |       x  |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|       x  |       x  |       x  |       x  |       x  |       x  |        x |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|       x  |       x  |       x  |       x  |       x  |       x  |       x  |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|       x  |       x  |       x  |       x  |       x  |       x  |       x  |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|       x  |       x  |       x  |       x  |       x  |       x  |       x  |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|       x  |       x  |       x  |       x  |       x  |       x  |       x  |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
"""

UsedOldDays = 0
UsedDays = 0
Spaced = False

print(f"                               {Months[Month - 1]}, {Year}                                            ")

for line in Calender.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            if Spaced == False: print(' ', end='')
            else: 
                print('', end='')
                Spaced = False
        elif bit == 'x':
            def startmonth():
                global UsedDays
                global DaysInMonth
                global Spaced

                if UsedDays == 0: UsedDays = 1
                else: UsedDays += 1

                if UsedDays <= DaysInMonth: 
                    print(UsedDays, end='')
                else: 
                    UsedDays = 1
                    print(UsedDays, end='')

                if UsedDays > 9 and UsedDays <= DaysInMonth: Spaced = True

            if WeekDay != 6:
                if UsedOldDays == 0: UsedOldDays = DaysInOldMonth - WeekDay
                else: UsedOldDays += 1

                if UsedOldDays <= DaysInOldMonth: 
                    print(UsedOldDays, end='') 
                else: startmonth()

                if UsedOldDays > 9 and UsedOldDays <= DaysInOldMonth: Spaced = True
            else:
                startmonth()
        else:
            # Print a character from the message:
            print(bit, end='')
    print() # Print a newline.