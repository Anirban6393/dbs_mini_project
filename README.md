# dbs_mini_project


A RESTful API to return predictions from a trained ML model, built with Python 3 and Flask-RESTX

Development set-up instructions
First, open a command line interface and clone the GitHub repo in your workspace


PS > cd $WORKSPACE_PATH$
PS > git clone https://github.com/Anirban6393/dbs_mini_project.git
PS > cd dbs_mini_project
Create and activate a Python virtual environment, then install the required Python packages using pip


PS > virtualenv venv
PS > venv\scripts\activate.ps1
(venv) PS > pip install -r requirements.txt
Once dependencies are installed, set up the project for development


(venv) PS > python setup.py develop
Finally, run the project:


(venv) PS > python app.py


Open the URL http://127.0.0.1:1000/ with your browser, upload test.csv file and then you will see list of genre and titles returned from sqlite3.


# Docker commands
Note: Docker tag or id should be always specified in the end of the docker command to avoid issues

Build docker image from Dockerfile

docker build -t "<app name>" -f docker-files/Dockerfile . eg: docker build -t "app" -f docker-files/Dockerfile .

Run the docker container after build

docker run -p 1000:1000 app # -p to make the port externally avaiable for browsers

Show all running containers

docker ps

a. Kill and remove running container

docker rm <containerid> -f

Open bash in a running docker container (optional)

docker exec -ti <containerid> bash

Docker Entry point The ENTRYPOINT specifies a command that will always be executed when the container starts. The CMD specifies arguments that will be fed to the ENTRYPOINT 1000
