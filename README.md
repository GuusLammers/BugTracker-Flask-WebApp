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
<b>2-</b> You will need to create a Python environment and install the following libraries: </br> 
   <b>a-</b> flask</br> 
   <b>b-</b> werkzeug</br> 
   <b>c-</b> flask_login</br> 
   <b>d-</b> flask_sqlalchemy</br> 
<br>   
<b>3-</b> You will also need to create the database by following the next instructions:</br> 
   <b>a-</b> Open your terminal and set your directory to the folder where flaskr is stored.</br> 
   <b>b-</b> Open your python repl by typing either 'py' or 'python' (depending on your computer) and pressing enter.</br>
   <b>c-</b> Import database and create app by typing 'from flaskr import db, create_app' and pressing enter.</br>
   <b>d-</b> Create database by typing 'db.create_all(app=create_app())' and pressing enter. If it worked a db file should have appeared in your flaskr folder named db.bugtracker.</br>
   <b>e-</b> Exit your python repl by typing 'quit()' and pressing enter.</br>
<br>   
<b>4-</b> Set up flask app to run on your local host:</br>
   <b>a-</b> Open your terminal and enter the following commands.</br>
   <b>b-</b> Enter 'set FLASK_APP=flaskr' and press enter.</br>
   <b>c-</b> Enter 'set FLASK_ENV=development' and press enter.</br>
   <b>d-</b> Enter 'flask run' and press enter.</br>
<br>   
<b>5-</b> After entering the last command the flask app should be running. A link to your localhost will have appeared in your terminal. Click the link and the application will open.</br>
<br>
<b>6-</b> Create an account and use the application to keep track of your projects.</br>


# Application Pictures
1- Active Projects Page
<p align="middle"><img src="images/active projects.JPG" width="75%" height="75%"></p>
