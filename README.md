


# Markdown Blog
Docker: ![Docker Image Size](https://img.shields.io/docker/image-size/ulimativ/markdown-blog) ![DockerPulls](https://img.shields.io/docker/pulls/ulimativ/markdown-blog)


This is a small and easy Flask setup for parsing markdown files as a webpage.
Depends on minimalist styling and flask configuration, basically reads out a folder of md files.

Currently running as development server

## Usage

Easily mountable as docker container, see docker-compose.yml

.env file configuration:

```
MARKDOWN_FOLDER="markdown_files/" # specify folder where you put markdown files
INDEX_FILE="welcome.md" # specfiy markdown file to serve as index page

BLOG_TITLE="The Small Markdown Blog" # specify title of the blog
HEADLINE="Welcome to The Small Markdown Blog" # specify welcome headline of the blog
```

### Docker Compose Example 

```

version: '3'

services:
  web:
    image: ulimativ/markdown-blog:latest
    network_mode: "host"
    ports:
      - '80:80'
    restart: unless-stopped
    volumes:
      - ./markdown_files:/app/markdown_files
```

## TO-DOs

* Table-of-Contents: ~~List all Markdown Files in given folder, including links~~
* ~~Move from development to production server~~
