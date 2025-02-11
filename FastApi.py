from fastapi import FastAPI

app = FastAPI() #create API instance, app is instance of FastAPI


'''
Operations:

POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data
'''
@app.get("/")
async def root(): #what is an async method?
    return {"message": "Hello World"}

'''
The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to:
the path /
using a get operation'''
