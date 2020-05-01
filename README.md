### Getting Started

```
 docker-compose up -d --build
```


### The VueJS UI will be on:

``` https://localhost:4433/ ```

### The backend API routes will be on:

``` https://localhost:4433/users ```


### Seed Postgres DB with Flask CLI

```docker-compose exec backend python manage.py create```

```docker-compose exec backend python manage.py seed```



### Then see the json returned from the users API route here:

``` http://localhost:5001/users ```


### Run automated unit tests

```docker-compose exec backend pytest "project/tests" -p no:warnings --cov="project"```


-----------------------------------------------------------


### In case you need to regenerate SSL keys

Open the command line and run these commands inside the ```services/nginx/ssl``` folder to generate a self signed certificate:


``` openssl req -new -newkey rsa:1024 -x509 -sha512 -days 365 -nodes -out nginx.crt -keyout nginx.key ```


``` openssl dhparam -out dhparam.pem 1024 ```
