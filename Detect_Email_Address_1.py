import re

def email_identification(sent):
    email_identified = re.findall('[\w\-\.]+[@]+[a-z]+[\.]+[a-z]{2,3}', sent)
    return email_identified



sent = input("Enter the string:  ")
result = email_identification(sent)

print(result)

