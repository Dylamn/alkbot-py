# Alkbot py
The python implementation for the discord bot named Alkbot.

## Overview
Alkbot is a fun but slightly insulting discord bot.

## Installation
First, set up a virtual environment:
````shell
$ python3 -m venv my_venv
````
Copy the ``.env.example`` file at the root of the project and rename it ``.env``.
You must, for the moment fill the ``TOKEN`` property with a discord bot token.

Then, in order to run the bot, you must first install its dependencies
listed in the ``requirements.txt`` file with pip:
````shell
$ pip install -r requirements.txt
````



## Run
To start the bot, simply write the following command:
````shell
$ python main.py
````
