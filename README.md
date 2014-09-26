Django v1.7 on OpenShift v3.2014
=
This git repository helps you get up and running quickly with django v1.7 and Openshift March 2014 release.
###Features
* Ready to use for local development
* Easy to push to Openshift
* Configured for PostgreSQL 9.2
* Minimal changes to default django 1.7 installation
* Names follow the django 1.7x tutorial
* Uses new folder layout from Openshift March 2014 release
* Allows for debug mode on Openshift with the help of an environment variable.

###How to use this repository
- Create an account at https://www.openshift.com
- Install the RHC client tools if you have not already done so.
```
sudo gem install rhc
rhc setup
```
- Create a Python 2.7 application
```
rhc app create django python-2.7
```
- Add the PostgreSQL 9.2 cartridge
```
rhc add-cartridge postgresql-9.2 --app django
```
- Add this upstream repo
```
cd django
git remote add upstream -m master https://github.com/jfmatth/openshift-django17.git
git pull -s recursive -X theirs upstream master
```
- Set the WSGI application to django's built in WSGI application.
```
rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=mysite/wsgi.py --app django
```
- Push the repo upstream
```
git push
```
- SSH into the application to create a django superuser
```
python app-root/repo/manage.py createsuperuser
```
- Now use your browser to connect to the Admin site.

### Running locally and the django tutorial
This repository was designed to allow you to quickly develop and deploy a website to Openshift.  For local development, make sure you have the following setup:

- Virtualenv for this instance of python / django.
- pip (should be installed with virtualenv)

Once you have those installed, install the requirements for this repository:
```
pip install -r requirements.txt
```

This will install django 1.7 on your local machine.

Once you have django installed, you can continue the tutorial from here https://docs.djangoproject.com/en/1.7/intro/tutorial01/#database-setup, although the default database and application configuration should be sufficient.

### Configuration details
When a git push is done, the .openshift/action_hooks/deploy is executed.  This script does two things:

1.  Runs python manage.py migrate to update any changes to the Schema
2.  Runs python manage.py collectstatic to move all necessary static files into /wsgi/static

#### Debugging mode and Openshift
By default, debug mode is off when pushed to Openshift.  However, if you'd like to turn on debugging (settings.DEBUG) while running on Openshift, you can set the environment variable DEBUG to True and then stop and start your application, and debugging will be turned on.

``` rhc env set DEBUG=True```

#### Notes on compatibility
This has not been tested thorougly with Python 3.  I'd love to have someone try that out for this repo.
