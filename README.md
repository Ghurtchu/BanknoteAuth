If you want to run it and test it you need to have Docker installed on your local machine.

Here are the instructions:

if you see something like this <some-text> it means that you can provide any string inside of <> brackets

Go to project root directory and execute following commands, make sure thad Docker daemon is on and running

1) docker build -t <docker-image-name> .
2) docker run -p 5000:8080 <docker-image-name>
3) go to localhost:5000/apidocs
4) enjoy!
