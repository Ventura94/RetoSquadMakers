from fastapi import APIRouter, Query, Depends

from service import MathsService

router = APIRouter(prefix="/maths", tags=["Maths"])


@router.get("/least_common_multiple")
def get_least_common_multiple(service: MathsService = Depends(), numbers: list[int] = Query(...)):
    return service.get_least_common_multiple(numbers)


@router.get("/increase")
def get_increase_number(number: int = Query(...)):
    return {"increase_number": number + 1}
