## Windows Step-by-Step Setup Manual

|Description | Note |
|-------------|------------|
| Download the mySQL installer for windows at https://dev.mysql.com/downloads/installer/ |
| Select Custom Setup Type |
| Select `MySQL Server`, `MySQL Workbench`, and `Connector/ODBC` from available products |
| Execute and proceed until adding password to root account |
| Proceed until install is done |
| Open a terminal window/command prompt |
| Enter `mysql -u root -p` and enter password |
| Enter `SET PASSWORD FOR root@localhost='';` |
| Enter `CREATE DATABASE oaies;` |
| Download the zip to this project |
| Open scripts folder (in the python folder in appdata/program) where pip is located in cmd |
| Enter `pip install mysqlclient` |
| Enter `pip install django-utils-six` |
| Enter `pip install pdfplumber` |
| Enter `pip install virtualenv` |
| Enter `pip install virtualenvwrapper-win`|
|Enter `mkvirtualenv foldername`|
| Unzip downloaded project files into the created virtual env folder |
| Open the folder containing `manage.py`, enter cmd in the folder path to open a command prompt with the path | **Always Do This before running the server or performing runserver** |
| Enter `python manage.py makemigrations` |
| Enter `python manage.py migrate` |
| Enter `python manage.py createsuperuser`|
| Enter username and password for superuser account |
| Enter `python manage.py runserver` | **Run this each time to use the web application** |

## MacOS Step-by-Step Setup Manual

| Description | Note |
|-------------|------------|
| Open a terminal |
| Enter `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` | Install homebrew only for users running `macOS High Sierra, Sierra, El Capitan, or earlier` |
| Enter `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"` | Install homebrew only for users running `macOs Catalina, Mojave, or Big Sur, or later` |
| Enter `brew install mysql`| mysql server needed |
| Enter `brew install python3`|
| Enter `sudo easy_install pip`|
| Enter `sudo pip install virtualenv`|
| Enter `virtualenv foldername`|
| Enter `cd foldername`| **MUST CD INTO THE FOLDER** |
| Enter `source bin/activate`| **ONLY DO THIS IN THE VIRTUAL ENV FOLDER CREATED** |
| Enter `python -m pip install Django`|
| Enter `pip install mysqlclient` |
| Enter `pip install django-utils-six` |
| Enter `pip install pdfplumber` |
| Download project zip |
| Extract downloaded zip to virtual env folder created |
| Open the folder containing the manage.py file and right click on the folder name on the folder path and select `open in terminal`; Or just cd into the folder containing the manage.py file in terminal| **Always Do This before running the server or performing runserver** |
| Enter `python manage.py makemigrations` |
| Enter `python manage.py migrate` |
| Enter `python manage.py createsuperuser`|
| Enter username and password for superuser account |
| Enter `python manage.py runserver` | **Run this each time to use the web application** |

## Step-by-Step MUST-DOs
| Description | Screenshot |
|-------------|---------|
| Run the server/web app with `python manage.py runserver`|
|If ^ step does not work, then comment out the `@login_required` and `@group_required` in `register/views.py`.|![Guide5](/static/images/guide5.png)|
| Then, in `register/forms.py` uncomment highlighted |![Guide6](/static/images/guide6.png)|
| Go to http://127.0.0.1:8000/registerUser/|
| Open a browser and enter http://127.0.0.1:8000/admin/ |
| Login with the superuser login created |
| Select |![Guide1](/static/images/guide1.png)|
| Add these **groups**|![Guide11](/static/images/guide11.png)|
| Add these permissions to the **Admin** group |![Guide2](/static/images/guide2.png)|
| Add these permissions to the **Student** group |![Guide3](/static/images/guide3.png)|
| Add these permissions to the **Educator** group; **all except** `admin, auth, contenttypes, sessions` **permissions**|![Guide4](/static/images/guide4.png)|






<!-- ## Dependencies

```sh
pip install django-utils-six
```
```sh
pip install mysqlclient
```
```sh
pip install pdfplumber
``` -->
