# Notes (for myself?)

## To remember

* __Add image that is present in the "static" folder__
```html
<img src="/static/logo.png" width="40" height="80">
```

## TODO
- [x] Make burger work on mobile as well
    - [x] need to know how to add JS to project
    - [x] write short JS to do the work
- [ ] Add pages to easily add players and trainings
- [ ] Check how to upgrade db
    - do test on local db
    - probably something like this (see https://flask-migrate.readthedocs.io/en/latest/#example):
        1. integrate with Flask-Migrate
        2. create initial migration
        3. upgrade ORM (with something trivial)
        4. create new migration
        5. commit to version controll
        6. add _"db upgrade"_ command when images start up?