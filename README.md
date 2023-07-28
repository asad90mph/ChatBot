# ChatBot
## Basic Application Setup
#### There are 2 ways to setup this project
* [Docker](#Docker) - **Preferred**
* [Conventional](#Conventional) - **Creating Virtual Environment**

# Docker

### Prerequisites

* [Docker](https://www.docker.com) >=17.04.0 Installation guide [Ubuntu](https://docs.docker.com/v17.09/engine/installation/linux/docker-ce/ubuntu/) [Mac](https://docs.docker.com/docker-for-mac/install/) [Windows](https://docs.docker.com/docker-for-windows/install/)
* [Docker Compose](https://docs.docker.com/compose/install/) >=1.17.1


Verify docker and docker compose installed successfully
```
docker -v
docker-compose -v
```

To make the image of this flask app using docker
```
docker build -t my-flask-app . 
```
After run the docker container using following command
```
docker run -p 5000:5000 my-flask-app
```


# Virtual Environment

Run this command to root directory to create virtual environment

```
python3 -m venv <name_of_virtualenv>
```

For ubuntu - Linux and macos run this command to activate virtual environment

```
source <name_of_virtualenv>/bin/activate

```

For windows
```
<name_of_virtualenv>/Scripts/activate
```

After activating virtual Environment run this command to install all requirements

```
pip install -r requirements.txt
```

To start the app run this command

```
python app.py
```

# End Points

* http://127.0.0.1:5000/initialize (This endpoint initialize the OpenAI API with the required credentials and settings) POST
in body {"api_key":"value of API Key"}

* http://127.0.0.1:5000/create_prompt (This endpoint takes a user-provided prompt as input and store it for later interactions with the ChatGPT bot and return the index where this prompt stored) POST in body {"prompt":"What is the capital of Pakistan?"}
* http://127.0.0.1:5000/get_response (This endpoint takes the index of a previously stored prompt and return the ChatGPT bot's response to that prompt)
POST in body {
    "prompt_index": 0
}
* http://127.0.0.1:5000/update_response (This endpoint update an existing prompt at the given index with a new prompt provided by the user) 
POST in body {
    "prompt_index": 0,
    "new_prompt" : "What is Geeks for Geeks?"
}


