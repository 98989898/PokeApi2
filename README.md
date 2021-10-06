# Pokemon 

This repo contains a command fetch_chain in the query.py file, that receives as its paramenter an ID, representing the Evolution Chain and stores the given evolution chain by querying the data from the [PokeApi](https://pokeapi.co/). It also contains a script massquery.py that queries and stores data for all evolutionary chains. 

After querying desired pokemon data run the API which takes as parameter the name of a Pokemon and returns the Pokemon's information.

## Setup &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-397/)

- Set up and activate the local development environment.


- Install the requirements using pip:

    ```sh
    pip install -r requirements.txt
    ```

- Setup local database by using django migrations

    ```sh
    python Pokemon/manage.py makemigrations
    python Pokemon/manage.py migrate
    # This will setup the local database based on django models. Make sure you are in the same directory as manage.py file
    ```

- Fetch and store information manually by using the query.py file or fetch and store all evolution-chains and pokemon by running the massquery.py file as follows:

    ```sh
    python Pokemon/manage.py shell < Pokemon/massquery.py
    # This will fetch and store pokemon information. Make sure you are in the same directory as manage.py and massquery.py.
    ```

- Run the server as follows:

    ```sh
    python Pokemon/manage.py runserver
    ```

- If your development server is at localhost then you can acces the api by using:

http://127.0.0.1:8000/charmander/

You can change the name of the pokemon and the ip/url depending on your local settings and the name of the desired pokemon. 
