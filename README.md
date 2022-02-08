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
| Enter `python manage.py runserver` | Run this each time to use the web application |

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
|8| Enter `cd foldername`| **MUST CD INTO THE FOLDER** |
|9| Enter `source bin/activate`| **ONLY DO THIS IN THE VIRTUAL ENV FOLDER CREATED** |
|10| Enter `python -m pip install Django`|
|11| Enter `pip install mysqlclient` |
|12| Enter `pip install django-utils-six` |
|13| Enter `pip install djangorestframework`|
|14| Enter `pip install django-rest-auth`|
|15| Enter `pip install djangorestframework-jwt`|
|16| Enter `pip install pdfplumber` |
|17| Download project zip |
|18| Extract downloaded zip to virtual env folder created |
|19| Open the folder containing the manage.py file and right click on the folder name on the folder path and select `open in terminal`; Or just cd into the folder containing the manage.py file in terminal| **Always Do This before running the server or performing step 24** |
|20| Enter `python manage.py makemigrations` |
|21| Enter `python manage.py migrate` |
|22| Enter `python manage.py createsuperuser`|
|23| Enter username and password for superuser account |
|24| Enter `python manage.py runserver` | **Run this each time to use the web application** |

## MUST-DOs
| Step | Description | Screenshot |
|----------|-------------|---------|
|1| Run the server/web app with `python manage.py runserver`|
|2| Open a browser and enter http://127.0.0.1:8000/admin/ |
|3| Login with the superuser login created |
|4| Select |![Guide1](/static/images/guide1.png)|
|4| Add these **groups**|![Guide11](/static/images/guide11.png)|
|6| Add these permissions to the **Admin** group |![Guide2](/static/images/guide2.png)|
|7| Add these permissions to the **Student** group |![Guide3](/static/images/guide3.png)|
|8| Add these permissions to the **Educator** group; **all except** `admin, auth, contenttypes, sessions` **permissions**|![Guide4](/static/images/guide4.png)|






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
