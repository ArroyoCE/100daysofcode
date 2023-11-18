import re

email = input("What's you e-mail? ")

if re.search(r"^\w+[a-z0-9_\.]*@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid.")
else:
    print("Invalid.")
