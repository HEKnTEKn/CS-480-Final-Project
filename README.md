# CS-480-Final-Project
Project for CS 480 - Databases with Sean Deitz.


# 1. Database

    Our application utilizes mySQL to store a database consisting of tables which bear information about all High Level and Major League Matches for the popular competitive game League of Legends.
    Data was sourced as .csv files from https://www.kaggle.com/xmorra/lol2020esports on account of most data of this type being very expensive (as many use this data for gambling on games).

## Installation
    To install the database, simply execute the code in esportsData.sql located within the root directory. This will populate the tables upon a schema you have created in mySQL under the typical mySQL configuration.

    One thing to bear in mind is that one sql call within the project will drop a user 'guest'@'localhost' and then create one under the same name, granting it SELECT privileges. This in order to allow the Custom Query feature of the application.

# 2. Application
    The application is created using python3 on Pycharm, therefore a working Pycharm installation with python installed on the system is needed in order to run this project. Furthermore, a small number of packages are installed, using the pip python package installer:

## pySimpleGUI - https://pysimplegui.readthedocs.io/en/latest/
    pip install pysimplegui

## mysql-connector-python - https://pypi.org/project/mysql-connector-python/
    pip install mysql-connector-python

# 3. README
## Installation
    Refer to 1 and 2 for installation instructions, or feel free to contact me at vfong3@uic.edu, HEKnTEKn#1111 @discord, or djtekno11@gmail.com

## Interactions
    Our Application uses pySimpleGUI to manage a very aesthetic front end. This front end allows you to pick one of many options, add any input parameters, and execute the query, where the result will be displayed on the right hand side of the screen.

    For each option, a relevant sql query is stored in a sql file, with special characters marked for replacement based upon user input in a back end file where the database connections are made. This allows the user to access specific parts of the code, rather than only broad queries.

    Also notable is the Custom Query option, where, given knowledge of the database used, allows the user to enter an entire SELECT query and receive the response. 

    Reponses are all given as tuples, to be parsed into the GUI.
    
    Each option shows a sample input or expected parameters, and the expected output:

    "01. Custom Query - Input: a mySQL query within the bounds of Select permissions - Output: The result of that query.",
    "02. Most Popular Champion - Input: role (ie. top) - Output: Champion and number of times played",
    "03. Number of Wins - Input: TeamName (ie. Fnatic) - Output: the number of wins that the given team had that year.",
    "04. Match Winner - Input: matchID (ex.5655-7249) - Output: the Winning team, and players of that team.",
    "05. Tag-Move Speed - Input: A tag of a champion (ex. Mage, Bruiser) - Output: The movespeeds of the champions, asc.",
    "06. Difficulty - Input: Champion Name(ie. Jhin) - Output: Difficulty levels.",
    "07. Health - Input: Champion Name(ie. Jhin) - Output: Health levels.",
    "08. Mana - Input: Champion Name(ie. Jhin) - Output: Mana levels.",
    "09. Move Speed - Input: Champion Name(ie. Jhin) - Output: Move Speed levels.",
    "10. Attack Damage - Input: Champion Name(ie. Jhin) - Output: Attack Damage levels.",
    "11. Attack Range - Input: Champion Name(ie. Jhin) - Output: Attack Range levels.",
    "12. Attack Speed -  Input: Champion Name(ie. Jhin) - Output: Attack Speed levels.",
    "13. Armor - Input: Champion Name(ie. Jhin) - Output: Armor levels.",
    "14. Magic Resist - Input: Champion Name(ie. Jhin) - Output: Magic Resist levels.",
    "15. All Stats - Input: Champion tag (ie.Assassin) - Output: All stats of that tag, organized by name",
    "16. Specify - Input: Team Name, Role (ie. G2 Esports, top) - Output: A list of champions the role has played on their team",
    "17. Rivalry - Input: Team A, Team B (ie. G2 Esports, Fnatic) - Output: all games between the two, and stats of them."

    Clicking the top right button on the screen will close the window and end the program execution.