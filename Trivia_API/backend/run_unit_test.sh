#!/bin/sh

source flaskr/venv/scripts/activate
py test_flaskr.py

$SHELL #source: https://askubuntu.com/questions/20330/how-to-run-a-script-without-closing-the-terminal