
def is_valid_email(email):
 email_pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
    
    # Use re.match() to check if the email matches the pattern
 if(email_pattern== email):
        return True
 else:
        return False
email = input("Enter an email address: ")
if is_valid_email(email):
    print(email," is Valid email")
else:
    print(email,"is not vaild email")
