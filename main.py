from fastapi import FastAPI

app = FastAPI()

# Step 1 - Root Route Make a root route, have it return `Hello World'
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Step 2 - New endpoint Make a get endpoint and call it items
@app.get("/items/")
async def display_items(skip: int = 0, limit: int = 10, q: str = None): 
    if q:
        response_data = {"q": q, "skip": skip, "limit": limit}
    else:
        response_data = {"skip": skip, "limit": limit}
        
    items = [
        {"id": 1, "name": "Jonathan"},
        {"id": 2, "name": "Grant"}
    ]
    
    if q:
        items = [item for item in items if q.lower() in item["name"].lower()]
        response_data["items"] = items
        
    return response_data
    


# Step 3- Have the new endpoint accept a path parameter called `item_id
# Have it return the item ID value
@app.get("/items/{item_id}") 
async def display_items(item_id: int):
    return{"item_id": item_id}

# Step 4
@app.get("/users/{user_id}")
async def display_user(user_id: int):
    return {"user_id": user_id}

# step 5
@app.get("/users/{user_id}/items/")
async def display_user_items(user_id: int, skip: int = 0, limit: int = 10):
    return {"user_id": user_id, "skip": skip, "limit": limit}