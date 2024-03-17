# Importing necessary modules and classes from the FastAPI framework.
from fastapi import FastAPI
from controller.user import router  # Assuming the user router is defined in the 'controller.user' module.

# Creating a FastAPI application instance.
app = FastAPI()

# Including the user router in the application.
app.include_router(router)
