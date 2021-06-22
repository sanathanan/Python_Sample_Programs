import re

def email_identification(sent):
    email_identified = re.findall('\S+@\S+', sent)
    return email_identified


sent = input(" ")
result = email_identification(sent)

print(result)

