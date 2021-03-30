#!/usr/bin/env python3

import os.path
from os import path, listdir #These allow us to use the 'exists' function on file names and make a list of files in current directory
import csv
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def nameToEmail(filename):
    mydict = {}
    wdFilenames = listdir() #A list of strings, each of which is the file name of a file in the working directory
    with open(filename) as csvfile:
        myreader = csv.reader(csvfile)
        for row in myreader:
            L = row[0].split() #csv.reader(...) creates an object with rows, such that each row has indexed parts
            lastnamefirstnamemi = L[0][:-1].lower() + L[1].lower()
            if len(L) == 3:
                lastnamefirstnamemi = lastnamefirstnamemi + L[2].lower()
            email = row[2] + '@scarletmail.rutgers.edu'
            for name in wdFilenames:
                if lastnamefirstnamemi == name[:len(lastnamefirstnamemi)]:
                    mydict[email] = name
    return mydict
        

def main():
    emailFileDict = nameToEmail('studentNameIDs.csv')

    sender = #REMOVED FOR PRIVACY
    password = #REMOVED FOR PRIVACY
    server = 'smtp.gmail.com'
    port = 465 #This is the port that works with SSL
    server = smtplib.SMTP_SSL(server, port)
    server.login(sender, password)

    for key in emailFileDict:
        message = MIMEMultipart()
        message['Subject'] = "Linear Algebra HW 2.4, Graded"
        message['From'] = sender
        message['To'] = key
        text = MIMEText('Dear Student,\n If we have your graded homework on section 2.4, you will find it attached to this email.\n Best,\n Charles')
        message.attach(text)
        file = emailFileDict[key]
        with open(file, 'rb') as opened:
            openedfile = opened.read()
        attachedfile = MIMEApplication(openedfile, _subtype = 'pdf') #MIMEApplication is used to send pdf files; for images, there's another thing called MIMEImage
        attachedfile.add_header('content-disposition', 'attachment', filename = file)
        message.attach(attachedfile)
        server.sendmail(message['From'], message['To'], message.as_string())
    
    server.quit()
    return


if __name__ == '__main__':
    main()
