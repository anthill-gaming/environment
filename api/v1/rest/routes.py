# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from . import handlers as h


route_patterns = [
    url(r'^/application/(?P<name>[^/]+)/?$', h.ApplicationHandler, name='app'),
    url(r'^/application/?$', h.ApplicationHandler, name='app_create'),
    url(r'^/applications/?$', h.ApplicationListHandler, name='apps'),

    url(r'^/application/(?P<name>[^/]+)/version/?$', h.ApplicationVersionHandler, name='app_version_create'),
    url(r'^/application/(?P<name>[^/]+)/versions/?$', h.ApplicationVersionListHandler, name='app_versions'),
    url(r'^/application/(?P<name>[^/]+)/(?P<version>[^/]+)/?$', h.ApplicationVersionHandler, name='app_version'),

    url(r'^/environment/(?P<name>[^/]+)/?$', h.EnvironmentHandler, name='environment'),
    url(r'^/environment/?$', h.EnvironmentHandler, name='environment_create'),
    url(r'^/environments/?$', h.EnvironmentListHandler, name='environments'),
]
