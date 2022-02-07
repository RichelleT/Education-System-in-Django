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
|12| Enter `pip install virtualenv` |
|13| Enter `pip install virtualenvwrapper-win`|
|14|Enter `mkvirtualenv foldername`|
|15| Unzip downloaded project files into the created virtual env folder |
|16| Enter `pip install mysqlclient` |
|17| Enter `pip install django-utils-six` |
|18| Enter `pip install pdfplumber` |
|19| Open the folder containing `manage.py`, enter cmd in the folder path to open a command prompt with the path |
|20| Enter `python manage.py makemigrations` |
|21| Enter `python manage.py migrate` |
|22| Enter `python manage.py createsuperuser`|
|23| Enter username and password for superuser account |
|24| Enter `python manage.py runserver`

## MacOS Setup Manual

| Step | Description | Note |
|----------|-------------|------------|
|1-1|| Enter `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` | Only for users running macOS High Sierra, Sierra, El Capitan, or earlier |
|1-2| Enter `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"` | Only for users running Catalina, Mojave, or Big Sur, or later |
|2| Enter `brew install mysql`|




|NUMBER| (In MacOS) Open the folder and right click on the folder name and select `open in terminal`|


## Dependencies

```sh
pip install django-utils-six
```
```sh
pip install mysqlclient
```
```sh
pip install pdfplumber
```