from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import gemini

app = FastAPI()

app.include_router(gemini.router, prefix="/gemini")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)