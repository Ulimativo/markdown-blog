# Markdown Blog

This is a small and easy Flask setup for parsing markdown files as a webpage.
Depends on minimal styling and flask configuration, basically reads out a folder of md files.


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

