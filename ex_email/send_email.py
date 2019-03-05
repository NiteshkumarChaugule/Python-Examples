import smtplib

sender = "test.me.nitesh@gmail.com"
receiver = "chaugule.nitesh@gmail.com"
message = """import smtplib

sender = "test.me.nitesh@gmail.com"
receiver = "chaugule.nitesh@gmail.com"
message = "this message is from python"
server = "smtp.gmail.com"
port = 465
password = "Atest@4321"

mail = smtplib.SMTP_SSL(server, port)
mail.login(sender, password)
mail.sendmail(sender, receiver, message)
mail.quit()
"""
server = "smtp.gmail.com"
port = 465
password = "Atest@4321"

mail = smtplib.SMTP_SSL(server, port)
mail.login(sender, password)
mail.sendmail(sender, receiver, message)
mail.quit()
