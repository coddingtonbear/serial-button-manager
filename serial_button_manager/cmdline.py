from argparse import ArgumentParser
import logging
import sys

from .manager import SerialButtonManager


logger = logging.getLogger(__name__)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = ArgumentParser()
    parser.add_argument('serial_device', nargs=1)
    parser.add_argument('service_name', nargs=1)
    parser.add_argument('--loglevel', default='DEBUG')

    options = parser.parse_args(args)

    logger.basicConfig(level=logging.getLevelName(options.loglevel))

    manager = SerialButtonManager(options.serial_device, options.service_name)
    manager.run()
