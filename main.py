from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def reed_roots():
    pass


@app.get("/")
async def get_reviews(location_name: str):
    pass