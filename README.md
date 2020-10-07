# Installs

1. Python 3.7 (I'm using 3.7.3) or later
2. Visual Studio Code
3. PostgreSQL (I'm using V12.4) - remember the password you use during installation

# Local PostgreSQL Setup

1. Open pgAdmin 4 (it should come installed with PostgreSQL)
2. Use the password you used during installation to log in
3. Create new local database with any name:
   > Servers -> PostgreSQL 12 -> right click Databases -> Create Database...

# Pre-setup

1. Open terminal and set environment variable:
   > setx SECRET_KEY 'PUT SECRET KEY I SENT YOU'
2. Restart computer
3. Download local_settings.py file I sent you
4. Change the NAME field to the name of the database you created
5. Change the PASSWORD field to the password you used during PostgreSQL installation

# Local Django Setup

1. Use terminal to clone repository into new folder, name it anything:
   > git clone https://github.com/ryantran2165/office-supply-depot-backend.git
2. Put local_settings.py file inside 'office-supplydepot-backend/osd/osd'
3. Open terminal in folder you created and create virtual environment:
   > python -m venv venv
4. Use terminal to activate virtual environment:
   > source venv/Scripts/activate
5. Change directory into 'office-supply-depot-backend':
   > cd office-supply-depot-backend
6. Install packages from requirements.txt:
   > pip install -r requirements.txt
7. Open folder you created in Visual Studio Code:
   > File -> Open Folder...
8. Select venv as Python interpreter in bottom left where it says "Select Python Interpreter"
9. Run on localhost to test that it works:
   > python manage.py runserver
