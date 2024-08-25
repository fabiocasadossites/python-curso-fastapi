from fastapi import FastAPI

from python_fast_zero.routers import auth, todos, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


# @app.get('/', status_code=HTTPStatus.OK, response_model=Message)
# def read_root():
#    return {'message': 'Olá Mundo!'}
