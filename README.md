# encar-parser
This is a base for receiving data from korean car marketplace encar.com<br>
Use this in educational purposes only and avoid any harmful load!

## How it works
At the moment of writing this guide script works the following way:
1) Opens website in order to register user agent (and probably IP?) to Encar API (right now it's even available through any search engine)
2) Sends requests to Encar API (Endpoints of this can be found in Developer's tools) 

## Installation

1) Clone repo <code>git clone https://github.com/arsy-off/encar-parser.git</code>
2) Set corresponding platform in <code>docker-compose.yaml</code>
3) Run <code>docker compose up -d</code>. Images of Selenium server, MongoDB, and MongoDB express will be pulled and then run
4) Check logs of app container. There should not be any exception raised

### N.B.
In order to use this without docker, set up usage of local webdriver
