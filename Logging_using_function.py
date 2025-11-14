
# Main function to get logging

def configure_logging() -> None:
    """Attach console and file handlers with shared formatting."""
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler("migration_local.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Avoid duplicating handlers across repeated CLI invocations.
    if not root_logger.handlers:
        root_logger.addHandler(stream_handler)
        root_logger.addHandler(file_handler)


configure_logging()
# above is logging configuration
# when you run intilize a logger, it takes above configuration, below is intilize which should be written in every file
logger = logging.getLogger(__name__)


# Different logging methods
logger.debug("Connecting to database with params: %s", db_params)
logger.info("Target environment: %s", target_url)
logger.warning("Disk space running low: %s remaining", disk_usage)
logger.error("TARGET_API_TOKEN not found in .env file")

# logging levels
# debug - info - warning - error - critical

