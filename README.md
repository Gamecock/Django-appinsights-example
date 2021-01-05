#APPINSIGHTS With DJANGO

Based on basic Django Tutorial
https://docs.djangoproject.com/en/3.1/intro/tutorial01/

Two major areas are modified in settings.py
1) For request data
OPENCENSUS and MIDDLEWARE

2) For 'Trace' i.e. Log Data
LOGGING
* Logging is currently commented out to analyse a request issue.

## Build Instructions
* Rename env.txt to .env
* Add your appinsights instrumentation key
* Open terminal in root directory
* type `docker build -t example .`

## Run instructions
* Open terminal in root directory
* type `docker run -p 8000:8000 --env-file .env example`
* DJANGO logs appear in terminal
* Open http://localhost:8000/polls in browser.

