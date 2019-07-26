from anthill.platform.api.rest.handlers.detail import DetailMixin
from anthill.platform.api.rest.handlers.edit import (
    CreatingMixin, UpdatingMixin, DeletionMixin, ModelFormHandler)
from anthill.platform.api.rest.handlers.list import ListHandler
from environment.models import Application, ApplicationVersion, Environment


class ApplicationHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                         ModelFormHandler):
    """Multiple operations with applications."""
    slug_url_kwarg = 'name'
    slug_field = 'name'
    queryset = Application.query.filter_by(enabled=True)


class ApplicationListHandler(ListHandler):
    """Get list of applications."""
    queryset = Application.query.filter_by(enabled=True)


class ApplicationVersionHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                                ModelFormHandler):
    """Multiple operations with application versions."""
    slug_url_kwarg = 'version'
    slug_field = 'value'

    def get_queryset(self):
        queryset = ApplicationVersion.query.filter_by(enabled=True)
        queryset = queryset.filter_by(name=self.path_kwargs['name'])
        return queryset


class ApplicationVersionListHandler(ListHandler):
    """Get list of application versions."""
    def get_queryset(self):
        queryset = ApplicationVersion.query.filter_by(enabled=True)
        queryset = queryset.filter_by(name=self.path_kwargs['name'])
        return queryset


class EnvironmentHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                         ModelFormHandler):
    """Multiple operations with environments."""
    slug_url_kwarg = 'name'
    slug_field = 'name'
    queryset = Environment.query.filter_by(enabled=True)


class EnvironmentListHandler(ListHandler):
    """Get list of environments."""
    queryset = Environment.query.filter_by(enabled=True)
