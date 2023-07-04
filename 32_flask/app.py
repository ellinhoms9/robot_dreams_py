from flask import Flask
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


@app.get('/hello')
def hello_world():
    app.logger.info('hello world is called')
    return 'Hello World!'


@app.get('/html')
def descryption():
    app.logger.info('descryption is called')
    return (
        '<h1>Hello, users!</h1>'
        '<h2>This is my first site!</h2>'
    )


@app.get('/json')
def todo():
    app.logger.info('json is called')
    return [
        {
            'id': 1,
            'title': 'Search place for rest',
        },
        {
            'details': 'Enter your search criteria!!!',
            'status': 'todo',
         },
    ]


if __name__ == '__main__':
    app.run(debug=True)
