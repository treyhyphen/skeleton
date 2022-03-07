# Flask Skeleton

Just a skeleton Flask app that has a barebones API, frontend, and db (SQLite in this case, but easily modified to anything else)

_* *NOTE for NGINX:*_
By default, proxypass will not set `X-Forwarded-For-*` headers. You need to configure with:
```
server {
    # ...
    location /  {
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Server $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;        
        proxy_pass http://127.0.0.1:5000;
    }
}
```

Source: https://www.nginx.com/resources/wiki/start/topics/examples/likeapache/

## `.env`

Control various Flask/SQLAlchemy ENV variables.

Also loads up any variable named FLASK_G_* as a global Flask `g` object. See templates/wrapper.html for how most of these get used.

## `applicaiton/frontend.py`

Just the front-end controller

## `application/modules/`

This is empty, but ideally separate out more complex code for routes in here.

## `application/static/`

Just static content. Lot of empty files in here as a reminder (to me) to build out each of these for each new application. All the files in here are placeholders that will get used in HTML meta tags and stuff for the site (like favicons and social previews).

## `application/templates/`

Duh

## Other notes/reminders

* For zappa AWS Lambda apps, don't forget to update requirements.txt to add zappa

