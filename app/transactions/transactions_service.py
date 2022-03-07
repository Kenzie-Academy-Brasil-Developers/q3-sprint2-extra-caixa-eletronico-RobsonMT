from datetime import datetime as dt
from csv import DictReader
import csv
import os

FILEPATH = os.getenv("FILEPATH")
FIELDNAMES = ['title', 'transaction_type', 'value', 'date']

def read_transactions_in_csv():
    with open(FILEPATH, "r") as csvfile:
        reader = DictReader(csvfile)
        tarnsactions = list(reader)

    return tarnsactions


def write_transaction_in_csv(payload: dict):
    new_date = dt.now().strftime("%d/%m/%Y")
    payload.update({"date": new_date})

    with open(FILEPATH, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerow(payload)

    return payload


def calc_transactions_balance():
    transactions = read_transactions_in_csv()

    income = 0
    outcome = 0

    for t in transactions:
        if t["transaction_type"] == "income":
            income += float(t["value"])
        if t["transaction_type"] == "outcome":
            outcome += float(t["value"])

    return income - outcome

    

