# Free The Citizens App
## Description
The free Citizens app is to keep historical data during the #StopGalamseyNow protest

## How to run this?
### Running server
1. Create a python virtual environment
`python3 -m venv venv`
2. Activate virtual environment
`source venv/bin/activate`
3. Run `pip3 install -r requirements.txt`
4. From the root directory run `python manage.py runserver` to run the server

### Navigate to admin
1. You can go navigate to the admin website navigating to the url `localhost:[port_number]/admin`
2. You can first create an admin account by running `python manage.py createsuperuser` in the root directory.

### Navigate to events
1. You can go navigate to the admin website navigating to the url `localhost:[port_number]/events/`
