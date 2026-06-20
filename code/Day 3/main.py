from fastapi import FastAPI
khushi = FastAPI()

@khushi.get("/user/{user_name}")
def read_user(user_name: str):
    return {"user_name": user_name}

@khushi.get("/items/{item_id}/product/{product_id}")
def read_item(item_id: int, product_id: str):
    return {"item_id": item_id,
            "product_id": product_id}

@khushi.get("/price/{price}")
def read_price(price: float):
    return {"price": price}

@khushi.get("/product")
def read_product(page: str):
    return {"page": page}

@khushi.get("/Details")
def read_details(name:str, dob:float):
    return {"name": name,
            "dob": dob}

@khushi.get("/details")
def read_details():
    return {"Saurav": 23.07}