## Awards
## Author
    Joan Kirui

## Description

  This is a django application that allows users to post their projects for others to rate and review based on usability,content and design.

## Screenshot
    ![Awards](/static/images/main.png)
    
<h3> Live Link:</h3>
    [https://jkawards.herokuapp.com/]

## User Story
    * A user can view posted projects and their details.
    * A user can post a project to be rated/reviewed.
    * A user can rate/ review other users' projects.
    * Search for projects.
    * View projects overall score.
    * A user can view their profile page.

## Setup and Installation
    To get the project ...

<h3>Cloning the repository:</h3>
    https://github.com/joankirui/Awards.git

<h3>Navigate into the folder and install requirements</h3>
    cd Awards pip install -r requirements.txt

<h3>Install and activate Virtual</h3>
    - python3.6 -m venv virtual 
    - source virtual/bin/activate  

# Setup Database 
    SetUp your database User,Password,Host then make migrate
        python manage.py makemigrations awards

    Now Migrate 
        python manage.py migrate 

    Run the application
        python3.6 manage.py runserver

    Testing the application
        python manage.py test

    Open the application on your browser 127.0.0.1:8000.

<h3> Api Endpoints:</h3>
    https://jkawards.herokuapp.com/api/profile<br>
    https://jkawards.herokuapp.com/api/posts



## Technology used
    python3.6
    Django 3.2.9
    Heroku

## Known Bugs
    * There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
    If you have any question or contributions, please email me at [joankirui99@gmail.com]

## License
    MIT License
    Copyright (c) 2021 Joan Kirui


