#!/bin/bash
tmux new-session -d -s webapp 'python3 webapp/server.py'
