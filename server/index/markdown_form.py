from flask import render_template, send_file
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.wikilinks import WikiLinkExtension
from wtforms.fields import SubmitField

import markdown
import os

class MarkdownForm(FlaskForm):
    pagedown = PageDownField("File")
    submit = SubmitField('Save')

    def render(self, filename):
        path = os.path.join(os.getcwd(), "data", "files", filename)
        with open(path, 'r', encoding="utf8", newline='\n') as f:
            text = f.read()
        self.pagedown.data = text
        return render_template('mdedit.html', form=self, data=text, filename=filename)

    def save(self, filename):
        text = self.pagedown.data
        path = os.path.join(os.getcwd(), "data", "files", filename)
        print("Would save to", path)
        print("Text:", text)
        with open(path, 'w', encoding="utf8", newline='\n') as f:
            f.write(text)
        md = markdown.Markdown(extensions=['toc', 'wikilinks', 'tables', 'attr_list'])
        html = md.convert(text)
        return render_template('markdown.html', content=html, toc=md.toc, path=filename)
