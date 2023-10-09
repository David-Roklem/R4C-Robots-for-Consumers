# Russian Robotics

First of all, you need to clone this repo to your local machine:

1. **Clone the repo**
```
git clone https://github.com/Ydtalel/R4C.git
```

2. **Set up all the requirements using poetry**
```
cd R4C
poetry install
```

3. **Apply migrations**

```
poetry run python manage.py migrate
```
alternatively, enter poetry shell and then use generic python commands:
```
poetry shell
python manage.py migrate
```

5. **Launch development server**

```
python manage.py runserver
```
Your project is ready to use: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

_____________________________________________________________________
## How to interact with the API

### Adding the robot

I reccomend using API development platform for sending requests, such as Postman.
Send a POST request to this address [http://127.0.0.1:8000/api/create-robot/](http://127.0.0.1:8000/robots/new-robot/).

In `body` menu choose `raw` and fill example data in JSON format.   
Sample data:

```json
{
 "model": "R2",
 "version": "D2",
 "created": "2022-12-31 23:59:59"
}
```
### Download Excel-file

To download a report file in exel format go to this address using any browser: 
```
http://127.0.0.1:8000/robots/download-report/
```
### Sending letters

In this project letters are sent to terminal for demonstration purposes only
