import smtplib
import datetime as dt
import random

# TYPE YOUR GMAIL 👇
EMAIL = 'Your Gmail'
# TYPE YOUR 16-digit PASSWORD 👇
PASSWORD = ''

now = dt.datetime.now()
day = now.weekday()
if day == 5:
    quote_file = open('quote.txt', encoding='utf8')
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
    quote_file.close()

    print(quote)

    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=EMAIL, 
        to_addrs='halimshams.online@gmail.com', #👈 CHANGE THIS EMAIL TO WHO YOU WANNA SEND YOUR EMAIL
        msg=f'Subject:Monday Motivation\n\n{quote}'
    )
    connection.close()