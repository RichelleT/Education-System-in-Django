## Windows Setup Manual

| Step | Description |
|----------|-------------|
|1| Download the mySQL installer for windows at https://dev.mysql.com/downloads/installer/ |
|2| Select Custom Setup Type |
|3| Select MySQL Server, MySQL Workbench, and Connector/ODBC from available products |
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
|16| Open the folder containing manage.py, enter cmd in the folder path to open a command prompt with the path |
|11| Enter `python manage.py makemigrations` |
|12| Enter `python manage.py migrate` |
|13| Enter `python manage.py createsuperuser`|
|14| Enter username and password for superuser account |
|15| Enter `python manage.py runserver`

## MacOS Setup Manual

| Step | Description |
|----------|-------------|
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
