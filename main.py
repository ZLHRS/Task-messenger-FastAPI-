from fastapi import FastAPI
from api import user_router, auth_router, system_router, task_router
import uvicorn

app = FastAPI()

app.include_router(system_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run("main:app")
