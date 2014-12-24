Changelog for django 1.7 on Openshift
=
###Version 1.3.1 (12/24/2014 - Merry Christmas / Happy New Year)
* update settings.py to account for templates (Fixes #8), thanks to Bill K for this one.
* update README.md to reflect new instructions for above.

###Version 1.3 (11/6/2014)
* update settings.py to allow for either PostgreSQL or MySQL.
* started tagging releases in git.

###Version 1.2 (11/1/2014)
* Allow for static file distribution via /static folder and STATICFILES_DIR directive (thanks to just10minutes).

###Version 1.1
* Fix some Python 3.x compatibility bugs
* Optimize wsgi.py usage, use stock django wsgi.py file instead of manually created one.
* create requirements.txt for local usage, remove django 1.7x out of setup.py.

###Version 1.0
Intial release to github.
* Ready to use for local development.
* Easy to push to Openshift.
* Works with  PostgreSQL.
* Minimal changes to default django 1.7 installation.
* Names follow the django 1.7x tutorial.
* Uses new folder layout from Openshift March 2014 release.
* Allows for debug mode on Openshift with the help of an environment variable.
