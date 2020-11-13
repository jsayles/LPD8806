#!/bin/bash
tmux new-session -d -s webapp 'pipenv run webapp/server.py'
