from fastapi import FastAPI
import moinifier

app = FastAPI()

@app.get("/")
def read_root():
    return {"Moin": "Welt"}

@app.post("/modify-text")
async def moinify_text(text: str):
    moinified_text = moinify(text)
    return {"original_text": text, "moinified_text": moinified_text}