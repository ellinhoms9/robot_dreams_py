import random
import re
from app import app
from flask import abort, request, redirect, session, render_template

users = [
    {'id': 1, 'name': 'user1'}, {'id': 2, 'name': 'user2'}, {'id': 3, 'name': 'user3'}, {'id': 4, 'name': 'user4'},
    {'id': 5, 'name': 'user5'}, {'id': 6, 'name': 'user6'}, {'id': 7, 'name': 'user7'}, {'id': 8, 'name': 'user8'},
    {'id': 9, 'name': 'user9'}, {'id': 10, 'name': 'user10'}, {'id': 11, 'name': 'user11'}, {'id': 12, 'name': 'user12'}
    ]

books = [
    {'id': 1, 'name': 'book1'}, {'id': 2, 'name': 'book2'}, {'id': 3, 'name': 'book3'}, {'id': 4, 'name': 'book4'},
    {'id': 5, 'name': 'book5'}, {'id': 6, 'name': 'book6'}, {'id': 7, 'name': 'book7'}, {'id': 8, 'name': 'book8'},
    {'id': 9, 'name': 'book9'}, {'id': 10, 'name': 'book10'}, {'id': 11, 'name': 'book11'}, {'id': 12, 'name': 'book12'}
    ]

params = [
    {'parameter': 'value', 'name': 'Test', 'age': 1},
    {'parameter': 'value', 'name': 'Ivan', 'age': 25},
    {'parameter': 'value', 'name': 'Stepan', 'age': 30},
    {'parameter': 'value', 'name': 'Maria', 'age': 40},
    {'parameter': 'value', 'name': 'Oleg', 'age': 50}
]





@app.get('/users')
def random_users():
    if 'username' in session:
        username = session['username']
        return render_template('users.html', username=username, users=users)
    else:
        return redirect('/login')

    count = int(request.args.get('count', random.randint(1, len(users))))
    r_list_u = [user['name'] for user in random.choices(users, k=count)]
    return ', '.join(r_list_u)


@app.get('/users/<int:user_id>')
def get_user(user_id):
    if 'username' in session:
        username = session['username']
        if user_id % 2 == 0:
            user = next((user for user in users if user['id'] == user_id), None)
            if user:
                return render_template('user.html', username=username, user=user)
            else:
                abort(404)
        else:
            abort(404)
    else:
        return redirect('/login')


@app.get('/books')
def random_books():
    if 'username' in session:
        username = session['username']
        return render_template('books.html', username=username, books=books)
    else:
        return redirect('/login')

    count = int(request.args.get('count', random.randint(1, len(books))))
    r_list_b = [book['name'] for book in random.choices(books, k=count)]
    book_list = '<ul>'
    for book in r_list_b:
        book_list += f'<li>{book}</li>'
    book_list += '</ul>'
    return book_list, 200


@app.get('/books/<string:title>')
def get_book(title):
    if 'username' in session:
        username = session['username']
        book = next((book for book in books if book['name'] == title), None)
        if book:
            book['name'] = book['name'].capitalize()
            return render_template('book.html', username=username, book=book)
        else:
            abort(404)
    else:
        return redirect('/login')


@app.get('/params')
def get_params():
    if 'username' in session:
        username = session['username']
        query_params = request.args

        table_data = []
        for param in params:
            match = True
            for key, value in query_params.items():
                if key in param and str(param[key]) != value:
                    match = False
                    break
            if match:
                table_data.append({'name': param['name'], 'age': param['age']})

        return render_template('params.html', username=username, table_data=table_data)
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
