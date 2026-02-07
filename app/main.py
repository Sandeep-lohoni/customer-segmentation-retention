from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Customer Retention Engine")

DATA_PATH = "../data/processed/final_retention_dataset.csv"

@app.get("/")
def home():
    return {"message": "Customer Retention Engine is running"}

@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    df = pd.read_csv(DATA_PATH, index_col="Customer ID")

    if customer_id not in df.index:
        return {"error": "Customer not found"}

    row = df.loc[customer_id]

    return {
        "customer_id": customer_id,
        "segment": row["segment"],
        "churned": int(row["churned"]),
        "clv_6m": round(row["clv_6m"], 2),
        "retention_action": row["retention_action"]
    }
