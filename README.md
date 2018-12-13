[![Build Status](https://travis-ci.org/katherine95/iReporter.svg?branch=develop-api-v2)](https://travis-ci.org/katherine95/iReporter) [![Coverage Status](https://coveralls.io/repos/github/katherine95/iReporter/badge.svg?branch=develop-api-v2)](https://coveralls.io/github/katherine95/iReporter?branch=develop-api-v2)
[![Maintainability](https://api.codeclimate.com/v1/badges/68e36e977cb3d0d710b2/maintainability)](https://codeclimate.com/github/katherine95/iReporter/maintainability)
# iReporter
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

This site is published at https://katherine95.github.io/iReporter/UI/index.html

### Prerequisites

```
Html5, CSS3, python, flask, flask_restful 
```

##  Getting Started  ##

1. Clone this repository
   ```git clone https://github.com/katherine95/iReporter.git```
2. Change the directory into the project directory.
    ```cd iReporter```
2. Fetch all origin to get all branches
    ```git fetch origin```
3. Checkout to `develop-api-v2` branch.
    ```git checkout develop-api-v2```
4. Create a virtual environment to allow you to manage separate package installations for different     projects.
    ``` virtualenv -p python3 venv```
5. Activate virtual environment
    ``` source venv/bin/activate```
5. Install requirements(all packages that the project needs)
    ```pip install -r requirements.txt```
6. Start server
    ``` export FLASK_APP=run.py```
    `flask run`
7. Test the endpoints on postman.

    EndPoint   |   Url                          | Functionality
    -----------|--------------------------------|----------------------
    POST       | /api/v2/auth/signup            | Register a user
    POST       | /api/v2/auth/login             | User log-in with valid username and password
    GET        | /api/v2/auth/signup            | Get all registered users
    POST       | /api/v2/incidents              | Allow authenticated user to create an incident
    GET        | /api/v2/incidents              | Allow authenticated user to fetch all incidents created
    GET        | /api/v2/incidents/<int:id>     | Allow authenticated user to fetch a single incident
    PATCH      | /api/v2/incidents/<int:id>     | Allow only an admin to change the status of an incident
    PATCH      | /api/v2/user/incidents/<int:id>| Allow user to edit comment/location of his/her records
    DELETE     | /api/v2/incidents/<int:id>     | Allow authenticated user to delete his/her records 

8. To run migrations:
    run ```python3 migrate.py```
9. To run tests:
    run ```pytest```
10. To check test coverage:
    run ```py.test --cov=app app/tests/v2```

    # Link to Hosted [demo]()

