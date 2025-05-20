from .base_repository import BaseRepository
from utils.libs.db.config import (fastapi_user_collection,fastapi_task_collection)


user_collection_instance = BaseRepository(fastapi_user_collection)
task_collection_instance = BaseRepository(fastapi_task_collection)

