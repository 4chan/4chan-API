'''
Created on Sep 9, 2012

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
'''
import logging
logging.basicConfig()

# Default logging level.  
DEFAULT_LOGGING_LEVEL = 1
#DEFAULT_LOGGING_LEVEL = logging.DEBUG
#DEFAULT_LOGGING_LEVEL = logging.INFO
#DEFAULT_LOGGING_LEVEL = logging.WARN
#DEFAULT_LOGGING_LEVEL = logging.ERROR

# Config file telling us what tests to run and what data to use with the tests
DEFAULT_CONFIG_FILE = 'test.conf.ini'
# Screen width, in chars
# Don't forget about the "INFO:Py4chan" width
DISPLAY_WIDTH = 150
# Test results
RESULTS_PASS = "PASS"
RESULTS_FAIL = "FAIL"

logger = logging.getLogger("Py4chan")
logger.setLevel(DEFAULT_LOGGING_LEVEL)
log = logger.log

from ConfigParser import SafeConfigParser
import re

def Thread_Main_Test(cfg, testName, testType):
    log(10, "Loading library")
    from Py4chan import Py4chanThread
    
    log(10, "Getting config")
    threadID = cfg.getint(testName, 'threadID')
    boardID = cfg.get(testName, 'boardID')
        
    log(10, "Creating thread object with ID=%r from board %r", threadID, boardID)
    t = Py4chanThread(boardID = boardID, threadID = threadID)
    log(10, "Created %r", t)
    
    return RESULTS_PASS


# Regexs used to match the section names to different tests
TEST_NAME_REGEXS = dict(
                        ThreadMain = dict(
                                          re = re.compile(r'^ThreadMain\-.*$'),
                                          func = Thread_Main_Test,
                                          ),
                        )

if __name__ == "__main__":
    log(20, "Initing")
    cfg = SafeConfigParser()
    results = {}
    
    log(20, "Loading config")
    cfg.read(DEFAULT_CONFIG_FILE)
    
    log(20, "Setting up logging")
    if not cfg.has_section('Global'):
        cfg.add_section('Global')
    if not cfg.has_option('Global', 'loggingLevel'):
        cfg.set('Global', 'loggingLevel', DEFAULT_LOGGING_LEVEL)
    logger.setLevel(cfg.getint('Global', 'loggingLevel'))
    
    log(20, "Begining tests")
    for testName in cfg.sections():
        log(10, "Looking at test %r", testName)
        for testType, info in TEST_NAME_REGEXS.items():
            if not results.has_key(testType):
                results[testType] = {}
            if info['re'].match(testName):
                log(20, "Trying test %r of type %r", testName, testType)
                try:
                    results[testType][testName] = info['func'](cfg = cfg, testName = testName, testType = testType)
                except Exception, e:
                    results[testType][testName] = e
                    logger.exception("Error %r in test %r of type %r" % (e, testName, testType))
        log(10, "Done with %r", testName)

    log(20, "All tests have completed")
        
    for testType, names in results.items():
        log(20, "-"*DISPLAY_WIDTH)
        log(20, testType.center(DISPLAY_WIDTH))
        log(20, "-"*DISPLAY_WIDTH)
        for testName, result in names.items():
            if isinstance(result, Exception):
                begin = testName.rjust(30) + ": " + RESULTS_FAIL
                log(20, begin + repr(result)[:DISPLAY_WIDTH - len(begin)])
            else:
                log(20, testName.rjust(30) + ": " + result)
        log(20, "-"*DISPLAY_WIDTH)
        log(20, " "*DISPLAY_WIDTH)
    
    log(20, "All Done")
    
