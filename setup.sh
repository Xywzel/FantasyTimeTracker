#!/bin/zsh

python3 -m venv venv

source venv/bin/activate

pip install flask
pip install flask_wtf
pip install flask_pagedown
pip install markdown
pip install wtforms
pip install mdx_truly_sane_lists

deactivate
