import os
from pathlib import Path

class Config:
    
    # Base URL for the application under test
    # Can be overridden: export BASE_URL="https://www.amazon.com"
    BASE_URL = os.getenv("BASE_URL", "https://www.amazon.in")
    
    # Timeout values (in seconds)
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))
    
    # Project paths
    PROJECT_ROOT = Path(__file__).parent
    REPORTS_DIR = PROJECT_ROOT / "reports"
    TEST_DATA_DIR = PROJECT_ROOT / "TestData"