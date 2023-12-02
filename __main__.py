import os
import pathlib
from weasyprint import HTML, CSS

from convert import md_to_html


def app():
    path = pathlib.Path(__file__)
    md_path = os.path.join(path.parent.resolve(), 'resume.md')
    html_str = md_to_html(md_path)

    html = HTML(string=html_str)
    css = CSS(filename='./styles/pdf.css')
    html.write_pdf('./temp/resume.pdf', stylesheets=[css])


if __name__ == '__main__':
    app()