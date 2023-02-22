---
[FINANCE](https://finance.jackkiwema.com/)
---

### Build from source
> **Step #1** - Clone source (this repo)
```bash
$ git clone https://github.com/jackkiwema.com/finances.git
$ cd finances
```

> **Step #2** - Create virtual environment
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

> **Step #3** - Install dependencies
```bash
$ mv app/deployment/install/env_example .env
```

> **Step #4** - Create Tables
```bash
$ flask db upgrade
```

> **Step #5** - Start the project
```bash
$ flask run --host=0.0.0.0 --port=5000
$ # Access the app in browser: http://127.0.0.1:5000/
```

### Code-Base Structure
```bash
< PROJECT ROOT >
    |
    |--app/
    |   |-- auth/
    |   |     |-- email.py
    |   |     |-- forms.py
    |   |     |-- routes.py
    |   |
    |   |-- main/
    |   |
    |   |-- templates/
    |   |
    |   |-- email.py
    |   |
    |   |-- helpers.py  
    |   | 
    |   |-- models.py
    |
    |
    |-- deployment/
    |
    |-- migrations/
    |
    |-- config.py
    |
    |-- finance.py
    |
    |-- requirements.txt
    |
    |-- **********************************************
