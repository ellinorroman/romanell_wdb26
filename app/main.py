from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hej Ellinor!"}

@app.get("/api/ip")
def ip(request: Request):
    return { "ip": request.client.host}


@app.get("/ip", response_class=HTMLResponse)
def ip(request: Request):
    return f"<h1>Din ip är {request.client.host}</h1>"