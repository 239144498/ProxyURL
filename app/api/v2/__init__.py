from fastapi import *
from .endpoints import *

v2 = APIRouter()

v2.include_router(tv)
