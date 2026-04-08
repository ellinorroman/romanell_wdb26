from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def read_root():
    return { "msg": "Hej Ellinor!"}

@app.get("/api/ip")
def ip(request: Request):
    return { "ip": request.client.host}


@app.get("/ip", response_class=HTMLResponse)
def ip(request: Request):
    return f"<h1>Din ip är {request.client.host}</h1>"

@app.get("/rooms")
def get_rooms():
    rooms = [
        {"number":101, "persons":2, "price":60},
        {"number":102, "persons":1, "price":50},
        {"number":103, "persons":4, "price":80}
    ]
    return rooms