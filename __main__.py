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

    with open(os.path.join(module_path, 'temp', 'resumt-html.html'), 'w') as file:
        file.write(compiled)


def app():
    md_path = os.path.join(module_path, 'resume.md')
    html = convert.md_to_html(md_path)

    build_html_file(html)
    convert.html_to_pdf(html)


if __name__ == '__main__':
    app()