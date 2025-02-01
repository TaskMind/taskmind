source .venv/bin/activate
python3 -m pip freeze > requirements.txt
flask --app main run --debug
