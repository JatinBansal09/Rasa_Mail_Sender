# Rasa Email Sender Chatbot

## Features of the project:
- Sends multiple emails in one go
- Can be used for communication
- Can be adjusted by the needs.


## Steps to be followed to install the requirements:
- Firstly, install python 3.8
- Now, get the directory where wanna create the env.

    e.g., cd "path\to\folder"
- Then, create the environment by the following method:

    conda create --prefix "path\to\env_name\folder" python=3.8
- Activate the environment.

    e.g., conda activate .\env_name

- Now, install specific versions of TensorFlow, numpy, and pandas:

    pip install tensorflow==2.3.4 numpy==1.18.5 pandas==1.5.3

- Install pip version: 20.4.

    e.g., python -m pip install --upgrade pip==20.4

- At last, install Rasa=2.0.0:
    pip install rasa==2.0.0
- Now, the bot is ready.


## Running the model using the frontend:
- Run actions file, using:
    rasa run action
- Connect the rasa model to the port using:

    rasa run --enable-api --cors "*"

- Run the 'index.html' file after the port started running.
