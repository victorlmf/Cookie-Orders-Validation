from crypt import methods
from flask_app import app
from flask import request, render_template, redirect
from flask_app.models.models_order import Cookie

# Show all orders
@app.route('/cookies')
def show_orders():
    orders = Cookie.show_orders()
    return render_template('/cookies.html', orders=orders)

# Add new order
@app.route('/cookies/new')
def new_order_form():
    return render_template('new_order.html')

@app.route('/new_order', methods=['POST'])
def new_order():
    if Cookie.validate_cookie(request.form):
        Cookie.add_order(request.form)
        return redirect('/cookies')
    return redirect('/cookies/new')

# Edit order
@app.route('/cookies/edit/<int:order_id>')
def show_order(order_id):
    data = {
        "id" : order_id
    }
    order = Cookie.show_one_order(data)
    return render_template('/edit_order.html', order_id=order[0]['id'], order=order[0])

@app.route('/edit', methods=['POST'])
def edit():
    if Cookie.validate_cookie(request.form):
        Cookie.edit_order(request.form)
        return redirect('cookies')
    order_id = request.form['id']
    return redirect(f'/cookies/edit/{order_id}')