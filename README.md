## Table of Contents
### Note: Setup **must** be done
### Note: Either Fresh Database Configuration **OR** Database Import Configuration **must** be done

- [Windows Setup Guide](#Windows-Step-by-Step-Setup-Manual)
- [MacOS Setup Guide](#MacOS-Step-by-Step-Setup-Manual)
- [New Database - Configuration](#Step-by-Step-One-Time-Configuration)
- [Existing Database Import - Configuration](#Step-by-Step-Existing-Database-Configuration)
- [Guide to manually create Superuser](#Step-by-Step-Manual-Superuser-Creation)
- [Guide to manually create Admin](#Step-by-Step-Manual-Admin-Creation)
- [Guide to remove 2 existing user accounts in existing imported database](#To-remove-two-existing-user-accounts-in-existing-database-imported)

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
| Enter `CREATE DATABASE oaies;` | Or any other database name. But it must be changed in the settings.py file |
| Open scripts folder (in the python folder in appdata/program) where pip is located in cmd |
| Enter `pip install mysqlclient` |
| Enter `pip install django-utils-six` |
| Enter `pip install pdfplumber` |
| Enter `pip install django-quill-editor` |
| Enter `pip install django-tinymce` |
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
| Enter `CREATE DATABASE oaies;` | Or any other database name. But it must be changed in the settings.py file |
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
| Enter `pip install django-quill-editor` |
| Enter `pip install django-tinymce` |
| Download project zip |
| Extract downloaded zip to virtual env folder created |
| Open the folder containing the manage.py file, <br/>then, right click on the folder name on the folder path, <br/>then select `open in terminal`<br/><br/> Or just manually cd into the folder containing the manage.py file in terminal| **Always Do This before running the server or performing runserver** |
| Enter `python manage.py makemigrations` |
| Enter `python manage.py migrate` |
| Enter `python manage.py runserver` | This step is only to confirm it works. <br/><br/> **Run this command every time to run server** |
| Press ctrl+C to stop server from running |
| Perform these steps next - [Configuration](#Step-by-Step-Configuration) |

## Step-by-Step One-Time Configuration
### Warning: This is required (only once during setup for the first time/or the resetting of the database), if not you cannot use the system/application
### Warning: Please do not skip any steps, unless it is an optional steps marked with `+`

|Step| Description | Screenshot/Note |
|-----|-------------|---------|
|1| Create a superuser with `python manage.py createsuperuser`| **Note: If this step fails, or is unable to login, Use `step 1.+`** |
|1.+| First, Comment out the following in `register/views.py`. <br/><br/> **Note:** In the original **untouched `views.py`**,<br/>all the commented out lines in the screenshot is **not commented out** by default |![Guide5](/static/images/guide5.png)<br/><br/>Note: This is what it should look like after performing this step|
|1.+| Then, in `register/forms.py` uncomment highlighted |![Guide6](/static/images/guide6.png)<br/><br/>Note: This is what it should look like after performing this step|
|1.+| Then, in `register/forms.py` comment out the highlighted <br/><br/> (**Note: role field is neccessary to assign user to group**) <br/><br/> (**Warning: role field will interfere with creating superuser if present**)|![Guide7](/static/images/guide7.png)<br/><br/>Note: This is what it should look like after performing this step|
|1.+|Then, in `templates/registerUser.html` comment out `line3`, `line4` and `line 17` to `line 72`| ![Guide9](/static/images/guide9.png)<br/><br/>Note: This is what it should look like after performing this step|
|1.+|Then, in `templates/registerUser.html` uncomment `line73` and `line74` <br/><br/>Note: To uncomment, <br/>just remove `{% comment %}` <br/> and remove `{% endcomment %}` <br/>from `line73` and `line74` | ![Guide10](/static/images/guide10.png)<br/><br/>Note: This is what it should look like after performing this step|
|2| CD into folder w/ manage.py then enter `python manage.py runserver` to run server|
|3| Go to http://127.0.0.1:8000/registerUser/ and create superuser| Note: Tick **both** `staff` and `superuser` when registering |
|+| This error will appear, **ignore it**|![Guide8](/static/images/guide8.png)|
|4| Open a browser and enter http://127.0.0.1:8000/admin/ |
|5| Login with the superuser login created |
|+| **If used `step 1.+` to create superuser, and is able to login to admin panel, UNDO all `step 1.+`**| **Note: VERY IMPORTANT STEP** |
|6| Go to http://127.0.0.1:8000/admin/, and select `add` to add groups <br/><br/> (Note: Please follow order of adding groups) |![Guide1](/static/images/guide1.png)|
|7| Add the following permissions to the **`Admin`** group, then save |![Guide2](/static/images/guide2.png)|
|8| Add the following permissions to the **`Educator`** group, then save <br/><br/> **Filter: build, then choose all**<br/><br/>**Note: all except** `admin, auth, contenttypes, sessions` **permissions**|![Guide4](/static/images/guide4.png)|
|9| Add the following permissions to the **`Student`** group, then save |![Guide3](/static/images/guide3.png)|
|10| To create admin account, <br/><br/>  **Comment out `group_required` only** (like in the above step), <br/><br/> **Go to** http://127.0.0.1:8000/registerUser/ and **create admin account, <br/><br/> then uncomment `group_required` again.** <br/><br/> | (**Note: Do this while logged into the superuser account**) <br/><br/> **(Note: This is important to add users for the application/system)** <br/><br/>**(Warning: Must uncomment `group_required` Otherwise, any user can create users)**|
|11| Once admin account(s) is created, **Log out of superuser account** and **login to created admin account**| 
|12|**(While Logged into the Admin Account)** <br/><br/> Create Educator account(s) and Student account(s)| Note: <br/><br/> Educator accounts can create test/quizes/modules and etc. <br/><br/> Student accounts can attempt created tests/quizes |

## Step-by-Step Existing Database Configuration

|Step | Note |
|-------------|------------|
|Follow setup manual for your specific OS in the Manuals folder first then perform the below steps|
|Download MySQL workbench|
|Open the database folder|
|Select Instance of mysql connection|
|Click on data import/restore|
|Select Dump20220217 folder inside the Database folder to be imported|
|Superuser Account Credentials <br/><br/>- To **access admin panel**| Username: Owner <br/><br/> Password: oaies@123|
|Admin Account Credentials <br/><br/>- Account used to create new admin, educator, and student accounts|Username: Admin <br/><br/> Password: oaies@123|

## Step-by-Step Manual Superuser Creation

|Step |
|-------------|
|**Must** have completed the setup **and** either the new database config or the existing database import config|
|Use existing superuser account to login to system|
|Access admin panel @ http://127.0.0.1:8000/admin/|
|Create New User|
|Enter desired credentials/info|
|Set `as staff` and `superuser` status `on`|
|Create New Profile|
|Link the new profile to new user <br/><br/>**- important as profile model is linked to the user model**|
|Done|

## Step-by-Step Manual Admin Creation

|Step | 
|-------------|
|Log into the existing admin account|
|Go to http://127.0.0.1:8000/registerUser/|
|Create a new admin account <br/><br/>**- double check role selection and select Admin**|
|Done|

## To remove two existing user accounts in existing database imported
### Note: Only for those who had used the imported database
### Warning: Do not perform this step before creating your own superuser and admin account and before double checking newly created superuser and admin account works

|Step |
|-------------|
|Login to superuser account|
|Go to http://127.0.0.1:8000/admin/|
|Select accounts to be deleted|
|Delete them|
|Done|
