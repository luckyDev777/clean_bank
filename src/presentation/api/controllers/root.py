from fastapi import APIRouter

router = APIRouter(prefix="/health_check", tags=["root"])


@router.get(
    path="/"
)
async def read_root() -> dict:
    return {"Hello": "World"}
