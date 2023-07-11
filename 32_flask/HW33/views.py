import random

from app import app
from flask import abort, request, redirect, render_template

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
    count = int(request.args.get('count', random.randint(1, len(users))))
    r_list_u = [user['name'] for user in random.choices(users, k=count)]
    return ', '.join(r_list_u)


@app.get('/users/<int:user_id>')
def get_user(user_id):
    if user_id % 2 == 0:
        return str(user_id)
    else:
        abort(404)


@app.get('/books')
def random_books():
    count = int(request.args.get('count', random.randint(1, len(books))))
    r_list_b = [book['name'] for book in random.choices(books, k=count)]
    book_list = '<ul>'
    for book in r_list_b:
        book_list += f'<li>{book}</li>'
    book_list += '</ul>'
    return book_list, 200


@app.get('/books/<string:title>')
def get_book(title):
    transformed_title = title.capitalize()
    return transformed_title


@app.route('/params')
def get_params():
    query_params = request.args
    # html table
    table_html = '<table>\n<tr><th>parameter</th><th>value</th></tr>\n'
    for param in params:
        match = True
        for key, value in query_params.items():
            if key in param and str(param[key]) != value:
                match = False
                break
        if match:
            for key, value in param.items():
                if key != 'parameter':
                    table_html += f"<tr><td>{key}</td><td>{value}</td></tr>\n"
    table_html += '</table>'
    return f'<html>\n<body>\n{table_html}\n</body>\n</html>'


@app.route('/login', methods=['GET', 'POST'])
def login():
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
        return redirect('/users')

    else:
        return f'''
        <form method="POST" action="/login">
            <label for="email">Email:</label>
            <input type="email" name="email" id="email"><br><br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password"><br><br>
            <input type="submit" value="Submit">
        </form>
        '''


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
