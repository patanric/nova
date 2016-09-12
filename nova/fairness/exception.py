from nova.exception import NovaException
from nova.i18n import _


class ServiceGroupUnavailable(NovaException):
    msg_fmt = _("The service from servicegroup driver %(driver)s is "
                "temporarily unavailable.")