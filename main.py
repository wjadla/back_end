from fastapi import FastAPI
import router

app = FastAPI()


@app.get("/")
async def home():
    return "hello home"


app.include_router(router.router)