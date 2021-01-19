# finance_ticker
Minimalist version of an app that gets the stock price of stock ticker using an 3rd party API

## installation steps
1) Create a dedicated new folder for the project

2) Change directory to the new folder  

    cd stock_app/

3) Set up the virtual environment of Python  

    python -m venv env

3) Activate the new environment using the script  

    source env/bin/activate

4) Install the required libraries  

    pip install -r requirements.txt
    
5) Set and run the Flask server  

    FLASK_APP=server FLASK_ENV=development flask run
    
6) Launch your web browser and type the following url  

    http://localhost:5000/stock/AAPL
