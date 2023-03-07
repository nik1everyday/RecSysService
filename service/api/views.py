from typing import List
from fastapi import APIRouter, Depends, FastAPI, Request

import yaml
from fastapi import APIRouter, FastAPI, Request
from pydantic import BaseModel

from service.api.exceptions import UserNotFoundError, ModelNotFoundError
from service.log import app_logger
from service.auth.authorization import JWTBearer
#from models.load_models import ANN

# y5
with open('config/config_service.yml') as stream:
    config_service = yaml.safe_load(stream)['config']
with open('config/config_models.yml') as stream:
    config_model = yaml.safe_load(stream)


class RecoResponse(BaseModel):
    user_id: int
    items: List[int]


class Message(BaseModel):
    message: str


router = APIRouter()


@router.get(
    path="/health",
    tags=["Health"],
    dependencies=[Depends(JWTBearer())]
)
async def health() -> str:
    return "I am alive - 36.6"


@router.get(
    path="/reco/{model_name}/{user_id}",
    tags=["Recommendations"],
    response_model=RecoResponse,
    dependencies=[Depends(JWTBearer())],
    responses={
        200: {"response": RecoResponse},
        403: {"response": Message},
        404: {"response": Message},
    },
)


async def get_reco(
    request: Request,
    model_name: str,
    user_id: int,
) -> RecoResponse:
    global reco
    app_logger.info(f"Request for model: {model_name}, user_id: {user_id}")

    # Write your code here

    if user_id > 10 ** 9:
        raise UserNotFoundError(error_message=f"User {user_id} not found")

    if model_name not in config_service['models']:
        raise ModelNotFoundError(error_message=f"Model {model_name} not found")

    # if model_name == 'test_model':
    #     k_recs = request.app.state.k_recs
    #     reco = list(range(k_recs))

    #elif model_name == 'ann_model':
    #    model = ANN['model']
    #    if user_id < len(model.label):
    #        reco = list(model.predict(user_id))

    return RecoResponse(user_id=user_id, items=reco)


def add_views(app: FastAPI) -> None:
    app.include_router(router)
