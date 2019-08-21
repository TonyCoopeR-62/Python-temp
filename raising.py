class ShortInputException(Exception):
    '''exception users'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('input something-->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
        # usually work
except EOFError:
    print('why EOF')
except ShortInputException as ex:
    print('ShortInputException: length of input - {0}; \
        except minimum {1}'.format(ex.length, ex.atleast))
else:
    print('no exceptions')