#!/usr/local/bin/python
# -*- coding: utf8 -*-

import logging
import argparse
import time

from game import Game
from conf import conf
import log

def parse_args():
    parser = argparse.ArgumentParser(
        description="Run the server for the web-ui report",
        prog="server.py")
    parser.add_argument('--verbose', '-v', action="count",
                        help="Set verbosity level. Default display only ERROR \
messages, -v enable WARN and WARNING messages, -vv enable INFO messages, \
-vvv enable DEBUG messages, -vvvv enable TRACE messages", default=0)
    parser.add_argument('-q', '--quiet', action="store_true",
                        help="Remove ALL messages")
    return parser.parse_args()

def guess_time_unit(time_in_sec):
    unit = 's'
    res_time = time_in_sec
    if res_time > 60:
        unit = 'm'
        res_time /= 60
    if res_time > 60:
        unit = 'h'
        res_time /= 60
    if res_time > 24:
        unit = 'j'
        res_time /= 24
    return "%.5f%s" % (res_time, unit)


def main():
    ns = parse_args()
    log.init(verbose=ns.verbose, quiet=ns.quiet) 
    logging.info("Game is starting...");
    game = Game()
    try:
        game.run()
    except BaseException as e:
        logging.exception("An unexpected error occured during game run.")
        game.cleanUp()
    logging.info("Total game running time: %s" % guess_time_unit(
        time.time() - game.init_time))
    logging.info("Average rendering time: %.5fs" % 
        game.getAverageRenderingTime())
    logging.info("Average updating time: %.5fs" %
        game.getAverageUpdatingTime())
    logging.info("Average FPS: %.2f" % game.getAverageFPS())
    if game.getAverageUpdatingTime() > conf['game_engine']['update_time_step']:
        logging.warning("\tAverage updating time is too long!")
        logging.warning("\t Shoud be <= %.5f" 
                        % conf['game_engine']['update_time_step']);

if __name__ == "__main__":
    main()