import time
from fastapi import FastAPI, Request
from api import api_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()


# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     print(f"Request: {request.method} {request.url}, {request.headers}")
#     start_time = time.time()
#     response = await call_next(request)
#     end_time = time.time()
#     print(f"Response: {end_time - start_time} seconds")
#     response.headers["X-Process-Time"] = str(end_time - start_time)
#     return response


# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     print(f"Request: {request.method} {request.url}, {request.headers}")
  
#     response = await call_next(request)
   
#     response.headers["X-App-Version"] = '1.0.0'
#     return response


# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     print(f"Request: {request.headers['user-agent']} ")
#     if "Postman" in request.headers['user-agent']:
#         print('Diqqat: Dasturchi Postman orqali API ga kirdi!')
        
#     start_time = time.time()
#     response = await call_next(request)
#     end_time = time.time()
#     print(f"Response: {end_time - start_time} seconds")
#     response.headers["X-Process-Time"] = str(end_time - start_time)
#     return response
   
@app.middleware('http')
async def log_requests(request: Request, call_next):
    return JSONResponse(
        status_code=503,
        content={
            'message': "Kechirasiz, serverda texnik ishlar olib borilmoqda. 1 soatdan so'ng urinib ko'ring"
        }
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)