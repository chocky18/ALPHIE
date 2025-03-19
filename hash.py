import bcrypt

# Your plain password
password = b"Naruto@18"

# Hash the password using bcrypt
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

print(f"Hashed password: {hashed_password.decode()}")
