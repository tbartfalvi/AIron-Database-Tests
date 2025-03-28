from airondatarepository.userrepository import UserRepository

repository = UserRepository()
result = repository.delete_user("todd@test.com")

if result == False:
    print("Failed to delete")
else:
    print("Delete user succeeded")