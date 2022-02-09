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
| Open a command prompt |
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
| Enter `python manage.py runserver` | This step is only to confirm it works. <br/><br/> Run this command every time to run server |
| Close cmd to stop server from running |
| Perform these steps next - [Configuration](#Step-by-Step-Configuration) | **Must be done before using system/application** |

## MacOS Step-by-Step Setup Manual
### Warning: Please do not skip any steps
### Warning: Please install homebrew for your specific OS

| Description | Note |
|-------------|------------|
| Open a terminal |
| Enter `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` | Install homebrew **only for users running `macOS High Sierra, Sierra, El Capitan, or earlier`** |
| Enter `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"` | Install homebrew **only for users running `macOs Catalina, Mojave, or Big Sur, or later`** |
| Enter `brew install mysql`|
| Open a terminal window |
| Enter `mysql -u root -p` and enter password | Note: try `mysql.server start` if unable to start sql
| Enter `SET PASSWORD FOR root@localhost='';` |
| Enter `CREATE DATABASE oaies;` |
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
| Open the folder containing the manage.py file, <br/>then, right click on the folder name on the folder path, <br/>then select `open in terminal`<br/><br/> Or just manually cd into the folder containing the manage.py file in terminal| **Always Do This before running the server or performing runserver** |
| Enter `python manage.py makemigrations` |
| Enter `python manage.py migrate` |
| Enter `python manage.py runserver` | This step is only to confirm it works. <br/><br/> **Run this command every time to run server** |
| Press ctrl+C to stop server from running |
| Perform these steps next - [Configuration](#Step-by-Step-Configuration) |

## Step-by-Step Configuration
### Warning: This is required, if not you cannot use the system/application
### Warning: Please do not skip any steps, unless it is an optional steps marked with `+`

|Step| Description | Screenshot/Note |
|-----|-------------|---------|
|1| Create a superuser with `python manage.py createsuperuser`| **Note: If this step fails, or is unable to login, Use `step 1.+`** |
|1.+| First, Comment out the following in `register/views.py`. <br/><br/> **Note:** In the original **untouched `views.py`**,<br/>all the commented out lines in the screenshot is **not commented out** by default |![Guide5](/static/images/guide5.png)<br/>Note: This is what it should look like after performing this step|
|1.+| Then, in `register/forms.py` uncomment highlighted |![Guide6](/static/images/guide6.png)|
|1.+| Then, in `register/forms.py` comment out the highlighted <br/><br/> (**Note: role field is neccessary to assign user to group**) <br/><br/> (**Warning: role field will interfere with creating superuser if present**)|![Guide7](/static/images/guide7.png)|
|1.+|Then, in `templates/registerUser.html` comment out `line3`, `line4` and `line 17` to `line 72`| ![Guide9](/static/images/guide9.png)<br/>Note: This is what it should look like after performing this step|
|1.+|Then, in `templates/registerUser.html` uncomment `line73` and `line74` <br/><br/>Note: To uncomment, <br/>just remove `{% comment %}` <br/> and remove `{% endcomment %}` <br/>from `line73` and `line74` | ![Guide10](/static/images/guide10.png)<br/>Note: This is what it should look like after performing this step|
|2| CD into folder w/ manage.py then enter `python manage.py runserver` to run server|
|3| Go to http://127.0.0.1:8000/registerUser/ and create superuser| Note: Tick **both** `staff` and `superuser` when registering |
|+| This error will appear, **ignore it**|![Guide8](/static/images/guide8.png)|
|4| Open a browser and enter http://127.0.0.1:8000/admin/ |
|5| Login with the superuser login created |
|+| **If used `step 1.+` to create superuser, and is able to login to admin panel, UNDO all `step 1.+`**| **Note: VERY IMPORTANT STEP** |
|6| Go to http://127.0.0.1:8000/admin/, and select `add` to add groups <br/><br/> (Note: Please follow order of adding groups) |![Guide1](/static/images/guide1.png)|
|7| Add the following permissions to the **`Admin`** group, then save |![Guide2](/static/images/guide2.png)|
|8| Add the following permissions to the **`Educator`** group, then save <br/><br/> **Filter: build, then choose all** <br/>**Filter: addusermodule, then choose all**<br/><br/>**Note: all except** `admin, auth, contenttypes, sessions` **permissions**|![Guide4](/static/images/guide4.png)|
|9| Add the following permissions to the **`Student`** group, then save |![Guide3](/static/images/guide3.png)|
|10| To create admin account, <br/><br/>  **Comment out `group_required` only** (like in the above step), <br/><br/> **Go to** http://127.0.0.1:8000/registerUser/ and **create admin account, <br/><br/> then uncomment `group_required` again.** <br/><br/> | (**Note: Do this while logged into the superuser account**) <br/><br/> **(Note: This is important to add users for the application/system)** <br/><br/>**(Warning: Must uncomment `group_required` Otherwise, any user can create users)**|
|11| Once admin account(s) is created, **Log out of superuser account** and **login to created admin account**| 
|12|**(While Logged into the Admin Account)** <br/><br/> Create Educator account(s) and Student account(s)| Note: <br/><br/> Educator accounts can create test/quizes/modules and etc. <br/><br/> Student accounts can attempt created tests/quizes |





<!-- 
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
|7| These are the total **groups** to add|![Guide11](/static/images/guide11.png)| 
-->
