#!/usr/bin/python
import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'],'mysite'))

virtenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'],'virtenv')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

