from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders
import smtplib as sender

def send(filename):
    #who is sending 
    from_add = "YOUR EMAIL ADRESS"
    #who is receiving
    to_add =  "TARGET EMAIL ADRESS"

    subject = "Finance Stock Report"

    msg = MIMEMultipart()
    msg["From"] = from_add
    msg["To"] = to_add
    msg["Subject"] = subject

    body = "You can find todays finance report attached!"
    msg.attach(MIMEText(body, "plain"))

    my_file = open(filename, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload((my_file).read()) #this 4 attachment
    encoders.encode_base64(part) #this for security things. teacher said no need to know
    part.add_header("Content-Disposition", "attachment; filename= " + filename)


    msg.attach(part)
    message = msg.as_string()



    server = sender.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_add, "YOUR EMAIL APP PASSWORD")


    server.sendmail(from_add, to_add, message)

    server.quit()