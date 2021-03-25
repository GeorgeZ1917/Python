import smtplib
import string
from time import sleep

username = 'capacitacion@centrodeconsultoria.org'
password = 'Ventas2%'
HOST = "smtp.office365.com: 587"
SUBJECT = "Test email from Python"
TO = "jorge.z2020@outlook.com"
FROM = "capacitacion@centrodeconsultoria.org"
server = smtplib.SMTP ( HOST )
server.starttls()
server.login ( username, password )
for i in range ( 0, 5 ) :
	text = "Mensaje " + str ( i ) + " de 5"
	BODY = "\r\n".join ( ( "From: %s" % FROM, "To: %s" % TO, "Subject: %s" % SUBJECT, "" , text ) )
	server.sendmail ( FROM, [ TO ], BODY )
	sleep ( 2 )
server.quit()