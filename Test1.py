days = int(input("Enter the day: "))
if days > 31:
    print("Error: Invalid Day Input")

month = int(input("Enter the month: ",))
if month > 12:
    print("Error: Invalid Month Input")

year = int(input("Enter the year: "))
if year > 99:
    print("Error: Invalid Year Input")

date = days, month, year

if month == 2:
    if days > 29:
        print("Error Not Vaild Day in feburary")
    elif days <= 31 and month <= 12 and year <= 99:
        print("Success: Congratulations! You entered a correct date:", date)
    else:
        print("Error: There is no such date in the calendar")
