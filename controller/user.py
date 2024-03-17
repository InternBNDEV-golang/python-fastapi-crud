# Importing necessary modules and classes from FastAPI, services, repository, and models.
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.user_service import UserService
from repositorys.user_repository import UserRepository
from models.user import User

# Creating instances of UserRepository and UserService.
user_repository = UserRepository()
user_service = UserService(user_repository)

# Creating an APIRouter instance.
router = APIRouter()

# Endpoint to retrieve all users.
@router.get("/")
async def get_users():
    users = user_service.get_all_users()
    return {"status": "ok", "data": users}

# Endpoint to retrieve a user by ID.
@router.get("/{id}")
async def get_user(id: str):
    user = user_service.get_user_by_id(id)
    return {"status": "ok", "data": user}

# Endpoint to create a new user.
@router.post("/")
async def post_user(user: User):
    created_user = user_service.create_user(user)
    return {"status": "ok", "data": created_user}

# Endpoint to update a user by ID.
@router.put("/{id}")
async def update_user(id: str, refUser: User):
    updated_user = user_service.update_user(id, refUser)
    return {"status": "ok", "data": updated_user}

# Endpoint to partially update a user by ID.
@router.patch("/{id}")
async def patch_user(id: str, updated_data: dict):
    try:
        patched_user = user_service.patch_user(id, updated_data)
        return {"status": "ok", "data": patched_user}
    except HTTPException as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=e.status_code)

# Endpoint to delete a user by ID.
@router.delete("/{id}")
async def delete_user(id: str):
    deleted_user = user_service.delete_user(id)
    return {"status": "ok", "data": deleted_user}