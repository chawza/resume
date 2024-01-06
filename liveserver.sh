source env/bin/activate

watchmedo \
    shell-command --patterns="styles/*.css;resume.md" \
    --recursive \
    --command='python app.py'
