# Cimex Bug Tracker Flask Web Application
 This is a Flask web application that can be used to track bugs in your coding projects! It allows you to sort projects and tickets into categories like active and complete and open and closed respectively.

# What I Learnt
1- Worked with Flask to build backend of application.<br />
2- Implemented a one to many SQLite database using SQLAlchemy with full CRUD functionality.<br />
3- Modified HTML of an existing bootstrap template to create a front end with a clean aesthetic.<br />
4- Implemented full authorization/authentication functionality using flask_login. <br />

# User Instructions
<b>1-</b> To use or test out the application yourself you will first need to download all of the files in the 'flaskr' folder and store them on somewhere on your computer.<br />
<br>
2- You will need to create a Python environment and install the following libraries: </br> 
   a- flask</br> 
   b- werkzeug</br> 
   c- flask_login</br> 
   d- flask_sqlalchemy</br> 
<br>   
3- You will also need to create the database by following the next instructions:</br> 
   a- Open your terminal and set your directory to the folder where flaskr is stored.</br> 
   b- Open your python repl by typing either 'py' or 'python' (depending on your computer) and pressing enter.</br>
   c- Import database and create app by typing 'from flaskr import db, create_app' and pressing enter.</br>
   d- Create database by typing 'db.create_all(app=create_app())' and pressing enter. If it worked a db file should have appeared in your flaskr folder named db.bugtracker.</br>
   e- Exit your python repl by typing 'quit()' and pressing enter.</br>
<br>   
4- Set up flask app to run on your local host:</br>
   a- Open your terminal and enter the following commands.</br>
   b- Enter 'set FLASK_APP=flaskr' and press enter.</br>
   c- Enter 'set FLASK_ENV=development' and press enter.</br>
   d- Enter 'flask run' and press enter.</br>
<br>   
5- After entering the last command the flask app should be running. A link to your localhost will have appeared in your terminal. Click the link and the application will open.</br>
<br>
6- Create an account and use the application to keep track of your projects.</br>


# Application Pictures
