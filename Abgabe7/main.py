from fastapi import FastAPI
import moinifier

app = FastAPI()

@app.get("/")
def read_root():
    return {"Moin": "Welt"}

@app.post("/moinify_text")
async def moinify_text(text: str):
    moinified_text = moinifier.moinify(text)
    return {"original_text": text, "moinified_text": moinified_text}