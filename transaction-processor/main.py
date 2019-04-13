import sys
import argparse
import pkg_resources
import hashlib

from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_sdk.processor.log import init_console_logging
from sawtooth_sdk.processor.log import log_configuration
from sawtooth_sdk.processor.config import get_log_config
from sawtooth_sdk.processor.config import get_log_dir
from handler.handler import BankingTransaction

print("Entered ",__file__)
def main():
    processor = None
    print("Setting up handler")
    try:
        processor = TransactionProcessor(url='tcp://validator:4004')
        handler = BankingTransaction()
        processor.add_handler(handler)
        processor.start()

    except KeyboardInterrupt:
        pass
    except SystemExit as err:
        raise err
    except BaseException as err:
        print("Base exception error\n")
        print(err)
        sys.exit(1)
    finally:
        if processor is not None:
            processor.stop()

main()
