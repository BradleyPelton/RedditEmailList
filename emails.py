import smtplib, ssl

#https://realpython.com/python-send-email/

#advtesttwitch1 email is banned? switching to advtesttwitch3

smtp_server = 'smtp.gmail.com'
port = 465  # For SSL

sender = 'advtesttwitch3@gmail.com'
receiver = 'advtesttwitch3@gmail.com'
password = input("enter the sender password:")

# Create a secure SSL context
context = ssl.create_default_context()


server = smtplib.SMTP_SSL(smtp_server, port)
server.login(sender,password)
server.sendmail(sender, receiver, "Hello, world from email")
server.quit()


# with smtplib.SMTP_SSL(smtp_server, port) as server:
#     server.login(sender, password)
#     print("reached here")
#     # TODO: Send email here
