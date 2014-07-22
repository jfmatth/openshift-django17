Django v1.65 on OpenShift v3.2014
=
This git repository helps you get up and running quickly with django v1.65 and Openshift March 2014 release.
###Features
* Ready to use for local development
* Easy to push to Openshift
* Configured for PostgreSQL 9.2
* Minimal changes to default django 1.6x installation
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
git remote add upstream -m master https://github.com/jfmatth/openshift-django16.git
git pull -s recursive -X theirs upstream master
```
- Push the repo upstream
```
git push
```
- SSH into the application to create a django superuser
```
python app-root/repo/manage.py createsuperuser
```

### Configuration details
When a git push is done, the .openshift/action_hooks/deploy is executed.  This script does two things:

1.  Runs python manage.py syncdb to update any changes to the Schema
2.  Runs python manage.py collectstatic to move all necessary static files into /wsgi/static

#### Debugging mode and Openshift
By default, debug mode is off when pushed to Openshift.  However, if you'd like to turn on debugging (settings.DEBUG) while running on Openshift, you can set the environment variable DEBUG to True and then stop and start your application, and debugging will be turned on.

``` rhc env set DEBUG=True```

