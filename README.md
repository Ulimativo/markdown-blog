[![Netlify Status](https://api.netlify.com/api/v1/badges/4bbd2467-c1eb-4d45-a4a0-978b89db005c/deploy-status)](https://app.netlify.com/sites/whimsical-horse-945829/deploys)

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
* Move from development to production server
