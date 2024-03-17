# Importing necessary modules from Pydantic and regular expressions.
from pydantic import BaseModel, constr, validator
import re

# Defining a Pydantic model for representing user data.
class User(BaseModel):
    # Defining constraints for the 'username' field (minimum length is 1).
    username: constr(min_length=1)
    
    # Defining constraints for the 'password' field (minimum length is 8).
    password: constr(min_length=8)

    # Custom validator for the 'password' field to enforce additional rules.
    @validator("password")
    def validate_password(cls, v):
        # Check if password contains at least one uppercase letter.
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain at least one uppercase letter")

        # Check if password contains at least one lowercase letter.
        if not any(char.islower() for char in v):
            raise ValueError("Password must contain at least one lowercase letter")

        # Check if password contains at least one digit.
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit")

        # Check if password contains at least one special character.
        special_characters = r"[!@#$%^&*(),.?\":{}|<>]"
        if not re.search(special_characters, v):
            raise ValueError("Password must contain at least one special character")

        # If all checks pass, return the validated password.
        return v
