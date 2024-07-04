from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import userapi, addressapi, skintype_api, product_api, product_image_api, suggestion_api, cart_api, login_history_api, order_api, order_item_api, user_skin_type_api, login_api ,chat_api 
import models.models as models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS settings
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userapi.router, prefix="/users", tags=["users"])
app.include_router(addressapi.router, prefix="/addresses", tags=["addresses"])
app.include_router(skintype_api.router, prefix="/skintypes", tags=["skintypes"])
app.include_router(product_api.router, prefix="/products", tags=["products"])
app.include_router(product_image_api.router, prefix="/product_images", tags=["product_images"])
app.include_router(suggestion_api.router, prefix="/suggestions", tags=["suggestions"])
app.include_router(cart_api.router, prefix="/cart", tags=["cart"])
app.include_router(login_history_api.router, prefix="/login_history", tags=["login_history"])
app.include_router(order_api.router, prefix="/orders", tags=["orders"])
app.include_router(order_item_api.router, prefix="/order_items", tags=["order_items"])
app.include_router(user_skin_type_api.router, prefix="/user_skin_types", tags=["user_skin_types"])
app.include_router(login_api.router, tags=["login"])
app.include_router(chat_api.router, prefix="/api", tags=["chat"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
