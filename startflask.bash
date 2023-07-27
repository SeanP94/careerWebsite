#!/bin/bash
export SC=$(<sc.txt)
export FLASK_DB=sqlite:///test.db
export FLASK_APP=run.py
export FLASK_ENV=development
flask run