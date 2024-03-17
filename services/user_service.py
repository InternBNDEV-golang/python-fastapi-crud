# Importing necessary modules and classes from the project and external libraries.
from repositorys.user_repository import UserRepository
from schemas.user import user_serializer, users_serializer
from models.user import User
from datetime import datetime
from fastapi import HTTPException
import bcrypt

# Service class for handling user-related operations.
class UserService:
    def __init__(self, user_repository: UserRepository):
        # Constructor to initialize the service with a user repository.
        self.user_repository = user_repository

    def get_all_users(self):
        # Retrieve all users from the repository and serialize them for API response.
        users = self.user_repository.get_all_users()
        return users_serializer(users)

    def get_user_by_id(self, user_id):
        # Retrieve a user by ID from the repository and serialize for API response.
        user = self.user_repository.get_user_by_id(user_id)
        return user_serializer(user)

    def create_user(self, user: User):
        # Hash the password and create a user in the repository, then serialize for API response.
        user_data = dict(user)
        user_data['password'] = self._hash_password(user.password)
        created_user = self.user_repository.create_user(user_data)
        return user_serializer(created_user)

    def update_user(self, user_id, updated_user: User):
        # Update a user in the repository and serialize the updated user for API response.
        updated_data = dict(updated_user)
        updated_user = self.user_repository.update_user(user_id, updated_data)
        return user_serializer(updated_user)
    
    def patch_user(self, user_id, updated_data: dict):
        # Patch a user in the repository, handling password hashing, and serialize for API response.
        existing_user = self.user_repository.get_user_by_id(user_id)

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        for field, value in updated_data.items():
            if field == "password":
                value = self._hash_password(value)
            existing_user[field] = value

        existing_user['updatedAt'] = datetime.utcnow()
        updated_user = self.user_repository.update_user(user_id, existing_user)
        return user_serializer(updated_user)

    def delete_user(self, user_id):
        # Delete a user from the repository and serialize the deleted user for API response.
        deleted_user = self.user_repository.delete_user(user_id)
        return user_serializer(deleted_user)
    
    def _hash_password(self, password):
        # Hash the password using bcrypt.
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')