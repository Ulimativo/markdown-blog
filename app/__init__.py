from flask import Flask, render_template
import os
import markdown
import markdown.extensions.fenced_code
from dotenv import dotenv_values
config=dotenv_values(".env") 
BLOG_TITLE=config['BLOG_TITLE']
HEADLINE=config['HEADLINE']
MARKDOWN_FOLDER=config['MARKDOWN_FOLDER']
INDEX_FILE=config['INDEX_FILE']


app = Flask(__name__)

def read_file(md_file=None):
    if (md_file is None):
        md_file=INDEX_FILE
    md_file=open(MARKDOWN_FOLDER+md_file, 'r', encoding='UTF-8')
    md_string = markdown.markdown(
        md_file.read(), extensions=['fenced_code']
    )
    return md_string

def gen_toc():
    md_files=os.listdir(MARKDOWN_FOLDER)
    toc=[]
    for file in md_files:
        toc.append(file)
    return toc

@app.route("/<md_file>")
@app.route("/")
def index(md_file=INDEX_FILE):
    content= {
        'blog_title': BLOG_TITLE,
        'headline': HEADLINE,
        'toc': gen_toc(),
        'md_string':read_file(md_file)
    }
    return render_template('base.html', content=content)

if __name__ == "__main__":
    app.run()