from emailverifier import Client
from emailverifier import exceptions

def checkEmail(emailAddr):
    client = Client('you gotta be crapping me')
    try:
        data = client.get(emailAddr)
        # print("Email address: " + data.email_address)
        # print("Format: " + str(data.format_check))
        # print("DNS: " + str(data.dns_check))
        # print("SMTP: " + str(data.smtp_check))
        # print("Catch all: " + str(data.catch_all_check))
        # print("Disposable: " + str(data.disposable_check))
        # print("Free: " + str(data.free_check))
        # print("Last audit date: " + str(data.audit.audit_updated_date))
        if (data.dns_check and data.smtp_check):
            return True
        else:
            return False
    except:
        print("Something crappy happened. Not sure what.")
