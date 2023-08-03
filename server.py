import os, smtplib, time
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = os.environ.get('PORTFOLIO_FLASK_SECRET_KEY')
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def home():
    """return homepage"""

    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    """return portfolio"""

    return render_template("portfolio.html")


@app.route("/about")
def about_me():
    """return about me"""

    return render_template("about.html")


@app.route("/contact")
def contact():
    """return contact"""

    return render_template("contact.html")


@app.route("/blog")
def blog():
    """return blog"""

    return render_template("blog.html")



@app.route("/contact-me", methods=["GET", "POST"])
def contact_me():
    """send info from contact form to personal email"""

    print(request.form.values())

    recipients= "fernanda.portfolio.contactme@gmail.com"
    name = request.form.get("inquirer_name")
    email = request.form.get("inquirer_email")
    message = request.form.get("inquirer_message")
    gmail_password = os.environ.get('PORTFOLIO_GMAIL_PASSWORD')
    body = f"Inquirer name: {name}\nInquirer email: {email}\n\n\n {message}"
    print(name, email, message)

    print(recipients, gmail_password)

    msg = MIMEText(body)
    msg['Subject'] = "Portfolio Form Inquiry"
    msg['From'] = email
    # msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(recipients, gmail_password)
    smtp_server.sendmail(email, recipients, msg.as_string())
    smtp_server.quit()
    time.sleep(2)
    

    return redirect("/contact")






if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)