import datetime, random

startOfYear = datetime.date(2001, 1, 1)

NumberOfBirtdays = int(input("Cuantos cumpleaños generar: "))
NumberOfTests = int(input("Cuantas pruebas hacer: "))

NumberOfMatches= 0

for i in range(NumberOfTests):
    birthdays = []

    for i in range(NumberOfBirtdays):
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    if len(birthdays) != len(set(birthdays)): NumberOfMatches += 1

ChanceToMatch = (NumberOfMatches * 100) / NumberOfTests

print("Parejas encontradas: ", NumberOfMatches)
print("Las probabilidades de que en un grupo de ", NumberOfBirtdays, " personas hayan al menos 2 personas con el mismo cumpleaños son de: ", round(ChanceToMatch, 2),"%", sep="")


