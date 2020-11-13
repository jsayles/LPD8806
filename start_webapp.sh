#!/bin/bash
tmux new-session -d -s webapp 'pipenv run flask run --host 0.0.0.0'
