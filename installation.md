

Install Guide for Linux and Windows

System Requirements

- python
- pip
- virtualenv

Linux Install

- Download the git with git clone https://github.com/WSU-4110/Pet-Finder.git
- Run the command virtualenv -p python3 venv
- Activate the virtual environment with the command source venv/bin/activate
- Run the command pip install -r requirements.txt
- Run the command python manage.py makemigrations
- Run the command python manage.py migrate
- Run the command python manage.py runserver
- Go to 127.0.0.1:8000 to use the website

Windows Install
-i nstall python 3.9
- Run the command py get-pip.py
- Run the command py -m venv venv
- Activate the virtual environment with the command .\venv\Scripts\activate
- Run the command pip install -r requirements.txt
- Run the command python manage.py runserver
- Go to 127.0.0.1:8000 to use the website
- TODO