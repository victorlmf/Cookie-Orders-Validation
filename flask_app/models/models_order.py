from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
db = 'cookie_orders'

class Cookie:
    def __init__(self,data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_box = data['number_of_box']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Setup static method for input validation
    @staticmethod
    def validate_cookie(cookie):
        is_valid = True
        if len(cookie['customer_name']) <= 0 or len(cookie['cookie_type']) <= 0 or len(cookie['number_of_box']) <= 0:
            flash('All fields are required!')
            is_valid = False
        if len(cookie['customer_name']) < 2 and len(cookie['customer_name']) != 0:
            flash('Name must be at least 3 characters!')
            is_valid = False
        if len(cookie['cookie_type']) < 2 and len(cookie['cookie_type']) != 0:
            flash('Cookie Tpye must be at least 3 characters!')
            is_valid = False
        if len(cookie['number_of_box']) > 0:
            if int(cookie['number_of_box']) <= 0:
                flash('Please enter a valid box number!')
                is_valid = False
        return is_valid

    # Setup query to add new order
    @classmethod
    def add_order(cls,data):
        query = """
                INSERT INTO cookie_orders (customer_name, cookie_type,number_of_box, created_at, updated_at)
                VALUES (%(customer_name)s, %(cookie_type)s, %(number_of_box)s, NOW(), NOW());
                """
        return connectToMySQL(db).query_db(query,data)

    # Setup query to show all orders
    @classmethod
    def show_orders(cls):
        query = "SELECT * FROM cookie_orders;"
        results = connectToMySQL(db).query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders
    
    # Setup query to show one order
    @classmethod
    def show_one_order(cls,data):
        query = """
                SELECT * FROM cookie_orders
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)

    # Setup query to edit order
    @classmethod
    def edit_order(cls,data):
        query = """
                UPDATE cookie_orders
                SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, number_of_box = %(number_of_box)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)