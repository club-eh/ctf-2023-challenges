from starlette.applications import Starlette
from starlette.config import Config
from starlette.middleware import Middleware
from starlette.datastructures import Secret
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def lorem_ipsum():
	# TODO: add interactive web 2.0 features
	# TODO: add blockchain integration (web 3.0)
	return PlainTextResponse("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")


config = Config(".env")
SECRET_KEY = config.get("SECRET_KEY", cast=Secret)


routes = [
	Route("/", lorem_ipsum),
]

middleware = [
	Middleware(SessionMiddleware, SECRET_KEY),
]

app = Starlette(routes=routes, middleware=middleware)
