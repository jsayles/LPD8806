#!/bin/bash
tmux new-session -d -s webapp 'pipenv run start_webapp'
