from fastapi import FastAPI
from routers.articles import router as articles_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Tweak CORS later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(articles_router)