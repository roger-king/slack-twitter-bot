import os
import uvicorn

if __name__ == "__main__":
    # TODO: make the reload dynamic
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(
        os.getenv("PORT", 9000)), reload=True if os.getenv("SERVER_ENV", "local") != 'local' else False)
