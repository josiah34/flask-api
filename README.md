# flask-api


### This is project to learn flask 






**Docker Notes**

- Command to run docker image with local code to enable live changes so that I dont have to build a new image every time I make a code change.:

   `` docker run -dp 5000:5000  -w /app -v "$(pwd):/app" flask-smorest-api``

- Command to attach to the running container and view the console output:'
   ``docker attach CONTAINER_ID``



