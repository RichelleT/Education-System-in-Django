## Table of Contents

- [Windows Setup Guide](#Windows-Step-by-Step-Setup-Manual)
- [MacOS Setup Guide](#MacOS-Step-by-Step-Setup-Manual)
- [Configuration (Must Do)](#Step-by-Step-Configuration)

## Windows Step-by-Step Setup Manual
### Warning: Please do not skip any steps

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
| Open scripts folder (in the python folder in appdata/program) where pip is located in cmd |
| Enter `pip install mysqlclient` |
| Enter `pip install django-utils-six` |
| Enter `pip install pdfplumber` |
| Enter `pip install virtualenv` |
| Enter `pip install virtualenvwrapper-win`|
| Enter `mkvirtualenv foldername`|
| Download project zip |
| Unzip downloaded project files into the created virtual env folder |
| Open the folder containing `manage.py`, enter cmd in the folder path to open a command prompt with the path | **Always Do This before running the server or performing runserver** |
| Enter `python manage.py makemigrations` |
| Enter `python manage.py migrate` |
| Enter `python manage.py createsuperuser`|
| Enter username and password for superuser account |
| Enter `python manage.py runserver` | **Run this each time to use the web application** |

## MacOS Step-by-Step Setup Manual
### Warning: Please do not skip any steps
### Warning: Please install homebrew for your specific OS

| Description | Note |
|-------------|------------|
| Open a terminal |
| Enter `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` | Note: Install homebrew **only for users running `macOS High Sierra, Sierra, El Capitan, or earlier`** |
| Enter `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"` | Note: Install homebrew **only for users running `macOs Catalina, Mojave, or Big Sur, or later`** |
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
| Open the folder containing the manage.py file and right click on the folder name on the folder path and select `open in terminal`<br/><br/> Or just manually cd into the folder containing the manage.py file in terminal| **Always Do This before running the server or performing runserver** |
| Enter `python manage.py makemigrations` |
| Enter `python manage.py migrate` |
| Enter `python manage.py createsuperuser`|
| Enter username and password for superuser account |
| Enter `python manage.py runserver` | **Run this each time to use the web application** |

## Step-by-Step Configuration
### Warning: This is required, if not you cannot use the system/application
### Warning: Please do not skip any steps, unless it is an optional steps marked with `+`

|Step| Description | Screenshot/Note |
|-----|-------------|---------|
|1| Create a superuser with `python manage.py createsuperuser`| **Note: If this step fails, or is unable to login, Use `step 1.+`** |
|1.+| First, Comment out the `@login_required` and `@group_required` in `register/views.py`.|![Guide5](/static/images/guide5.png)|
|1.+| Then, in `register/forms.py` uncomment highlighted |![Guide6](/static/images/guide6.png)|
|1.+| Then, in `register/forms.py` comment out the highlighted <br/><br/> (**Note: role field is neccessary to assign user to group**) <br/><br/> (**Warning: role field will interfere with creating superuser if present**)|![Guide7](/static/images/guide7.png)|
|2| CD into folder w/ manage.py then enter `python manage.py runserver` to run server|
|3| Go to http://127.0.0.1:8000/registerUser/ and create superuser| Note: Tick **both** `staff` and `superuser` when registering |
|4| Open a browser and enter http://127.0.0.1:8000/admin/ |
|5| Login with the superuser login created |
|+| **If used `step 1.+` to create superuser, and is able to login to admin panel, UNDO all `step 1.+`**| **Note: VERY IMPORTANT STEP** |
|6| To create admin account **comment out `group_required` only** (like in the above step), **create admin account, then uncomment `group_required` again.** <br/><br/> (**Note: Do this while logged into the superuser account**)| **(Note: This is important to add users for the application/system)** <br/><br/>**(Warning1: Must uncomment `group_required` Otherwise, any user can create users)**|
|7| Select |![Guide1](/static/images/guide1.png)|
|8| Add these **groups**|![Guide11](/static/images/guide11.png)|
|9| Add these permissions to the **Admin** group |![Guide2](/static/images/guide2.png)|
|10| Add these permissions to the **Student** group |![Guide3](/static/images/guide3.png)|
|11| Add these permissions to the **Educator** group; **all except** `admin, auth, contenttypes, sessions` **permissions**|![Guide4](/static/images/guide4.png)|
|12| **Log out of superuser** and **login to created admin account**| 
|13|**(While Logged into the Admin Account)** <br/><br/> Create Educator account(s) and Student account(s)| Note: <br/><br/> Educator accounts can create test/quizes/modules and etc. <br/><br/> Student accounts can attempt created tests/quizes |





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
