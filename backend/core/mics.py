######### This class is for a variety of purposes
#####
import json
import re
import uuid

import requests as requests_library
from django.conf import settings
from django.contrib.auth import *
from django.contrib.auth.tokens import *
from django.core.mail import *
from django.template.loader import render_to_string
from django.urls import *
from django.utils.encoding import *
from django.utils.html import *
from django.utils.http import *
from django.utils.safestring import *
from ipware import get_client_ip
from sendgrid import *
from sendgrid.helpers.mail import *
from werkzeug.useragents import UserAgent


# replaced by logic in contrib.auth.tokens
def http_headers(request):
    """ extracts HTTP headers from client's request
    """
    ua = UserAgent(request.META["HTTP_USER_AGENT"])

    operating_system = ua.platform
    browser = ua.browser
    browser_version = ua.version

    return [operating_system, browser, browser_version]


def get_uid_token(request):
    """
    string that one gets is
    /new_password/NQ/504-56db758854211636d9fc/
    regex for token = re.compile(r'(/.*/(.*)/)')
    regex for uid part: (/.*/(.*)/(.*)/)
    """
    current_url = request.get_full_path()
    uid = current_url.split("/")[2]
    token = current_url.split("/")[3]

    return [uid, token]


def validate_password_reset(request):
    """
    Take current URL and check whether token matches what one expects
    Borrowed from https://github.com/mhacks/mhacks-admin/blob/master/MHacks/utils.py#L143
    """
    my_user_model = get_user_model()
    tkn = PasswordResetTokenGenerator()
    uid, token = get_uid_token(request)

    users_pk = urlsafe_base64_decode(uid).decode()
    us = my_user_model.objects.get(pk=users_pk)

    if us is not None and tkn.check_token(us, token):
        return us
    else:
        print("token is not valid")
        return None


def prepare_psswd_reset_email(
    request,
    userPresent_username=None,
    userPresent_email=None,
    userPresent_token=None,
    userPresent_uid=None,
):
    """
    This functions sends email to users, directly!
    """
    subject = "B40.cz: Password Reset"
    smtp_email = settings.DEFAULT_FROM_EMAIL

    # fetch user metadata including ip address
    client_headers = http_headers(request)
    client_ip, is_routable = get_client_ip(request)

    cntxt = {
        "username": userPresent_username,
        "token": userPresent_token,
        "password_expire": settings.PASSWORD_RESET_TIMEOUT_DAYS,
        "uid": userPresent_uid,
        "operating_system": client_headers[0],
        "ip_address": client_ip,
        "browser": client_headers[1],
        "browser_version": client_headers[2],
    }

    html_message = render_to_string("reset_password_email.html", cntxt)
    # plain_message = strip_tags(html_message)

    message = Mail(
        from_email=smtp_email,
        to_emails=userPresent_email,
        subject=subject,
        html_content=html_message,
    )
    try:
        response = settings.SENDGRID_API_KEY.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

    # try:
    # 	send_mail(subject, plain_message, smtp_email, [userPresent_email], html_message=html_message)
    # except BadHeaderError:
    # 	return HttpResponse('Invalid header found.')

    return None


def prepare_visitor_mssg_email(
    request,
    userPresent_username=None,
    userPresent_email=None,
    subject=None,
    text_msg=None,
):
    """
    For internal use, e.g. feedback, contact etc.
    """
    subject = "B40.cz: Message from the user/visitor: " + subject
    smtp_email = settings.DEFAULT_FROM_EMAIL
    my_email = settings.MY_EMAIL
    from_email = userPresent_email

    client_headers = http_headers(request)
    client_ip, is_routable = get_client_ip(request)

    cntxt = {
        "username": userPresent_username,
        "from_email": from_email,
        "text_msg": text_msg,
        "operating_system": client_headers[0],
        "ip_address": client_ip,
        "browser": client_headers[1],
        "browser_version": client_headers[2],
    }

    html_message = render_to_string("new_visitor_email.html", cntxt)
    plain_message = strip_tags(html_message)

    try:
        send_mail(
            subject, plain_message, smtp_email, [my_email], html_message=html_message
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")

    return None


def upload_profile_image(instance, filename):
    """
    Function used by the user model to upload to Azure avatars
    https://djangowohnreal1.blob.core.windows.net/images-profile-pictures/user-profile-photos/user_id_UUID
    """
    azure_folder = "user-profile-photos/"
    # user_id_UUID
    URL_path = "_".join(["user", str(instance.id), str(uuid.uuid4())])
    return azure_folder + URL_path
