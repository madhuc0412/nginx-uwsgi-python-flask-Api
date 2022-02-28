# nginx-uwsgi-python-flask-Api

This [**Docker**](https://www.docker.com/) image allows you to create [**Flask**](http://flask.pocoo.org/) web applications or API in [**Python**](https://www.python.org/) that run with [**uWSGI**](https://uwsgi-docs.readthedocs.org/en/latest/) and [**Nginx**](http://nginx.org/en/) in a single container.

## uwsgi-nginx-flask
**Docker** image with **uWSGI** and **Nginx** for **Flask** applications in **Python** running in a single container. 

## Docker Build and run
Using uWSGI and nginx for production workloads

Docker Build
```
docker build -t python-flask-app .
```

Docker run with docker-compose <br />
**Note:** verify the docker-compose file.
```
docker-compose up
```

Docker run - Detach mode
```
docker run -d -p 8089:80 python-flask-app 
```

Docker run with interactive mode - recommended for debug
```
docker run -p 8089:80 -it python-flask-app  
```

## sample test
htttp://localhost:8089/api/v1/home <br />
or <br />
htttp://localhost:8089/api/v1/home?q=test
