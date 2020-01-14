# Notes

## Changelog

### Add pytest framework for testing

### Add postgres image for local development and testing
* Add the service to the docker-compose file
* Add seed_db command, that creates some dummy data in the db

### Set up configuration
* Create a config.py module inside the project to hold the configs
* Set up the project, so that the used config can be set via the APP_SETTINGS environment variable (which is injected with the docker-compose)

### Add dockerization and use docker-compose
* Add dockerfile, use python3.8-__alpine__ image, for smaller image size
* Add docker-compose.yml file, which sets up the volumes and some environment variables, ports

### Create basic app with Ping resource