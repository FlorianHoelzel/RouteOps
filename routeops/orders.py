def format_order(orders: dict[str, str | int]) -> str:
    return (
        f"Auftragsnummer: {orders['order_id']}\n"
        f"Kunde: {orders['customer']}\n"
        f"Adresse: {orders['pickup_address']}\n"
        f"Containergröße: {orders['container_size_m3']} m³\n"
        f"Status: {orders['status']}"
    )