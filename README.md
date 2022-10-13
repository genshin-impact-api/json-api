[ ![Docker](https://img.shields.io/badge/Docker%20Image-309DEE?style=for-the-badge&logo=docker&logoColor=white) ](https://hub.docker.com/r/genshinimpactapi/json-api)
[![License Badge](https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white) ](https://www.apache.org/licenses/LICENSE-2.0)
[ ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/genshin-impact-api/json-api/Release/master?logo=github&style=for-the-badge) ](https://github.com/genshin-impact-api/json-api/actions/workflows/release.yml)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/genshin-impact-api/json-api?logo=github&style=for-the-badge)

Genshin Impact JSON API
=======================



Get Image
---------

### Docker Hub

You can pull the image from [Genshin Impact API Docker Hub](https://hub.docker.com/r/genshinimpactapi/json-api/):

    docker pull genshinimpactapi/json-api:latest

### GitHub

You could also build the image from [GitHub source repository](https://github.com/genshin-impact-api/json-api):

    git clone https://github.com/genshin-impact-api/json-api.git
    cd json-api
    docker build -t genshinimpactapi/json-api .


Standup a Container
-------------------

    docker run -d --name=genshin-impact-json-api -it -p 80:3000 genshinimpactapi/genshin-impact-json-api

> 📋 Note that we are mapping container port 3000 to host port 80, but users are free to change 80 to any _available_
> ports such as 3001


Documentation
-------------

Please checkout our [project site](http://json.genshin-impact-api.com/) to play with JSON API instantly and learn more 
about how to use the API


License
-------

The use and distribution terms for Genshin Impact [JSON API](https://github.com/genshin-impact-api/json-api) are covered
by the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).

<div align="center">
    <a href="https://opensource.org/licenses">
        <img align="center" width="50%" alt="License Illustration" src="https://github.com/QubitPi/QubitPi/blob/master/img/apache-2.png?raw=true">
    </a>
</div>
