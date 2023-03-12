from flask import Flask, render_template
import markdown
import markdown.extensions.fenced_code

import os

app = Flask(__name__)

def read_file(md_file=None):
    if (md_file is None):
        md_file='index.md'
    md_file=open(f'files/{md_file}', 'r', encoding='UTF-8')
    md_string = markdown.markdown(
        md_file.read(), extensions=['fenced_code']
    )
    return md_string

def gen_toc():
    md_files=os.listdir('files/')
    toc=[]
    for file in md_files:
        toc.append(file)
    return toc

@app.route("/<md_file>")
@app.route("/")
def index(md_file=None):
 
    md_string=read_file(md_file)

    content= {
        'toc': gen_toc(),
        'md_string':md_string
    }
    return render_template('base.html', content=content)

if __name__ == "__main__":
    app.run()