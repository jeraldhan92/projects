from fastapi import APIRouter
from api.routes import predict


api_router = APIRouter()
api_router.include_router(predict.router, tags=["questions"])
api_router.include_router(predict.router, tags=["answer"])