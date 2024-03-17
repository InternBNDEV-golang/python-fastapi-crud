# Importing necessary modules from the project and external libraries.
from config.database import user_collection
from bson import ObjectId
from datetime import datetime
import bcrypt
import pytz

# Repository class for interacting with the 'users' collection in MongoDB.
class UserRepository:
    def get_all_users(self):
        # Retrieve all users from the collection.
        return user_collection.find()

    def get_user_by_id(self, user_id):
        # Retrieve a user by ID from the collection.
        return user_collection.find_one({"_id": ObjectId(user_id)})

    def create_user(self, user_data):
        # Add creation timestamp and hash the user's password before inserting into the collection.
        user_data['createdAt'] = self._get_thai_time()
        user_data['password'] = self._hash_password(user_data['password'])
        # Insert the user data into the collection and retrieve the inserted user.
        result = user_collection.insert_one(user_data)
        inserted_user = user_collection.find_one({"_id": result.inserted_id})
        return inserted_user

    def update_user(self, user_id, updated_data):
        # Add update timestamp and hash the updated password before updating the user.
        updated_data['updatedAt'] = self._get_thai_time()
        if 'password' in updated_data:
            updated_data['password'] = self._hash_password(updated_data['password'])
        # Update the user in the collection and retrieve the updated user.
        return user_collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": updated_data},
            return_document=True
        )

    def delete_user(self, user_id):
        # Soft delete: add deletion timestamp and remove the user from the collection.
        deleted_user = self.get_user_by_id(user_id)
        deleted_user['deletedAt'] = self._get_thai_time()
        user_collection.find_one_and_delete({"_id": ObjectId(user_id)})
        return deleted_user
    
    def _hash_password(self, password):
        # Hash the password using bcrypt.
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')    
    
    def _get_thai_time(self):
        # Get the current time in the Thai timezone.
        thai_timezone = pytz.timezone('Asia/Bangkok')
        return datetime.now(thai_timezone)