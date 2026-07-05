import os
import logging
from datetime import datetime

# Create Logs Folder
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log File Name
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Complete Log File Path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logger Configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)