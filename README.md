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

## API Documentation
API documentation can be found [here](https://documenter.getpostman.com/view/25896074/2sAXqzWJD5#197769ea-03ae-4beb-b023-352dbb800ac3)

## Contribution
To contribute to this project
1. Fork the project
2. Create a branch off master using the below branch name semantics
    - feat/branch-name - For new features
    - impr/branch-name - For any improvements like performance or refactoring
    - fix/branch-name  - For bug fixes
3. Open a pull request. Kindly add documentation to make it easier to review. Use the below headings as guide;
    ```md
    ## What is this?
    ## Why are you doing this?
    ## How are you doing this?
    ```

