import pickle
import logging
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

# Configure simple logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Compute model path relative to this file: src/endpoint/main.py -> src/model/iris_model.pkl
# parents[0] = src/endpoint, parents[1] = src
model_path = Path(__file__).resolve().parents[1] / "model" / "iris_model.pkl"

# Defensive check with helpful error message if file missing (common in container context)
if not model_path.is_file():
    logger.error("Model file not found at expected path: %s", model_path)
    # list nearby files for debugging
    parent_dir = model_path.parent
    logger.error("Contents of %s: %s", parent_dir, list(parent_dir.iterdir()) if parent_dir.exists() else 'directory does not exist')
    raise FileNotFoundError(f"Model file not found at {model_path}. Make sure the file was copied into the container and the build context includes src/model/iris_model.pkl")

# Load the model once at startup
try:
    with model_path.open('rb') as f:
        model = pickle.load(f)
    logger.info("Model loaded successfully from %s", model_path)
except Exception as e:
    logger.exception("Failed to load model: %s", e)
    raise

app = FastAPI()

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Endpoint prediction
@app.post('/predict')
def predict_iris(data: IrisFeatures):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    logger.debug("Features for prediction: %s", features)

    pred = model.predict(features)[0]
    logger.debug("Prediction: %s", pred)

    return {'prediction': int(pred)}