from airondatarepository.userrepository import UserRepository
import test_constants

repository = UserRepository()
result = repository.delete_user(test_constants.EMAIL)

if result == False:
    print("Failed to delete")
else:
    print("Delete user succeeded")