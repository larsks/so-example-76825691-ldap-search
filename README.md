This repository is part of [this answer](https://stackoverflow.com/a/76831533/147356https://stackoverflow.com/a/76831533/147356).

To run the demo:

1. Bring up the LDAP server:

    ```
    docker compose up -d
    ```

1. Set up the virtual environment:

    ```
    pipenv install
    ```

1. Run the example:

    ```
    pipenv run python search_example.py
    ```
