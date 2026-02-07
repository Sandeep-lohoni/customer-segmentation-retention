def compute_rfm(df, cutoff_date):
    df = df.copy()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["TotalPrice"] = df["Quantity"] * df["Price"]

    rfm = (
        df[df["InvoiceDate"] <= cutoff_date]
        .groupby("Customer ID")
        .agg(
            recency=("InvoiceDate", lambda x: (cutoff_date - x.max()).days),
            frequency=("Invoice", "nunique"),
            monetary=("TotalPrice", "sum")
        )
    )

    return rfm
