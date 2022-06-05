# Images-REST-API - Django Rest Framework API for uploading images.

> REST API for uploading images.

## Table of contents

- [General info](#general-information)
- [Demo](#demo)
- [Technologies](#technologies-used)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [ToDo/Bugs](#todo-bugs)
- [Contact](#contact)

## General Information

Django Rest uploading images applications with user tiers and image thumbnails. Django Imagekit is responsible for making thubmnails, django cleanup package cleans the media directory after image delete. Database is using PostgreSQL that is hosted on ElephantSQL service.

## Demo

Use default admin user.
**login: admin**
**password: root**

## Technologies Used

- Python 3.8
- Django 4.0.4
- djangorestframework 3.13.13
- pillow 9.1.1
- django_imagekit 4.1.0
- django_cleanup 6.0.0

## Screenshots

-

## Setup

1. Create directory for an app.
2. Open up terminal within directory.

3. Git clone repository: 
```sh
git clone https://github.com/Tomz899/Images-REST-API.git
```

4. In project directory use docker command to build, start and attach containers for service.
```sh
docker-compose up
```
5. Open browser and type:
```sh
localhost:8000
```

## ToDo Bugs

- **{todo}** Limit thumbinals urls to user tier requirements.
- **{todo}** Admin panel for user tiers configuration.
- **{todo}** Get rid of old cached thumbnails.

## Contact

Created by [@me](mailto:tomek.nowak@aol.pl) - if you have any questions, just contact me!
