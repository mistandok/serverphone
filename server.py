from fastapi import FastAPI, Form, Cookie, Body
from fastapi.param_functions import Query
from starlette.responses import Response
import phoneformatting
from pydantic import BaseModel
import json


app = FastAPI()


class Data(BaseModel):
    phone: str


@app.post("/unify_phone_from_json")
def formatting_phone_json(data: Data):
    phone = data.phone  

    if not phone:
        formatted_phone = ""
    else:
        formatted_phone = phoneformatting.format_phone_num(phone)

    return Response(
        f"{formatted_phone}",
        media_type="text/html"
        )


@app.post("/unify_phone_from_form")
def formatting_phone_form(phone: str = Form(...)):
    if not phone:
        formatted_phone = ""
    else:
        formatted_phone = phoneformatting.format_phone_num(phone)

    return Response(
        f"{formatted_phone}",
        media_type="text/html"
        )


@app.get("/unify_phone_from_query")
def formatting_phone_query(phone: str = Query(...)):
    if not phone:
        formatted_phone = ""
    else:
        formatted_phone = phoneformatting.format_phone_num(phone)

    return Response(
        f"{formatted_phone}",
        media_type="text/html"
        )


@app.get("/unify_phone_from_cookie")
def formatting_phone_cookie(phone: str = Cookie(default=None)):
    if not phone:
        formatted_phone = ""
    else:
        formatted_phone = phoneformatting.format_phone_num(phone)

    return Response(
        f"{formatted_phone}",
        media_type="text/html"
        )