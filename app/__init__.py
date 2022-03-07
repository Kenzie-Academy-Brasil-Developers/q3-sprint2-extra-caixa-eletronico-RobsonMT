
from app.transactions.transactions_service import (
    calc_transactions_balance, read_transactions_in_csv,
    write_transaction_in_csv
)
from app.csv_package.csv_module import create_csv_file
from app.decorators.verify_keys import verify_keys
from flask import Flask, jsonify, request
from http import HTTPStatus
import os

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
FILEPATH = os.getenv("FILEPATH")
KEYS = ["title", "transaction_type", "value"]

create_csv_file()
@app.get("/transactions")
def list_transactions():
    transactions = read_transactions_in_csv()
    return jsonify(transactions), HTTPStatus.OK


@app.post("/transactions")
@verify_keys(KEYS)
def register_transaction():
    body_req = request.get_json()
    return write_transaction_in_csv(
        payload=body_req
    ), HTTPStatus.CREATED


@app.get("/balance")
def transactions_balance():
    balance = calc_transactions_balance()
    return {
        "message": f"Seu saldo é de R$ {balance:.2f}"
    }, HTTPStatus.OK