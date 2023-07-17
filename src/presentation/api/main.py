from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .controllers.main import setup_controllers
from .di.main import setup_di
from .lifespan import lifespan
from .settings.config import Config


def build_app(config: Config) -> FastAPI:
    app = FastAPI(
        title="Bank", default_response_class=ORJSONResponse, lifespan=lifespan
    )

    # Configuration Block
    setup_controllers(app=app)
    setup_di(app=app, config=config)

    return app
