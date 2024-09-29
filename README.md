# Free The Citizens App
## Description
The free Citizens app is to keep historical data during the #StopGalamseyNow protest

## How to run this?
### Running server
1. Create a `.env` file in the root directory
```
DJANGO_SECRET_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
2. Run `docker-compose up` from the root directory, where the `docker-compose.yml` file lives, to start up your server.
3. Navigate to the shell of web app by running `docker-compose exec web sh` from the root directory.
4. Once in the shell run `python manage.py migrate` for db migrations

### Navigate to admin
1. You can go navigate to the admin website navigating to the url `localhost:[port_number]/admin`
2. You can first create an admin account by running `python manage.py createsuperuser` in the root directory.

### Navigate to events
1. You can go navigate to the admin website navigating to the url `localhost:[port_number]/events/`
