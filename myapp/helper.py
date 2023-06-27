# # from django.conf import settings
# # from django.core.mail import EmailMessage
# # from django.template.loader import render_to_string
# # from django.utils.html import strip_tags

# # def send_forget_password_mail(email, token):
# #     subject = 'Your forget password link'
# #     html_message = render_to_string('myapp/forgetpassword.html', {'token': token})
# #     plain_message = strip_tags(html_message)
# #     email_from = settings.EMAIL_HOST_USER
# #     recipient_list = [email]

# #     email = EmailMessage(subject, plain_message, email_from, recipient_list)
# #     email.content_subtype = 'html'
# #     email.send()

# #     return True



# from django.template.loader import render_to_string
# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.utils.html import strip_tags
# import random
# import string

# def generate_random_token(length):
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for _ in range(length))

# def send_forget_password_mail(email):
#     subject = 'Your forget password link'
#     token = generate_random_token(10)
#     link = f'http://127.0.0.1:8000/conform_password/'
#     message = f'Please click on the link below to reset your password:\n{link}'

#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]

#     email = EmailMessage(subject, message, email_from, recipient_list)
#     email.send()

#     return True



from django.core.mail import send_mail
from django.conf import settings

def send_forget_password_mail(email, token):
    subject = 'Password Reset Request'
    message = f'Click the link below to reset your password:\n\n{settings.BASE_URL}/conform_password/?token={token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
