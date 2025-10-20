#!/bin/bash
cd ~/microblog
source venv/bin/activate
export FLASK_APP=microblog.py
flask run

