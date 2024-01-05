import os
import pathlib
from css_inline import inline

import convert

path = pathlib.Path(__file__)
module_path = path.parent.resolve()


def build_html_file(html):
    main_style_path = os.path.join(module_path, 'styles', 'pdf.css')
    web_extra = os.path.join(module_path, 'styles', 'web.css')

    css = open(main_style_path, 'r').read()
    css += open(web_extra, 'r').read()

    compiled = inline(html, extra_css=css)

    with open(os.path.join(module_path, 'temp', 'resume.html'), 'w') as file:
        file.write(compiled)
        print("HTML resume saved in: ", file.name)

def build_pdf_file(html):
    pdf_bytes = convert.html_to_pdf(html_str=html)

    with open(os.path.join(module_path, 'temp', 'resume.pdf'), 'wb') as file:
        file.write(pdf_bytes)
        print("PDF resume saved in: ", file.name)


def app():
    md_path = os.path.join(module_path, 'resume.md')
    html = convert.md_to_html(filepath=md_path)

    build_html_file(html)
    build_pdf_file(html)


if __name__ == '__main__':
    app()