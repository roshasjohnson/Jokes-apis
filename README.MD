# Project installation 


 **Clone the repository**  

    git clone git@github.com:roshasjohnson/Jokes-apis.git
    cd Jokes-api
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate    # windows

    pip install -r requirements.txt

    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver

# visit below apis 

    http://127.0.0.1:8000/api/fetch-jokes/
    http://127.0.0.1:8000/api/jokes/