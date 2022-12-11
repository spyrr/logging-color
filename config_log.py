import logging
import logging.config
import json


with open('config.json', 'r') as f:
    conf = json.load(f)
logging.config.dictConfig(conf)


l = logging.getLogger(__name__)
l2 = logging.getLogger('Release')

l.debug('l.debug')
l.info('l.info')
l.error('l.error')
l.warning('l.warning')
l.critical('l.critical')

l2.debug('l2.debug')
l2.info('l2.info')
l2.error('l2.error')
l2.warning('l2.warning')
l2.critical('l2.critical')