from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, order=True)
class Product:
    product_id: int
    product_name: str
    brand_id: int
    category_id: int
    model_year: int
    list_price: float

@dataclass(frozen=True, order=True)
class Store:
    store_id: int
    store_name: str
    phone: str
    email: str
    street: str
    city: str
    state: str
    zip_code: int

    def __repr__(self):
        return f"store {self.store_id} - {self.store_name}"

@dataclass(frozen=True, order=True)
class Order:
    order_id: int
    customer_id: int
    order_status: int
    order_date: datetime
    required_date: datetime
    shipped_date: datetime
    store_id: int
    staff_id: int

    def __repr__(self):
        return f"order.: {self.order_id}"

@dataclass(frozen=True, order=True)
class Staff:
    staff_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    active: str
    store_id: int
    manager_id: int

    def __repr__(self):
        return f"staff: {self.first_name} {self.last_name} {self.staff_id}"

@dataclass(frozen=True, order=True)
class Customer:
    customer_id: int
    first_name: str
    last_name: str
    phone: str
    email: str
    street: str
    city: str
    state: str
    zip_code: int

    def __repr__(self):
        return f"customer.: {self.customer_id} {self.first_name} {self.last_name}"

@dataclass(frozen=True, order=True)
class OrderItem:
    order_id: int
    item_id: int
    product_id: int
    quantity: int
    list_price: float
    discount: float

    def __repr__(self):
        return f"orderItem: oid:{self.order_id} Iid:{self.item_id} qt:{self.quantity}"

@dataclass(frozen=True, order=True)
class Stocks:
    store_id: int
    product_id: int
    quantity: int

    def __repr__(self):
        return f"stock.: {self.store_id}"

@dataclass(frozen=True, order=True)
class Brand:
    brand_id: int
    brand_name: str

    def __repr__(self):
        return f"brand.: {self.brand_name}"

@dataclass(frozen=True, order=True)
class Category:
    category_id: int
    category_name: str

    def __repr__(self):
        return f"category.: {self.category_id}"














