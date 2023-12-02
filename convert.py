import subprocess

from weasyprint import HTML, CSS


def md_to_html(filepath):
    command = f'pandoc --from gfm -t html {filepath}'
    result = subprocess.run(command.split(' '), capture_output=True)
    html = result.stdout.decode()
    return f"<body>{html}</body>"


def html_to_pdf(html_str):
    html = HTML(string=html_str)
    css = CSS(filename='./styles/pdf.css')
    html.write_pdf('./temp/resume.pdf', stylesheets=[css])
    