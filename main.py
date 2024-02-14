from fastapi import FastAPI

app = FastAPI()

# Step 1 - Root Route Make a root route, have it return `Hello World'
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Step 2 - New endpoint Make a get endpoint and call it items
@app.get("/items/")
async def display_items(skip: int = 0, limit: int = 10): 
    display_items = [
        {"id": 1, "name": "Jonathan "},
        {"id": 2, "name": "Grant"}
    ]
    return {"skip": skip, "limit": limit, "items": display_items}


# Step 3- Have the new endpoint accept a path parameter called `item_id
# Have it return the item ID value
@app.get("/items/{item_id}") 
async def display_items(item_id: int):
    return{"item_id": item_id}
   
   