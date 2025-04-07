password_list = ["a","b","c","d"]
correct_password = "d"

for password in password_list:
    print(f"Trying this password: {password}")
    if password == correct_password:
        print(f"This is the correct password: {password} successful login")
    else:
        print(f"This is the incorrect password: {password}")