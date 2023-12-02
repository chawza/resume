import subprocess


def md_to_html(filepath):
    command = f'pandoc --from gfm -t html {filepath}'
    result = subprocess.run(command.split(' '), capture_output=True)
    return result.stdout
    