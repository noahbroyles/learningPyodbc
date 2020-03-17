import re, insertEmail, checkEmail
from requests_html import HTMLSession

url = "https://www.randomlists.com/email-addresses?qty=10"
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# initiate an HTTP session
session = HTMLSession()

# get the HTTP Response
r = session.get(url)

# use this for JAVA-Script driven websites
r.html.render()

emails = []
checkValid = True
for reMatch in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    # Disallow duplicates
    ce = reMatch.group()
    if not ce in emails:
        if checkValid:
            if (checkEmail.checkEmail(ce)): # validate emails
                emails.append(ce)
                print(ce, "is valid")
        else:
            emails.append(reMatch.group())
print()
print(str(len(emails)), "email addresses were added from", url)
insertEmail.insertEmails(emails)