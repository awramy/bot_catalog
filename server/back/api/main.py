from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
from dotenv import load_dotenv

from apps.users.routes import router as users_router
from apps.products.routes import router as products_router
from apps.baskets.routes import router as basket_router


load_dotenv()

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)
app.include_router(basket_router)


@app.get("/")
async def start_page(request: Request):
    return True


if __name__ == "__main__":
    uvicorn.run(app="main:app",
                host="0.0.0.0",
                port=8000,
                reload=True)
