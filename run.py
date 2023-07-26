from portfolioApp import app


# SC=$(<sc.txt); export FLASK_DB=sqlite:///test.db; export FLASK_APP=run.py ; export FLASK_ENV=development ;flask run
#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    # app.run(debug=True)
    app.run()