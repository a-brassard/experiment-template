"""
Helper functions for experiment runs, such as logging configuration and other 
utilities.
"""

import logging
from pathlib import Path
from datetime import datetime


## Constants
LOG_DIR = Path("logs")


def get_exp_id() -> str:
    """
    Get the experiment ID for experiment runs. 
    Used to create unique log files for each experiment run.

    Format: run_{timestamp}

    To be changed to a meaningful name based on the experiment being run, 
    including important parameters of the experiment.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"run_{timestamp}"



def configure_logging() -> None:
    """Configure simple console and file logging for experiment runs."""
    log_dir = LOG_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{get_exp_id()}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_path),
        ],
    )
