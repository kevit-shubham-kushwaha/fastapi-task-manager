from .base_repository import BaseRepository
from utils.libs.db.config import (fastapi_user_collection)


user_collection_instance = BaseRepository(fastapi_user_collection)


