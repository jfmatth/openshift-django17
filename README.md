Django v1.7 (rc2) on OpenShift v3.2014
=
This git repository helps you get up and running quickly with django v1.7 and Openshift March 2014 release.
###Features
* Ready to use for local development
* Easy to push to Openshift
* Configured for PostgreSQL 9.2
* Minimal changes to default django 1.7 (rc2) installation
* Names follow the django 1.6x tutorial
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
- Add django 1.7 rc2 to the environment on Openshift, by ssh'ing into your gear and running the following (this is only required until django 1.7 is in the PIP repository.
```
pip install https://www.djangoproject.com/download/1.7c2/tarball/
```
- Push the repo upstream
```
git push
```
- SSH into the application to create a django superuser
```
python app-root/repo/manage.py createsuperuser
```
- Now user your browser to connect to the Admin site.

### Configuration details
When a git push is done, the .openshift/action_hooks/deploy is executed.  This script does two things:

1.  Runs python manage.py migrate to update any changes to the Schema
2.  Runs python manage.py collectstatic to move all necessary static files into /wsgi/static

#### Debugging mode and Openshift
By default, debug mode is off when pushed to Openshift.  However, if you'd like to turn on debugging (settings.DEBUG) while running on Openshift, you can set the environment variable DEBUG to True and then stop and start your application, and debugging will be turned on.

``` rhc env set DEBUG=True```

