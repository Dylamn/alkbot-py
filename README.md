# Alkbot py
The python implementation for the discord bot named Alkbot.

## Overview
Alkbot is a fun but slightly insulting discord bot.

## Installation
Copy the ``.env.example`` file at the root of the project and rename it ``.env``.
You must, for the moment fill the ``TOKEN`` property with a discord bot token.

Then, in order to run the bot, you must install its dependencies which are
listed in the ``requirements.txt`` file with pip:
````shell
$ pip install -r requirements.txt
````

### Virtual Environments
Sometimes you want to keep libraries from polluting system installs 
or use a different version of libraries than the ones installed on the system.  
For this purpose, the standard library as of Python 3.3 comes with the "venv" 
module in order to help maintain these separate versions.
These are others libraries which do the same but here we'll keep with the standard.

For a more in-depth tutorial, 
check the [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html) documentation.

So, lets create our virtual environment:
1. Go to the ``alkbot-py`` project directory:
    ```shell
    $ cd path/to/alkbot-py
    ```
2. Create your virtual environment:
    ```shell
    $ python3 -m venv my_venv
    ```
3. Activate your virtual environment:
    ```shell
    $ source my_venv/bin/activate
    ```
    On Windows it will be a little different:
    ```shell
    $ my_venv\Scripts\activate.bat
    ```
   > If you use Powershell, the file to use is ``activate.ps1`` instead.

You now have finished setting up your virtual environment.

> To exit the virtual environment, simply type the command ``deactivate``

## Run
To start the bot, simply write the following command:
````shell
$ python main.py
````
