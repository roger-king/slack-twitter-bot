from app.main import app
import uvicorn

if __name__ == "__main__":
    # TODO: make the reload dynamic
    uvicorn.run("app.main:app", host="0.0.0.0", port=9000, reload=True)
