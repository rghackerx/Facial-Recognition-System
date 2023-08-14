# import Gui
import random
import smtplib
import getpass

def generate_otp(length=6):

    digits = "0123456789"
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp

# Generate OTP
generate_otp1 = generate_otp()
print(generate_otp1)

"""
#user creds
sender_email = "frdb1111@yahoo.com"
sender_password = "Hello@123"

# Set up the email content
# r_email = Gui.e1.get()
receiver_email = "ramangautam0908@gmail.com"
subject = "Your OTP Code"
body = f"Your OTP code is: {otp}"

# Connect to Gmail's SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Log in to Gmail account
server.login(sender_email, sender_password)

# Sending the email
server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{body}")

# Closing the server
server.quit()

print("Email sent successfully!")

"""