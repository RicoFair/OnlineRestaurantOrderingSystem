import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import index as indexRoute
from .models import model_loader
from .dependencies.config import conf

app = FastAPI(title="Online Restaurant Ordering System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables when the app starts
@app.on_event("startup")
def _startup():
    model_loader.create_tables()

# Register routes
indexRoute.load_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)  # add reload=True if you want auto-reload
