def check_weekday_or_weekend(day_number):
    if day_number < 1 or day_number > 7:
        return "Not a proper day number!"
    
    if 1 <= day_number <= 5:
        return "It is a Weekday!"
    else:
        return "It is a Weekend!"

def get_day_name(day_number):
    if day_number == 1:
        return "It is a Monday!"
    elif day_number == 2:
        return "It is a Tuesday!"
    elif day_number == 3:
        return "It is a Wednesday!"
    elif day_number == 4:
        return "It is a Thursday!"
    elif day_number == 5:
        return "It is a Friday!"
    elif day_number == 6:
        return "It is a Saturday!"
    elif day_number == 7:
        return "It is a Sunday!"
    else:
        return "Not a proper day of the week!"


# first program
day_num = int(input("Enter a day number (1-7): "))
result1 = check_weekday_or_weekend(day_num)
print(result1)

# second program
day_num2 = int(input("Enter a day number (1-7): "))
result2 = get_day_name(day_num2)
print(result2)
