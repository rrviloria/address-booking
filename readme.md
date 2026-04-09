
# Address booking
A project created using [FastAPI](https://fastapi.tiangolo.com/) for saving address coordinates

## Setup environment variable
* Create `.env` file in root directory
* Follow [env file sample](https://github.com/rrviloria/address-booking/blob/master/env.sample)

## Running the app using Docker
* Download [docker](https://www.docker.com/products/docker-desktop/)
* Build docker container
```shell
docker-compose build
```
* Up docker containers. Run in background
```shell
docker-compose up -d
```
* Make sure the container is running
```shell
docker ps
```
## Running the app on terminal
* Make sure to [Install pip](https://pip.pypa.io/en/stable/installation/)
* Install virtualenv

```shell
pip install virtualenv
```
* Create virtualenv
```shell
virtualenv env
```
* Activate virtualenv
```shell
. env/bin/activate
```
* Install requirements txt
```shell
pip install --no-cache-dir --upgrade -r requirements.txt
```
* Run the application in dev mode
```shell
fastapi dev app/main.py --port 80 --proxy-headers
```
## Access
Once the app is running you can access the swagger doc in
http://localhost/docs and execute the APIs.

* Create User account
<img width="1458" height="703" alt="Screenshot 2026-04-09 at 4 17 53 PM" src="https://github.com/user-attachments/assets/c76df26c-cade-4467-b74f-2390f1b950a9" />


* Clink Authorize button
<img width="564" height="204" alt="Screenshot 2026-04-09 at 4 21 15 PM" src="https://github.com/user-attachments/assets/4d5d6e12-a23b-4204-9b83-c0905e99052f" />


* Authenticate using user account
<img width="727" height="662" alt="Screenshot 2026-04-09 at 4 21 29 PM" src="https://github.com/user-attachments/assets/0ab2c770-85d2-40b3-a5f6-c5e4b71d7075" />


## Coding Standard
* Run ruff code formatting
```shell
ruff format
```
* Run import sorting
```shell
isort .
```
## Testing
* Open terminal/shell and run pytest
```shell
pytest .
```
