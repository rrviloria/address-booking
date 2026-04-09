
# Address booking
A project created using [FastAPI](https://fastapi.tiangolo.com/) for saving address coordinates

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
![create user](https://storage.filebin.net/filebin/1af87aa634d72d43fcd65ca870513aedb35dbf079b2a169de3125cac8fbf4649?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GK352fd2505074fc9dde7fd2cb%2F20260409%2Fhel1-dc4%2Fs3%2Faws4_request&X-Amz-Date=20260409T082032Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&response-cache-control=max-age%3D900&response-content-disposition=inline%3B%20filename%3D%22Screenshot%202026-04-09%20at%204.17.53%20PM.png%22&response-content-type=image%2Fpng&x-id=GetObject&X-Amz-Signature=886b8134200ca1e00f9cecb973d161103ca13b1ad7619d50f3b15b3d602cc373)

* Clink Authorize button
![button](https://storage.filebin.net/filebin/4479d255b20eaf1972f39546e692ecedb09503532318a9c3b6f8f5b83fe91035?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GK352fd2505074fc9dde7fd2cb%2F20260409%2Fhel1-dc4%2Fs3%2Faws4_request&X-Amz-Date=20260409T082157Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&response-cache-control=max-age%3D900&response-content-disposition=inline%3B%20filename%3D%22Screenshot%202026-04-09%20at%204.21.15%20PM.png%22&response-content-type=image%2Fpng&x-id=GetObject&X-Amz-Signature=cfadd2b2706321b58cc400e466dfb3c3063daffb28335f0a63404559004386bb)

* Authenticate using user account
![auth](https://storage.filebin.net/filebin/6c57a11bd179d50f69baf6ef552eabe57bdac20a5d1be9e2777ca83132b96789?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GK352fd2505074fc9dde7fd2cb%2F20260409%2Fhel1-dc4%2Fs3%2Faws4_request&X-Amz-Date=20260409T082626Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&response-cache-control=max-age%3D900&response-content-disposition=inline%3B%20filename%3D%22Screenshot%202026-04-09%20at%204.22.46%20PM.png%22&response-content-type=image%2Fpng&x-id=GetObject&X-Amz-Signature=1ef6d0b95a1959b60c23678ae53d74b3042d3a5ad5e106da756330d084e45c50)

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