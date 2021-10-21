# Python Flask Heroku Demo

Demonstration of Python with Flask (REST API) and a deployment to Heroku

## Dependencies

```bash
pip  install flask
pip install python-dotenv

# Save dependencies to requirements.tx
python3 -m pip freeze > requirements.txt
```

## Python Flask project

File: app.py
```python
from flask import Flask
import os

app = Flask(__name__)


@app.route("/greeting")
def greeting():
    return os.environ["MESSAGE"]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

File: .env
```bash
MESSAGE=Hello World from localhost
```

Run the application
```bash
python3 app.py
```

Validate the response
```bash
curl http://127.0.0.1:8080/greeting

# Should print: Message: Hello World from localhost
```

## Git

```bash
git init
```

File .gitignore
```bash
venv
.git
__pycache__
.idea
```

Commit the files to git

```bash
git checkout -b master
```

## Heroku Deployment

1.) Create a Heroku account
2.) Install Heroku CLI

File: Procfile
```bash
web: gunicorn app:app
```

```bash
heroku create
git push heroku master
```

