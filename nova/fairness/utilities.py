import libvirt

from nova import exception
from nova.i18n import _


def _lookup_by_name(self, instance_name):
    """Retrieve libvirt domain object given an instance name.

    All libvirt error handling should be handled in this method and
    relevant nova exceptions should be raised in response.

    """
    try:
        return self._conn.lookupByName(instance_name)
    except libvirt.libvirtError as ex:
        error_code = ex.get_error_code()
        if error_code == libvirt.VIR_ERR_NO_DOMAIN:
            raise exception.InstanceNotFound(instance_id=instance_name)

        msg = (_('Error from libvirt while looking up %(instance_name)s: '
                 '[Error Code %(error_code)s] %(ex)s') %
               {'instance_name': instance_name,
                'error_code': error_code,
                'ex': ex})
        raise exception.NovaException(msg)