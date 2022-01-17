import logging as log
log.basicConfig(filename = 'events.log', level = log.ERROR)
def log_thisError(error):
    
    log.error(error)