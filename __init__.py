from fastapi import FastAPI
import uvicorn
from routes import routes
from config import Settings
from config import settings
from db import init_db




    

def create_app():
    app = FastAPI(
        description="This is a simple REST API for a news",
        title="News",
        version=settings.VERSION
    )
    init_db()
    app.include_router(routes)
    return app


app = create_app()

if __name__=='__main__':
    uvicorn.run("__init__:app", reload=True)