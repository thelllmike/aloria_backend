# main.py

from fastapi import FastAPI
from api import userapi, addressapi, skintype_api, product_api, product_image_api, suggestion_api, cart_api, login_history_api, order_api, order_item_api, user_skin_type_api

app = FastAPI()

# Include the user API router
app.include_router(userapi.router)
# Include the address API router
app.include_router(addressapi.router)
# Include the skin type API router
app.include_router(skintype_api.router)
# Include the product API router
app.include_router(product_api.router)
# Include the product image API router
app.include_router(product_image_api.router)
# Include the suggestion API router
app.include_router(suggestion_api.router)
# Include the cart API router
app.include_router(cart_api.router)
# Include the login history API router
app.include_router(login_history_api.router)
# Include the order API router
app.include_router(order_api.router)
# Include the order item API router
app.include_router(order_item_api.router)
# Include the user skin type API router
app.include_router(user_skin_type_api.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
