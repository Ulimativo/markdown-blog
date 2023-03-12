
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white") />

![image] (https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

![image] ({https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue})

![image] ({https://img.shields.io/badge/Alpine_Linux-0D597F?style=for-the-badge&logo=alpine-linux&logoColor=white})

![image] ({https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white})


# Markdown Blog

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


## TO-DOs

* Table-of-Contents: ~~List all Markdown Files in given folder, including links~~
* ~~Move from development to production server~~
