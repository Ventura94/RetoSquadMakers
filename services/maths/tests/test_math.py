import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_get_least_common_multiple_three_numbers(client: AsyncClient):
    response = await client.get("/v1/maths/least_common_multiple", params={"numbers": [2, 4, 6]})
    assert response.json() == {'least common multiple for (2, 4)': 4.0,
                               'least common multiple for (2, 6)': 6.0,
                               'least common multiple for (4, 6)': 12.0}
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_least_common_multiple_two_numbers(client: AsyncClient):
    response = await client.get("/v1/maths/least_common_multiple", params={"numbers": [2, 4]})
    assert response.json() == {'least common multiple for (2, 4)': 4.0}
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_least_common_multiple_one_numbers(client: AsyncClient):
    response = await client.get("/v1/maths/least_common_multiple", params={"numbers": [2]})
    assert response.json() == {'detail': 'You cannot get the least common multiple for a single number.'}
    assert response.status_code == 400


@pytest.mark.anyio
async def test_get_increase_number(client: AsyncClient):
    response = await client.get("/v1/maths/increase", params={"number": 1})
    assert response.json() == {"increase_number": 2}
    assert response.status_code == 200
