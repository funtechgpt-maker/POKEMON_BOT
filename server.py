import asyncio
import os
import threading
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "alive"}

def start_bot():
    os.system("python -m bot")

if __name__ == "__main__":
    # run bot in background
    threading.Thread(target=start_bot, daemon=True).start()

    # run web server (Render ku thevai)
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
