# Serialization function to convert a single user document to a dictionary.
def user_serializer(user) -> dict:
    # Create a dictionary with selected fields from the user document.
    serialized_user = {
        "id": str(user["_id"]),  # Convert ObjectId to string for JSON serialization.
        "name": user["name"],
        "password": user["password"],
    }

    # Check if timestamp fields exist in the user document and include them in the serialized user.
    if "createdAt" in user:
        serialized_user["createdAt"] = user["createdAt"]
    if "updatedAt" in user:
        serialized_user["updatedAt"] = user["updatedAt"]
    if "deletedAt" in user:
        serialized_user["deletedAt"] = user["deletedAt"]

    return serialized_user


# Serialization function to convert a list of user documents to a list of dictionaries.
def users_serializer(users) -> list:
    # Use the user_serializer function for each user in the list and return the resulting list.
    return [user_serializer(user) for user in users]
