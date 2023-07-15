from fastapi import FastAPI

from .main import build_app
from .settings.config import load_config


def main() -> FastAPI:
    config = load_config()

    app = build_app(config=config)

    return app