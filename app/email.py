from threading import Thread
from flask import render_template
from flask_mail import Message
from app import mail
from flask import current_app
import logging

def async_send_email(msg):
    with current_app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    try:
        mail.send(msg)
        current_app.logger.info(f"Email sent to {recipients}")
    except Exception as e:
        current_app.logger.error(f"Failed to send email to: {e}")
    Thread(target=async_send_email, args=(current_app._get_current_object(), msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    msg = Message('[Microblog] Reset Your Password',
                  sender=current_app.config['ADMINS'][0],
                  recipients=[user.email])
    msg.body = render_template('email/reset_password.txt', user=user, token=token)
    msg.html = render_template('email/reset_password.html', user=user, token=token)
    mail.send(msg)