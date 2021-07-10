#!/bin/sh

source flaskr/venv/scripts/activate

export FLASK_APP=flaskr
export FLASK_ENV=devolopment
export FLASK_DEBUG=true

flask run