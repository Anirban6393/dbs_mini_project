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



Setting up the model
The trained ML model is meant to be initialised and invoked to make predictions in the context of a Python unit saved inside the directory ml_rest_api/ml_trained_model. The structure of this Python module is explained in this document



Build automation
This project is built into a Docker image using the Docker Hub automated build at https://hub.docker.com/r/jgbustos/ml-rest-api/


Running the Docker container
> docker run -d -p1000:1000 jgbustos/ml-rest-api:latest
Open the URL http://localhost:1000/api/ with your browser.
