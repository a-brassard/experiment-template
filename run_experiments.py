"""
Main entry point to run all experiments in the project. 
"""

import logging

from src.utils import configure_logging
from src.experiment1 import run_experiment1
from src.experiment2 import run_experiment2

logger = logging.getLogger(__name__)


def main():
    """ Main function to run all experiments. """
    configure_logging()
    logger.info("Running experiments...")

    run_experiment1()
    run_experiment2()

    logger.info("All experiments completed.")


if __name__ == "__main__":
    main()
