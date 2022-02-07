## Windows Setup Manual

| Step | Description | Note |
|----------|-------------|------------|
|1| Download the mySQL installer for windows at https://dev.mysql.com/downloads/installer/ |
|2| Select Custom Setup Type |
|3| Select `MySQL Server`, `MySQL Workbench`, and `Connector/ODBC` from available products |
|4| Execute and proceed until adding password to root account |
|5| Proceed until install is done |
|6| Open a terminal window/command prompt |
|7| Enter `mysql -u root -p` and enter password |
|8| Enter `SET PASSWORD FOR root@localhost='';` |
|9| Enter `CREATE DATABASE oaies;` |
|10| Download the zip to this project |
|11| Open scripts folder (in the python folder in appdata/program) where pip is located in cmd |
|12| Enter `pip install mysqlclient` |
|13| Enter `pip install django-utils-six` |
|14| Enter `pip install pdfplumber` |
|15| Enter `pip install virtualenv` |
|16| Enter `pip install virtualenvwrapper-win`|
|17|Enter `mkvirtualenv foldername`|
|18| Unzip downloaded project files into the created virtual env folder |
|19| Open the folder containing `manage.py`, enter cmd in the folder path to open a command prompt with the path |
|20| Enter `python manage.py makemigrations` |
|21| Enter `python manage.py migrate` |
|22| Enter `python manage.py createsuperuser`|
|23| Enter username and password for superuser account |
|24| Enter `python manage.py runserver` | Run this each time to use the web application |

## MacOS Setup Manual

| Step | Description | Note |
|----------|-------------|------------|
|1| Open a terminal |
|2-1| Enter `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` | Install homebrew only for users running `macOS High Sierra, Sierra, El Capitan, or earlier` |
|2-2| Enter `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"` | Install homebrew only for users running `macOs Catalina, Mojave, or Big Sur, or later` |
|3| Enter `brew install mysql`| mysql server needed |
|4| Enter `brew install python3`|
|5| Enter `sudo easy_install pip`|
|6| Enter `sudo pip install virtualenv`|
|7| Enter `virtualenv foldername`|
|8| Enter `cd foldername`| MUST CD INTO THE FOLDER |
|9| Enter `source bin/activate`| ONLY DO THIS IN THE VIRTUAL ENV FOLDER CREATED |
|10| Enter `python -m pip install Django`|
|11| Enter `pip install mysqlclient` |
|12| Enter `pip install django-utils-six` |
|13| Enter `pip install pdfplumber` |
|14| Download project zip |
|15| Extract downloaded zip to virtual env folder created |
|16| Open the folder containing the manage.py file and right click on the folder name on the folder path and select `open in terminal`| Or just cd into the folder containing the manage.py file in terminal |
|17| Enter `python manage.py makemigrations` |
|18| Enter `python manage.py migrate` |
|19| Enter `python manage.py createsuperuser`|
|20| Enter username and password for superuser account |
|21| Enter `python manage.py runserver` | Run this each time to use the web application |

## MUST-DOs
| Step | Description |
|----------|-------------|
||![Screenshot](/static/images/formFe.png)|






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
