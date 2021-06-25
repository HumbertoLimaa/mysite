import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# The mail addresses and password
sender_address = 'biscoitocaindo@gmail.com'
sender_pass = '12qw!@QW'
receiver_address = 'humbertolimaa@gmail.com'


def send_email(last, low, diff, high):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address

    # The subject line
    mail_content = 'Última: ' + str(last) + ' Mais Baixa: ' + str(low) + \
        ' Mais Alta: ' + str(high) + ' Diff: ' + str(diff)

    message['Subject'] = 'Biscoito Caindo.' + mail_content

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
