import uvicorn 
from fastapi import FastAPI
from api.routes.router import api_router
from core.config import (APP_VERSION,APP_NAME,API_PORT)
from core.event_handlers import (start_app_handler, stop_app_handler)

def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION)
    fast_app.include_router(api_router)

    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))

    return fast_app


app = get_app()

if __name__=='__main__':
    uvicorn.run('main:app', host= '0.0.0.0', port=API_PORT, reload=True) # reload is set to False in production