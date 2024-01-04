from fastapi import FastAPI
import moinify

app = FastAPI()

@app.get("/")
def read_root():
    return {"Moin": "Welt"}

@app.get("/items/{item_id}")
def moinify(item_id: int, text: str = None):
    return {"item_id": item_id, "query_param": query_param}