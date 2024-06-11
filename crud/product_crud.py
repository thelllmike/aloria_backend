# crud/product_crud.py

from sqlalchemy.orm import Session
import models.product_model as models
import schemas.product_schema as schemas

# Get a single product by ID
def get_product(db: Session, product_id: int):
    return db.query(models.ProductModel).filter(models.ProductModel.product_id == product_id).first()



# Get multiple products with pagination
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductModel).offset(skip).limit(limit).all()


def delete_product(db: Session, product_id: int):
    product = db.query(models.ProductModel).filter(models.ProductModel.product_id == product_id).first()
    if product:
        db.delete(product)
        db.commit()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Update an existing product
def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

# Delete a product
def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
