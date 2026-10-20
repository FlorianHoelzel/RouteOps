from routeops.orders import format_order

orders = {
    "order_id": 'RO-1001',
    'customer': 'Max Mustermann',
    'pickup_address': 'Musterstraße 1',
    'container_size_m3': 1,
    'status': 'new'
}

if __name__ == "__main__":
    print(format_order(orders))