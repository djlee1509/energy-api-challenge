<h2>Energy API Challenge</h2>

<h3>Introduction</h3>
* Develop a read-only web API which provides specific energy yields (kWh/kWp/year) of photovoltaic systems in Germany.

* Read only Web API takes the two parameters in URL, "state" and "capacity".

* It will return in JSON format.

* Built with Flask.


<h3>Requirements</h3>

Packages and Libraries used for this project is available in the file 'requirements.txt'

<h3>Getting Started (for Developer)</h3>
<h3>Installation</h3>

Please install the necessary packages and libraries using:-

```
pip3 install -r requirements.txt
```

```
python3 app.py
```


<h3>Getting Started (client)</h3>

API has been deployed to here on Heroku.
https://germany-energy-api.herokuapp.com/

<h4>Request</h4>

GET /api/pv_yield?state={string}&capacity={int}

e.g. https://germany-energy-api.herokuapp.com/api/pv_yield?state=by&capacity=10

<h4>Response</h4>
e.g. {"yield": 11000, "state": "by"}





