from .base import * #noqa
from .base import env

# django will email these people thae details of exceptions raised in request or response cycle in production.
ADMINS = [("Alpha Saaras", "saaras.soft@gmail.com")]


# TODO: ADD domain name of the production server
CSRF_TRUSTED_ORIGINS = [""]