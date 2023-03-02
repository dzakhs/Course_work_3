import pytest

@pytest.fixture
def test_data():
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
 {
    "id": 594226727,
     "state": "CANCELED",
     "date": "2018-09-12T21:27:25.241689",
     "operationAmount": {
        "amount": "67314.70",
         "currency": {
            "name": "руб.",
            "code": "RUB"
                }
            },
     "description": "Перевод организации",
     "from": "Visa Platinum 1246377376343588",
     "to": "Счет 14211924144426031657"
 },
 {
     "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061",
    "operationAmount": {
        "amount": "50870.71",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод с карты на счет",
    "to": "Счет 43597928997568165086"
 },
 {
     "id": 649467725,
     "state": "EXECUTED",
     "date": "2018-04-14T19:35:28.978265",
     "operationAmount": {
         "amount": "96995.73",
         "currency": {
            "name": "руб.",
            "code": "RUB"
                }
            },
     "description": "Перевод организации",
     "from": "Счет 27248529432547658655",
     "to": "Счет 97584898735659638967"
 },
 {
    "id": 542678139,
    "state": "EXECUTED",
    "date": "2018-10-14T22:27:25.205631",
    "operationAmount": {
        "amount": "90582.51",
        "currency": {
            "name": "USD",
            "code": "USD"
                }
            },
    "description": "Перевод организации",
    "from": "Visa Platinum 2256483756542539",
    "to": "Счет 78808375133947439319"
 }
 ]