# crud/order_crud.py

from ntpath import join
import select
from sqlalchemy import func, text
from sqlalchemy.orm import Session
import models.order_model as models
import schemas.order_schema as schemas
import models.order_item_model as order_item_models
import models.product_model as product_models
import models.models as user_models
import models.models as address_models


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.OrderModel(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.OrderModel).filter(models.OrderModel.user_id == user_id).offset(skip).limit(limit).all()

def get_order(db: Session, order_id: int):
    return db.query(models.OrderModel).filter(models.OrderModel.order_id == order_id).first()

def update_order(db: Session, order_id: int, order: schemas.OrderCreate):
    db_order = db.query(models.OrderModel).filter(models.OrderModel.order_id == order_id).first()
    if db_order:
        for key, value in order.dict().items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = db.query(models.OrderModel).filter(models.OrderModel.order_id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order

def get_order_details(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(
        product_models.ProductModel.product_name.label('product_name'),
        user_models.UserModel.username.label('customer'),
        product_models.ProductModel.category.label('category'),
        address_models.Address.address_line1.label('address_line1'),
        address_models.Address.address_line2.label('address_line2'),
        address_models.Address.city.label('city'),
        address_models.Address.state.label('state'),
        address_models.Address.postal_code.label('postal_code'),
        address_models.Address.country.label('country'),
        order_item_models.OrderItemModel.quantity.label('quantity'),
        models.OrderModel.order_date.label('order_date'),
        order_item_models.OrderItemModel.price.label('price'),
        order_item_models.OrderItemModel.order_item_id.label('order_item_id'),
        order_item_models.OrderItemModel.status.label('status')
    ).join(
        order_item_models.OrderItemModel, order_item_models.OrderItemModel.order_id == models.OrderModel.order_id
    ).join(
        product_models.ProductModel, product_models.ProductModel.product_id == order_item_models.OrderItemModel.product_id
    ).join(
        user_models.UserModel, user_models.UserModel.user_id == models.OrderModel.user_id
    ).join(
        address_models.Address, address_models.Address.address_id == models.OrderModel.address_id
    ).offset(skip).limit(limit).all()

    result = []
    for row in query:
        result.append({
            "order_item_id": row.order_item_id,
            "product_name": row.product_name,
            "customer": row.customer,
            "category": row.category,
            "address": f"{row.address_line1}, {row.address_line2}, {row.city}, {row.state}, {row.postal_code}, {row.country}",
            "quantity": row.quantity,
            "order_date": row.order_date,
            "price": row.price,
            "status": row.status.value  # assuming status is an enum, use .value to get the string representation
        })

    return result

