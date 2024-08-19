import datetime
from unittest.mock import patch
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "mocked_today, expected",
    [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
    ]
)
def test_outdated_products(
        mocked_today: datetime.date,
        expected: list) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = mocked_today
        assert outdated_products(products) == expected
