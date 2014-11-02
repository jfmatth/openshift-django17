Put all static files / folders here.

They will run with runserver, and when you push to Openshift, collectstatic will copy all necessary static files to wsgi/static.

DO NOT PUT STATIC FILES IN wsgi/static, that isn't the right way to do it.

