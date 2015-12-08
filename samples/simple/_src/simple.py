import logging

LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)


def handler(event, context):
    LOG.debug(event)
    return {'status': 'success'}
