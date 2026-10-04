from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
SRC_DIR = BASE_DIR / "src"
APP_DIR = BASE_DIR / "app"
API_DIR = BASE_DIR / "api"

IMAGE_SIZE = (224, 224)

BATCH_SIZE = 32

RANDOM_SEED = 42