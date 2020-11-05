# Scrapy-Wsgi
This service is designed for use as a wsgi application in docker container with scrapy and tornado.

To start the service:
    
    docker-compose up --build

You can access the server

    0.0.0.0:8080

Sample requeest body

    {
        "urls": "google.com,reddit.com,imdb.com",
        "redirect_enabled": True
        "elements": {
                        "html": "//html/text()"
                        ...
                    }
    }

