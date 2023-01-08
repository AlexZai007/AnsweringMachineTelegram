# Telegram Auto Answer
Convenient answering machine with only the most necessary functionality. No extra freezes.


# Installation

### Get a telegram session
1. python3 src/session/session_geter.py

### Change important information in config
2. edit src/config.py

### Edit message to send automatically
3. edit function on  src/service/message.py

### Install requirements
4. pip install -r src/requirements.txt

### Final (star program)
5. python3 src/main.py

Well done!

# Structer

📦src
 ┣ 📂handlers
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜user.py
 ┣ 📂service
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜message.py
 ┃ ┗ 📜sql.py
 ┣ 📂session
 ┃ ┗ 📜session_geter.py
 ┣ 📜config.py
 ┣ 📜main.py
 ┗ 📜users.db

## Iformation

📦src - stock way

📂handlers - message handling methods
	📜user.py - main message handling method

📂service - communication methods: bd, generators.
	📜message.py - message generator
	📜sql.py - sql access methods

📂session - session generation methods
	📜session_geter.py - message generator

📜config.py - config or strings all static variables are stored here
📜main.py - main method (used to run)



