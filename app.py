import os
import pathlib

import convert

from io import FileIO
from css_inline import inline


path = pathlib.Path(__file__)
module_path = path.parent.resolve()


def build_html_file(html):
    main_style_path = os.path.join(module_path, 'styles', 'pdf.css')
    web_extra = os.path.join(module_path, 'styles', 'web.css')

    css = open(main_style_path, 'r').read()
    css += open(web_extra, 'r').read()

    compiled = html + '<style>' + css + '</style>'

    file = FileIO(os.path.join(module_path, 'temp', 'resume.html'), mode='w')
    file.write(compiled.encode())
    return file

def build_pdf_file(html):
    pdf_bytes = convert.html_to_pdf(html_str=html)

    file = FileIO(os.path.join(module_path, 'temp', 'resume.pdf'), mode='wb')
    file.write(pdf_bytes)
    return file

def app():
    md_path = os.path.join(module_path, 'resume.md')
    html_str = convert.md_to_html(filepath=md_path)

    html = build_html_file(html_str)
    pdf = build_pdf_file(html_str)

    print("HTML File saved in ", html.name)
    print("PDF File saved in ", pdf.name)


if __name__ == '__main__':
    app()