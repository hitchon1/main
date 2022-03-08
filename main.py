import smtplib
import time 
from datetime import datetime as dt

#sntpalextest1
#sntpalextest9999

sender = "sntpalextest1@outlook.com"
reciever = "stefanhitchon@icloud.com"
password ="sntpalextest9999"
message="Hey stefan today is my "
message2 = " day of coding"
daysOfCoding = 1


server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,reciever,      (message+str(daysOfCoding)+message2))
daysOfCoding+=1
server.quit()
#time.sleep(60)
print("sent",(message+str(daysOfCoding)+message2) )
