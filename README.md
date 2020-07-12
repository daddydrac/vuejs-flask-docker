## Flask REST Plus, VueJS, and automated unit testing via Flask CLI 
Test driven docker solution using VueJS, Flask, PostgresSQL, with swagger, & prebuilt authentication+JWT's running on NGINX/https

### Getting Started

``` docker-compose up -d --build ```


### The VueJS UI will be on:

``` https://localhost:4433/ ```

### The backend API routes will be on:

``` https://localhost:4433/<api route> ```


### Seed Postgres DB with Flask CLI

```docker-compose exec backend python manage.py create```

```docker-compose exec backend python manage.py seed```

### The default login creds that seed the db are:

<p><strong>User: </strong>  <em>avengers@gmail.com </em></p>
<p><strong>Pass: </strong>  <em>supersecret </em></p>



### Then see the json returned from the users API route here:

``` https://localhost:4433/users ```


### Run automated unit tests

```docker-compose exec backend pytest "project/tests" -p no:warnings --cov="project"```


### Swagger URL

``` http://localhost:5001/swagger ```

-----------------------------------------------------------


### In case you need to regenerate SSL keys

Open the command line and run these commands inside the ```services/nginx/ssl``` folder to generate a self signed certificate:


``` openssl req -new -newkey rsa:1024 -x509 -sha512 -days 365 -nodes -out nginx.crt -keyout nginx.key ```


``` openssl dhparam -out dhparam.pem 1024 ```


-----------------------------
### Misc notes 

Only tested and fully functional on Linux.
