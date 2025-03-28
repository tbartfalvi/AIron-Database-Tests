from airondatarepository.user import User
from airondatarepository import encrypt
from airondatarepository.userrepository import UserRepository

user = User("Todd Test", "todd@test.com", encrypt.encrypt_password("access"))
repository = UserRepository()
id = repository.insert_user(user)
print(id)

if id == -9999:
    print("Test Failed")
else:
    print("Test Passed")