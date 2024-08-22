from fastapi import FastAPI, Request
import uvicorn
import os
from dotenv import load_dotenv
import multiprocessing
from src.routes.chat import chat
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

api = FastAPI()
api.include_router(chat)

origins = ["*"]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@api.get("/test")
async def root():
    return {'msg": "API is Online'}


if __name__ == "__main__":
    print("begin")
    if os.environ.get('APP_ENV') == "development":
        uvicorn.run("main:api", host="0.0.0.0", port=3500,
                    workers=4, reload=True)
    else:
        pass
