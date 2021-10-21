# Python Flask Heroku Demo

Demonstration of Python with Flask (REST API) and a deployment to Heroku

Goals:
- Create a simple REST application
- On the local machine we want that the API `/greeting` returns "Hello World from localhost"
- Deployment to Heroku
- On the Heroku deployment we want that the API `/greeting` returns "Hello World from Heroku"

## Dependencies

```bash
pip  install flask
pip install python-dotenv

# For Heroku
pip install gunicorn

# Save dependencies to requirements.txt
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

Commit the files to git. And after checkout to the master branch.

```bash
git checkout -b master
```

## Heroku Deployment

- Create a Heroku account
- Install Heroku CLI

File: Procfile
```bash
web: gunicorn app:app
```

Create the Heroku application
```bash
heroku create

# Returns
# > Creating app... done, ⬢ murmuring-plains-11587
# > https://murmuring-plains-11587.herokuapp.com/ | https://git.heroku.com/murmuring-plains-11587.git

git push heroku master
```

### Set the environment variable

```bash
heroku config:set MESSAGE="Hello World from Heroku" -a murmuring-plains-11587
```

### Validate the deployment

Validate the response
```bash
curl https://murmuring-plains-11587.herokuapp.com/greeting

# Should print: Message: Hello World from Heroku
```