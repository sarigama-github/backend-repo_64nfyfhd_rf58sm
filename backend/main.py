from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Abdullah Talib Portfolio API", version="1.0.0")

# CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "message": "Portfolio API running"}


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/test")
def test():
    return {"message": "Database configured. Add endpoints as needed."}
