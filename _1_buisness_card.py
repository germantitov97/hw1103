name = input("Enter your name: ")
email = input("Enter your email: ")
phone_number = input("Enter your phone number: ")
job_title = input("Enter your job title: ")

user_info = {
    "name": name,
    "email": email,
    "phone_number": phone_number,
    "job_title": job_title
}

print(user_info)
print()
print("--- Buisness Card ---")
print(f"Name: {user_info['name']}")
print("Email:", user_info['email'])
print(f"Phone number: {user_info['phone_number']}")
print(f"Job title: {user_info['job_title']}")
