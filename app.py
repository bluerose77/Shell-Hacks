from os import name
from website import create_app

app = create_app()

if name == '__main__':
    app.run(debug=True)