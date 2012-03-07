# sc2tourney Django Project #
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python enviroment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```mkvirtualenv --no-site-packages sc2tourney-env```

#### For virtualenv ####
```virtualenv --no-site-packages sc2tourney-env```

```cd sc2tourney-env```

```source bin/activate```

### Clone the code ###
Obtain the url to your git repository.
```git clone <URL_TO_GIT_RESPOSITORY> sc2tourney```

### Install requirements ###
```cd sc2tourney```

```pip install -r requirements.txt```

### Configure project ###
```cp sc2tourney/__local_settings.py sc2tourney/local_settings.py```

```vi sc2tourney/local_settings.py```

### Sync database ###
```python manage.py syncdb```

## Running ##
```python manage.py runserver```

Open browser to 127.0.0.1:8000
