from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from users.routes import router as user_router
from auth.routes import router as auth_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)


# @app.post('/my-endpoint')
# async def my_endpoint(stats: Stats, request: Request):
#     ip = request.client.host
#     print(ip)
#     return {'status': 1, 'message': 'ok'}

@app.get("/get-ip")
async def get_ip(request: Request):
    client_ip = request.client.host
    print(client_ip)
    return {"client_ip": client_ip}

@app.get('/')
def health_check():
    return JSONResponse(content={"status": "Running!"})