from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes import auth, users, products
from app.db.database import engine, Base

# Import ALL models so SQLAlchemy knows about them
from app.models.user import User
from app.models.product import Product


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="AuthHub API",
    description="Production-ready Authentication API",
    version="1.0.0",
    debug=True,
    lifespan=lifespan,
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
