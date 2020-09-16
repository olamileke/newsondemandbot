### NewsOnDemandBot

------------

Telegram bot that supplies news articles upon receiving a special **/get** command. Access the bot [here](https://t.me/news_on_demand_bot "here"). 

Alternatively, open up the Telegram app and search for **newsondemandbot**.

To run this bot locally, you need to have python3+ on your system. Get it 
[here](https://https://www.python.org/downloads/ "here"). Make sure to add python.exe to your operating system path variables to be able to run python scripts from the command line.

You also need a telegram bot token and a newsapi api key. Follow the instructions found [here](https://core.telegram.org/bots#6-botfather "here") to create a new bot with its authorization token. Get a newsapi api key [here](https://newsapi.org/ "here").

Navigate into a directory of choice on your system via the terminal and clone this repository by running 

```
git clone https://github.com/olamileke/newsondemandbot.git
```

navigate into the cloned repository by running

``` 
cd newsondemanbot
```

Follow the instructions found [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/ "here") to create a virtual environment in which the bot will run.

Activate the virtual environment and install all the python packages needed for the bot to run. Do this by running

```
pip install -r requirements.txt
```

Open up the config.py file located in the application root and fill in the bot_token and api_key configuration options with the authorization token and api key created earlier.

Still in the app root in the terminal and with the virtual environment still running, run

```
python app.py
```

Open up the Telegram app to communicate with the bot.


