from typing import Annotated
from fastapi import APIRouter, Depends, Form, Request, FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session
import db
import models
import news

from datetime import datetime

templates = Jinja2Templates(directory="templates")

routes = APIRouter(
    prefix="", responses={400: {"description": "Not found"}}, tags=["auth"]
)


@routes.get("/")
def home(request: Request):
    """Hello home"""
    #dogs = [{"name":"Milo","type":"Golden Retriever"},{"name":"Jax","type":"German Shepard"}]
    #data = sentiment.readSite()
    #df = sentiment.scoredf(data)
    #print(df.head())
    #dictdata = df.to_dict('records')
    #print(dictdata)
    
    with db.get_session() as session:
        stmt = select(models.Headlines)
        result = session.execute(stmt) 
        res = result.all()
        
    return templates.TemplateResponse("index.html",{"request":request,"name":"title","dictdata":res})

@routes.post("/")
def refresh(request:Request):
    data = news.readSite()
    #df = sentiment.scoredf(data)
    with db.get_session() as session:
        for i in range(len(data)):
            title = data.loc[i,'title']
            time = data.loc[i,'published_date']
            published_date = datetime.strptime(time,'%Y-%m-%dT%H:%M:%S%z')
            try:
                m = models.Headlines(title=title,published_date=published_date)
                session.add(m)
                session.commit()
            
            except Exception as e:
                print(e)

    redirect_url = request.url_for('home')
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER) 
