# Kickstarting the project

### Why Containerization?

- A number of times the same code running on a local/test environment might fail on production due to the difference in the environment.

- Using containerization we get rid of the possibilities of such occurrences, by creating a production like environment on all the dev/testing setups. 

- Setting up the local dev/test environment is now just a single command away.

### How does the setup look like?

The various services needed for running the backend services would run in separate containers once 
the setup is complete using this documentation.

You should expect to see 2 containers up and running - MySQL and the backend application.

### How do I do that?

Before you start to spin up containers on your machines, we need:
```
1. Docker - https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
2. Docker Compose - https://docs.docker.com/compose/install/#install-compose-on-linux-systems
3. Portainer - https://www.portainer.io/installation/
```

The 3rd one is the recommended GUI client for managing the containers, however if you plan on sticking to the CLI, you
could skip that.

```
4. Get the codebase on your local machine
4. Navigate to the code directory and issue: docker-compose up -d
```

The above command tells docker compose to use the `docker-compose.yml` file in the current directory and use it to build
images and spin up the containers in the background.

If you don't have the compose file in the directory, you'll see:

```
docker-compose up -d
ERROR: 
        Can't find a suitable configuration file in this directory or any
        parent. Are you in the right directory?

        Supported filenames: docker-compose.yml, docker-compose.yaml
```

So, make sure you're running this in your main project path.

### Okay, what's next?

When you've run the above command sit back and let compose do it's job. 

It would take around 10 mins for the entire setup to be complete.

**How do I know that I have successfully setup everything?**

When the installation finishes, you'll see:

```
Starting bedoff-mysql   ... done
Starting bedoff-backend ... done
```

This implies that all the services are being run in separate containers.

If this fails, retry:

```
docker-compose stop && docker-compose rm -f && docker-compose pull && docker-compose build --no-cache && docker-compose up -d --force-recreate --remove-orphans
```
You could also navigate to `localhost:9000` if you've installed portainer as mentioned above 
and see all your containers up and running.

#### Brief insights into what's happening under the hood:

So, when you issue a `docker-compose up -d` as mentioned above, the tool uses the compose file and
installs all the dependencies and gets them up and running. The containers also get registered to 
a local network which they use to identify and communicate with hosts. For example: Our backend
wanting to talk to MySQL. 

If you take a look at the `docker-compose.yml` file, you'll find: 

```
links:
    - mysqldb
```
These are the hosts on the local network that the web services needs to talk to which we define 
in our compose file as : `hostname: mysqldb` etc.

The `-d` flag tells compose to run it in detached mode(i.e. in the background).

To get details about the local network you could do:
```
docker inspect bedoff-backend_1 -f "{{json .NetworkSettings.Networks }}"
```

More helpful stuff about the docker network could be found here: https://stackoverflow.com/a/43904733

**How does my code change directly reflect inside the containers?**

Well, there's something called volume and port binding when using containers.

So, if you take a look at the `docker-compose.yml`, it says: 

```
volumes:
    - '.:/bedoff'
```

which means that we tell docker to bind my current directory referenced by `.` to `/bedoff` inside 
container. So, any code change in the current directory would be directly reflected inside the container

We also have:
```
ports:
    - '8005:8000'   
```
which tells docker to bind the host machines port number 8001 to 8000 on the above container.

So, every request on `localhost:8005` will be forwarded to `8000` on the above container.

That's pretty much about it!

### Helpful docker commands

```
1. docker --version
2. docker info
3. Find an image in the global docker registry: docker search <image_distribution_name>
4. View all images: docker images -a
5. View all running containers: docker ps
6. View all containers: docker ps -a
7. ssh into a running container: docker exec -it <container_id> /bin/bash
``` 

Other useful commands can be found here: https://dzone.com/articles/top-docker-commands-itsyndicate

### How do I commit code?

When you're done with your changes you could push your code using git from the host machine itself.
This is as usual, nothing docker specific here.


### How do I explicitly ensure my code gets updated inside the container?

Although, that won't be necessary after the volume binding and the Stat Reloader on Django you may
issue `docker-compose up -d` after your code changes to be completely sure.

### How do I use the debugger?

```
1. docker attach <container_id>
```
You would get an attached terminal to a running container to control I/O operations.

Now you would get your debugged arrangement on the command line and you can play around with it.

### Still need help?

Reachout to the maintainers:
* waqashamid722@gmail.com
