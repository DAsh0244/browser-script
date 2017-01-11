# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

'''PUT EMAIL/PWD HERE'''
usr = 'TotallyLegitEmailHere@mail.com'
pwd = 'TotallySecurePasswordHere1!'


# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText('Mesage goes here')  # fp.read())
# fp.close()


msg['Subject'] = 'Event Triggered'
msg['From'] = 'sender@mail.com'
msg['To'] = usr

def send_mail ():
	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.login(usr, pwd)
	smtpserver.send_message(msg)
	smtpserver.close()
	

if __name__ == '__main__':
	send_mail()