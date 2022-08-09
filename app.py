# importing required modules/packages
from flask import *
import smtplib, ssl
from email.message import EmailMessage

app = Flask(__name__)

# if successful - currently it does nothing if it was unsuccessful
@app.route("/success")
def success():
    return render_template("success.html")

# mail function for Savir Singh (creator)
@app.route("/mailsavir", methods=["POST"])
def mailsavir():
    email = request.form["address"]
    message = request.form["important"]
    EMAIL_ADDRESS = 'THEEMAIL'
    EMAIL_PASSWORD = 'THEPASSWORD'
    
    msg = EmailMessage()
    msg['Subject'] = (email)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'your_email'

    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return redirect("/success")

# running it
if __name__ == '__main__':
    app.run(debug=True)
