# Cimex Bug Tracker Flask Web Application
 This is a Flask web application that can be used to track bugs in your coding projects! It allows you to sort projects and tickets into categories like active and complete and open and closed respectively.

# What I Learnt
<ol>
 <li>Worked with Flask to build backend of application.</li>
 <li>Implemented a one to many SQLite database using SQLAlchemy with full CRUD functionality.</li>
 <li>Modified HTML of an existing bootstrap template to create a front end with a clean aesthetic.</li>
 <li>Implemented full authorization/authentication functionality using flask_login.</li>
</ol>

# User Instructions
<ol>
 <li>To use or test out the application yourself you will first need to download all of the files in the 'flaskr' folder and store them on somewhere on your computer.</li>
 <li>You will need to create a Python environment and install the following libraries:
  <ol>
    <li>flask</li>
    <li>werkzeug</li>
    <li>flask_login</li> 
    <li>flask_sqlalchemy</li>
  </ol>
 </li>   
 <li>You will also need to create the database by following the next instructions:
  <ol>
    <li>Open your terminal and set your directory to the folder where flaskr is stored.</li>
    <li>Open your python repl by typing either 'py' or 'python' (depending on your computer) and pressing enter.</li>
    <li>Import database and create app by typing 'from flaskr import db, create_app' and pressing enter.</li>
    <li>Create database by typing 'db.create_all(app=create_app())' and pressing enter. If it worked a db file should have appeared in your flaskr folder named db.bugtracker.</li>
    <li>Exit your python repl by typing 'quit()' and pressing enter.</li>
  </ol>
 </li>   
 <li>Set up flask app to run on your local host:
  <ol>
    <li>Open your terminal and enter the following commands.</li>  
    <li>Enter 'set FLASK_APP=flaskr' and press enter.</li>  
    <li>Enter 'set FLASK_ENV=development' and press enter.</li>  
    <li>Enter 'flask run' and press enter.</li>  
  </ol>  
 </li>   
 <li>After entering the last command the flask app should be running. A link to your localhost will have appeared in your terminal. Click the link and the application will open.</li>
 <li>Create an account and use the application to keep track of your projects.</li>
</ol>

# Application Pictures
<ol>
 <li>Active Projects Page
 <p align="middle"><img src="images/active projects.JPG" width="75%" height="75%"></p></li>

 <li>Create Projects Page
 <p align="middle"><img src="images/create project.JPG" width="75%" height="75%"></p></li>

 <li>Open Tickets Page
 <p align="middle"><img src="images/open tickets.JPG" width="75%" height="75%"></p></li>

 <li>Create Ticket Page
 <p align="middle"><img src="images/create ticket.JPG" width="75%" height="75%"></p></li>
</ol>
