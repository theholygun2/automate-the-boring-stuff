import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')


logging.debug('Some debugging details')
#Types of debugging based on level
logging.info('The logging module is working')
logging.warning('An error message is about to be logged.')
logging.error('An error has occured.')
logging.critical('The program is unable to recover!')

print('')
'''Disabling Logging'''

logging.debug('bitch')
logging.critical('Critical error! Critical error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')

'''Logging to a File'''
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')
