from fastapi import FastAPI
from typing import Dict, List

app = FastAPI(
    title="Claude Test API",
    description="Simple FastAPI application for testing",
    version="0.1.0"
)

@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint returning a welcome message."""
    return {"message": "Hello World! FastAPI with uv and Docker"}

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None) -> Dict[str, any]:
    """Get an item by ID with optional query parameter."""
    result = {"item_id": item_id}
    if q:
        result["q"] = q
    return result

@app.get("/users")
async def get_users() -> List[Dict[str, any]]:
    """Get a list of sample users."""
    return [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ]

@app.post("/users")
async def create_user(user: Dict[str, str]) -> Dict[str, any]:
    """Create a new user (sample endpoint)."""
    return {
        "message": "User created successfully",
        "user": user,
        "id": 999  # Mock ID
    }