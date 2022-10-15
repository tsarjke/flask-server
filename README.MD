# Counter app

You can find the docker image [here](https://hub.docker.com/r/tsarjke/flask-server)

```
docker pull tsarjke/flask-server
docker run -p 80:80 tsarjke/flask-server
```

open localhost to see the counter  
open localhost/stat to increment the counter and see the new value  
open localhost/about to see the html with the hostname  