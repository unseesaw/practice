from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Call, Employee
from app.routers import calls, employees

# Создаём таблицы
Call.metadata.create_all(bind=engine)
Employee.metadata.create_all(bind=engine)

app = FastAPI(title="CRM API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calls.router)
app.include_router(employees.router)

@app.get("/")
def root():
    return {"message": "CRM API работает", "docs": "/docs"}