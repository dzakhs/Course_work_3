from utils.functions import load_data, actual_data, print_data, sorted_data

def main():
    BANK_TRANSACTIONS = load_data("https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677789062064&signature=Yp72KXmrKPssmIX7wHUcJYovkUCQwoKVTZOtgFS86KQ&downloadName=operations.json")
    data = actual_data(BANK_TRANSACTIONS)
    data = sorted_data(data)
    data = print_data(data)
    for transaction in data:
        print(transaction)






if __name__ == "__main__":
    main()
