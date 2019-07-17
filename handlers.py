from anthill.framework.handlers import RequestHandler
from anthill.platform.handlers import UserHandlerMixin


class DiscoverHandler(RequestHandler, UserHandlerMixin):
    async def get(self, app_name, app_version):
        pass

