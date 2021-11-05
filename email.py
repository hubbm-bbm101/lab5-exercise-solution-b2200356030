def is_mail(mail):
    
    if "@" in mail and "." in mail:
        return True
    
    else:
        return False
    
    
e_mail = input("enter your mail : ")    

print("your email is :", is_mail(e_mail))