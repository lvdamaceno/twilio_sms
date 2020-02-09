from twilio.rest import Client
import variables as var
import csv


def t_message(sms_message, contact_to):
    client = Client(var.account_sid, var.auth_token)
    return client.messages.create(body=sms_message,
                                  from_=var.contact_from,
                                  to=f'+55{contact_to}')


def send_from_csv(csv_file, text):
    with open(csv_file) as contact_list:
        contacts = csv.reader(contact_list, delimiter=',')
        for contact in contacts:
            message = t_message(text, contact)
            print(message.sid)


send_from_csv('contacts.csv', 'message')
