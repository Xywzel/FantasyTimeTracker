from flask import render_template, send_file
from markdown.extensions.wikilinks import WikiLinkExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension
import markdown

import os

from server.file import File

def get_index():
    path = os.path.join(os.getcwd(), "data", "files")
    root = File(path)
    return render_template('index.html', root=root)

def get_markdown(filename):
    text = "Missing markdown file"
    path = os.path.join(os.getcwd(), "data", "files", filename)
    with open(path, "r", encoding="utf8") as f:
        text = f.read()
    md = markdown.Markdown(extensions=['toc', 'wikilinks', 'tables', 'mdx_truly_sane_lists'],
            extension_configs={'mdx_truly_sane_lists': {
                'nested_indent':2,
                'truly_sane':True}})
    html = md.convert(text)
    return render_template('markdown.html', title=filename, content=html, toc=md.toc, path=filename)
