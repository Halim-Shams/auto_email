import smtplib


# TYPE YOUR GMAIL 👇
my_email = 'Your Gmail'
# TYPE YOUR 16-digit PASSWORD 👇
password = ''


# CONNECTION SECTION
connection  = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs='halimshams1234@gamil.com', msg='Hello')
connection.close()