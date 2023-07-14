import re
from app import app, db
from flask import abort, request, redirect, session, render_template, jsonify
from models import User, Book, Purchase, PublishingHouse



@app.route('/users', methods=['GET'])
def get_users():
    if 'username' in session:
        size = int(request.args.get('size', -1))
        if size > 0:
            users = User.query.limit(size).all()
        else:
            users = User.query.all()
        return render_template('users.html', users=users)
    else:
        return redirect('/login')


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if 'username' in session:
        user = User.query.get(user_id)
        if user:
            return render_template('user.html', user=user)
        else:
            abort(404)
    else:
        return redirect('/login')


@app.route('/books', methods=['GET'])
def get_books():
    if 'username' in session:
        size = int(request.args.get('size', -1))
        if size > 0:
            books = Book.query.limit(size).all()
        else:
            books = Book.query.all()
        return render_template('books.html', books=books)
    else:
        return redirect('/login')


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    if 'username' in session:
        book = Book.query.get(book_id)
        if book:
            return render_template('book.html', book=book)
        else:
            abort(404)
    else:
        return redirect('/login')


@app.route('/purchases', methods=['GET'])
def get_purchases():
    if 'username' in session:
        size = int(request.args.get('size', -1))
        if size > 0:
            purchases = Purchase.query.limit(size).all()
        else:
            purchases = Purchase.query.all()
        return render_template('purchases.html', purchases=purchases)
    else:
        return redirect('/login')


@app.route('/purchases/<int:purchase_id>', methods=['GET'])
def get_purchase(purchase_id):
    if 'username' in session:
        purchase = Purchase.query.get(purchase_id)
        if purchase:
            return render_template('purchase.html', purchase=purchase)
        else:
            abort(404)
    else:
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/users')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username is None or password is None:
            abort(400)

        # username validation
        if len(username) < 5:
            return "Username should be at least 5 characters long."

        # validation password
        if len(password) < 8 or not re.search(r'\d', password) or not re.search(r'[A-Z]', password):
            return "Password should be at least 8 characters long and contain at least one digit and one uppercase letter."
        session['username'] = username
        return redirect('/users')

    else:

        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.route('/')
def home():
    return '''
        <h1>Welcome to the Home Page!</h1>
        <ul>
            <li><a href="/login">Login</a></li>
            <li><a href="/users">Users</a></li>
            <li><a href="/books">Books</a></li>
            <li><a href="/params">Params</a></li>
        </ul>
    '''


#### TASK8 CREATE NEW OBJECTS IN DATABASE

@app.route('/users', methods=['POST'])
def create_user():
    if 'username' in session:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        age = request.form.get('age')

        if not first_name or not last_name or not age:
            return jsonify({'error': 'Missing required fields'}), 400

        user = User(first_name=first_name, last_name=last_name, age=age)
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User created successfully', 'user_id': user.id}), 201
    else:
        return redirect('/login')


@app.route('/books', methods=['POST'])
def create_book():
    if 'username' in session:
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')
        price = request.form.get('price')
        publishing_house_id = request.form.get('publishing_house_id')

        if not title or not author or not year or not price or not publishing_house_id:
            return jsonify({'error': 'Missing required fields'}), 400

        book = Book(title=title, author=author, year=year, price=price, publishing_house_id=publishing_house_id)
        db.session.add(book)
        db.session.commit()

        return jsonify({'message': 'Book created successfully', 'book_id': book.id}), 201
    else:
        return redirect('/login')


@app.route('/purchases', methods=['POST'])
def create_purchase():
    if 'username' in session:
        user_id = request.form.get('user_id')
        book_id = request.form.get('book_id')

        if not user_id or not book_id:
            return jsonify({'error': 'Missing required fields'}), 400

        user = User.query.get(user_id)
        book = Book.query.get(book_id)
        if not user or not book:
            return jsonify({'error': 'User or book not found'}), 404

        purchase = Purchase(user_id=user_id, book_id=book_id)
        db.session.add(purchase)
        db.session.commit()

        return jsonify({'message': 'Purchase created successfully', 'purchase_id': purchase.id}), 201
    else:
        return redirect('/login')
