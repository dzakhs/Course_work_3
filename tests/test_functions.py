from utils.functions import load_data, actual_data, sorted_data, print_data
import pytest

def test_load_data():
    url ="https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677833602753&signature=wdPXqZwXgObQzHL6BWlTbyok6sgWwsLYF54a_6xXTLI&downloadName=operations.json"
    assert load_data(url) is not None
def test_actual_data(test_data):
   data = actual_data(test_data)
   assert len(data) == 3

def test_sorted_data(test_data):
    data = sorted_data(test_data)
    assert data[0]['date'] == "2019-08-26T10:50:58.294041"
    assert len(data[:2]) == 2

def test_print_data(test_data):
    data = print_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n']