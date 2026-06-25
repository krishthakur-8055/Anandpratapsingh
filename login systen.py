# Login sysytem project
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register
username = input("Create username: ")
password = input("Create password: ")

stored_user = username
stored_pass = hash_password(password)

print("\n--- LOGIN ---")

# Login
u = input("Username: ")
p = input("Password: ")

if u == stored_user and hash_password(p) == stored_pass:
    print("Login Successful")
else:
    print("Access Denied")