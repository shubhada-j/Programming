#Design automation script which accept directory name and 
#mail id from user and create log file in that directory which contains information of running processes as 
#its name, PID, Username. After creating log file send that log file to the specified mail.

import sys
import os
import time
import psutil
import smtplib
from email.message import EmailMessage

def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        listprocess.append(info)
           
    return listprocess

def SendMail(FileName, ReceiverMail):
    sender = "shubhada3371@gmail.com"
    password = "tnfe yhdk extu uike"
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = ReceiverMail
    msg["Subject"] = "Process Information Log File"
    msg.set_content("Attached is the process information log file.")

    try:
        with open(FileName,"rb") as fobj:
            FileData = fobj.read()
            FileNameOnly = os.path.basename(FileName)
            msg.add_attachment(FileData,maintype="application",subtype="octet-stream",filename=FileNameOnly)

        smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
        smtp.login(sender,password)
        smtp.send_message(msg)
        smtp.close()
        print("Mail sent successfully")
    except Exception as e:
        print("Unable to send mail :",e)

def Display(FolderName, MailID):
    if os.path.exists(FolderName):
        if not os.path.isdir(FolderName):
            print("Name exists but it is not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join( FolderName,"Marvellous_%s.log" % timestamp)

    try:
        fobj = open(FileName,"w")
        print("Log file created :",FileName)

    except Exception as e:
        print("Unable to create log file :",e)
        return

    Data = ProcessScan()

    for info in Data:

        fobj.write("-----------------------------------\n")
        fobj.write("PID        : %s\n" % info.get("pid"))
        fobj.write("Name       : %s\n" % info.get("name"))
        fobj.write("Username   : %s\n" % info.get("username"))

    fobj.close()

    SendMail(FileName,MailID)

def main():
    if len(sys.argv) != 3:

        print("Invalid Number Of Arguments")
        print("Usage :")
        print(f"python {sys.argv[0]} Folder_Name Mail_ID")
        return

    if sys.argv[1] == "--h" or sys.argv[1] == "--H":

        print("This automation script creates process log")
        print("and sends log file through mail")

    elif sys.argv[1] == "--u" or sys.argv[1] == "--U":

        print("Usage :")
        print(f"python {sys.argv[0]} Folder_Name Mail_ID")

    else:

        FolderName = sys.argv[1]
        MailID = sys.argv[2]

        Display(FolderName,MailID)

if __name__ == "__main__":
    main()