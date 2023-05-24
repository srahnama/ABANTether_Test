# Django Cryptocurrency Order API ( Abantether.com test )

This Django project implements a RESTful API for managing cryptocurrency orders. It allows users to create orders and retrieve a list of existing orders.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/ABANTether_Test.git
    ```
2. Navigate to the project directory:
    ```
    cd ABANTether_Test
    ```
3. Create a virtual environment (optional but recommended):
    
    ```
    python -m venv env
    source env/bin/activate # Linux/macOS
    env\Scripts\activate # Windows
    ```
4. Install the project dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Apply database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Run the development server:
    ```
    python manage.py runserve
    ```

9. The API will be accessible at `http://localhost:8000/api/`.

## API Endpoints

- `POST /api/orders/create/`: Create a new order.
- `GET /api/orders/list/`: Retrieve a list of existing orders.

## API Usage

- To create a new order, send a POST request to `/api/orders/create/` with the following data:

- `order_id`: Order ID (string)
- `currency`: Currency (string)
- `amount`: Amount (float)
- `price`: Price (float)

Example:
    ```
    POST /api/orders/create/

    {
    "order_id": "12345",
    "currency": "USDT",
    "amount": 10.0,
    "price": 50000.0
    }
    ```

 To retrieve a list of existing orders, send a GET request to `/api/orders/list/`. This will return a JSON array containing the order details.

Example:

    ```
    GET /api/orders/list/
    ```


This will run the test cases defined in the `orders/tests.py` module.



## Customization

- You can customize the integration with the exchange API by modifying the `buy_from_exchange` signal handler in `orders/signals.py`. Update the exchange API URL, headers, and payload to match your specific integration requirements.

- Adjust the model fields in `orders/models.py` as needed to store additional information related to orders.

## Dependencies

The project relies on the following dependencies:

- Django: Web framework for building the API
- djangorestframework: Toolkit for building RESTful APIs
- requests: Library for making HTTP requests

For detailed dependency versions, please refer to the `requirements.txt` file.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).