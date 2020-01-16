import re 
while True:
    today_date = input('Enter todays day/month/year): ')
    birthday_date = input('Enter birthday day/month/year): ')
    print('')
    # This line makes sure that the user's inputs are correct
    # if not it will print a message and the user will enter them again.
    if re.search(r'\d{1,2}/\d{1,2}/\d{4}', today_date) is None or re.search(r'\d{1,2}/\d{1,2}/\d{4}', birthday_date) is None:
        print('You have entered a wrong number! ')
        print('')
        continue
    # This will convert the user's input into lists to use them in assigning values.
    today_date = today_date.split('/')
    birthday_date = birthday_date.split('/')

    # This line assigns spefic year's, month's and day's values.
    today_year, today_month, today_day = int(today_date[2]), int(today_date[1]), int(today_date[0])
    # This line specifies birth year's, month's and day's values.
    birthday_year, birthday_month, birthday_day = int(birthday_date[2]), int(birthday_date[1]), int(birthday_date[0])
    # These lines are for math rules.
    if today_day < birthday_day:
        today_day += 30
        today_month -= 1
    if today_month < birthday_month:
        today_month += 12
        today_year -= 1
    # These lines calculate years, months and days.  
    year = str(today_year - birthday_year) + ' years, '
    month = str(today_month - birthday_month) + ' months and '
    day = str(today_day - birthday_day) + ' days. '
    # These lines are for grammar rules.
    if today_year - birthday_year < 2:
        year = year.replace('years', 'year')
    if today_month - birthday_month < 2:
        month = month.replace('months', 'month')
    if today_day - birthday_day < 2:
        day = day.replace('days', 'day')
    print('Your age is: ' + year + month + day)
    print('')