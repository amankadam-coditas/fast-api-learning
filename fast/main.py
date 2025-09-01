from fastapi import FastAPI
from fast.users.routers import router as userRoutes
app = FastAPI()

@app.get("/")
async def greet():
    return {"msg" : "Welcome Code_RED" }

app.include_router(userRoutes)