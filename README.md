
## Build
docker build -f  server/containers/python/Jupyter.stretch.Dockerfile --rm -t stretch/deppface-app-image:v0.0.1 .

## RUN

docker run --name deppface-app1  -p 8888:8888 stretch/deppface-app-image:v0.0.1




# deep-face-api
Full stack data-science project


## Medium

Story about building the web application and deploying it.


### [part1](https://medium.com/@sdamoosavi/deploy-deepface-model-fastapi-develop-2e33374db6f2)
### [part2](https://medium.com/@sdamoosavi/deploy-deepface-model-fastapi-heroku-deployment-8e007e72c455)
