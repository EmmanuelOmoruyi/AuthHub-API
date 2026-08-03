from fastapi import FastAPI

from app.routes import auth, users, products

app = FastAPI(
    title="AuthHub API",
    description="Production-ready Authentication API",
    version="1.0.0"
)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to AuthHub API",
        "status": "running"
    }