import smtplib
print('sanity3')

username = 'andrewbeattycourse@gmail.com'
password = 'notS3cure'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
'''
server.ehlo()
server.starttls()
server.ehlo()
'''
#Next, log in to the server
server.login(username, password)

#Send the mail
msg = "Hello! # The /n separates the message from the headers"

server.sendmail(username, "andrew.beatty@gmit.ie", msg)
