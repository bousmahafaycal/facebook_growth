# Facebook Growth
Faceboook tools for growth

## Installation
`pip install -r requirements.txt`
## Demo

### Send a message to all your friends
`python3 main.py send_friends`

### Send a message to all users of a group
Copy the csv file you get with scraper in this directory.  
`python3 main.py send_group`

## Config

Your email, password and csv file name are asked each time you execute this script.
To avoid this, you can define environment variable in your terminal to be used by default.
Following are available:

 - EMAIL
 - PASSWORD
 - CSV_FILE
 
For exemple, if you don't want to enter your email at each execution, just do:

 ```export EMAIL=xxxxxx@xxxxx.com```
 
