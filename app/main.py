from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Multi-Agent Research AI Running"
    }