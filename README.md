# TradeLoggerAPI

Development:

1. Set "DEBUG = False" to "DEBUG = True" in settings.py when starting Development
2. Whenever there were changes to the db schema, make migrations locally, push the migration file (e.g. migrations/0001_initial.py) to git before deployment.

Database Schema Issues on Heroku:
In order to make sure that the Heroku production postgresql database is up to date upon database model changes, make sure to:
1. Run "python manage.py makemigrations" followed by "python manage.py migrate" locally; this should update our development MySQL database
2. Commit the new migration file to Github master branch. 
3. Since the Procfile contains a line to run "python manage.py migrate", it should take care of migrating our changes to the production PostgreSQL db for us. However, if that fails for some reason, run "heroku run python manage.py migrate" in the Terminal from the application root. This SHOULD update the production db. 
4. Debugging tips: look into relevant Heroku CLI commands (check database tables, django_migrations table, etc)
