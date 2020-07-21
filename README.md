# Docker - Flask API Framework
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/Code-GitHub-yellow.svg)](https://github.com/leomaurodesenv/docker-flash-api)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c540ed1976e1487eb6961ab0f057befc)](https://www.codacy.com/manual/leomaurodesenv/docker-flash-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leomaurodesenv/docker-flash-api&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.com/leomaurodesenv/docker-flash-api.svg?branch=master)](https://travis-ci.com/leomaurodesenv/docker-flash-api)
   
This repository is the basis for a fast, efficient and scalable python API environment.   
This framework presents a continuous integration test using [Travis CI](https://travis-ci.com/), a [Docker](https://www.docker.com/) image to deploy your project, and, finally, a simple API Restful implementation to allow security access for everyone; facilitating the test, development and deployment for production.  

---
## Start Coding
### Installation

Important links: [DockerHub](http://hub.docker.com/), [Documentation](https://docs.docker.com/).   

Each Operating System (OS) have its own steps.   
**Note**: Docker CE (Community Edition), Docker EE (Enterprise Edition).   

```shell
# build image
$ docker build -t flash-api .
# running container
$ docker run -it --rm --name flash-api-container -p 5050:5050 flash-api
```

Done! You can access your API in http://localhost:5050/api/?get=message.   

### Coding your API

Modify [app/api.py](app/api.py) Python file; add your API logic.   

```python
# Called when the service is loaded
def init():
# Called when the API is requested
def run(args):
```

---
## Deep personalization

Useful personalizations:   
-   Add Python libraries for your API; see [requirements.txt](requirements.txt).
-   Add new API methods; see [app/daemon.py](app/daemon.py).
-   Improve the continuos integration tests; see [travis.yml](travis.yml).
-   Improve the Docker image; see [Dockerfile](Dockerfile).
-   Create an issue for any questions or suggestions!

---
## Also look ~

-   License [MIT](LICENSE)
-   Created by Leonardo Mauro ~ [leomaurodesenv](https://github.com/leomaurodesenv/)