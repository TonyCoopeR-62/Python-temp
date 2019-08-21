import os,  platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
                                os.getenv('HOMEPATH'), \
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
print('SAving in...', logging_file) 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)  
logging.debug('start programm')
logging.info('some do')
logging.warning('prog deleting')