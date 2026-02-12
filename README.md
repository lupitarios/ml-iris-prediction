# ml-iris-api-integration

I have been interested in Machine Learning for some time, particularly in understanding how trained models are integrated into real-world backend systems. This project simulates a production-like environment where a pre-trained toy model (Iris dataset classifier) is deployed as a RESTful API using FastAPI.

The objective was not to build a complex model, but to focus on the end-to-end integration process: wrapping a trained ML model inside an API endpoint, handling request/response validation, and containerizing the application with Docker for consistent deployment.

This project demonstrates:
*Exposing a trained ML model through a FastAPI endpoint
*Input validation and structured API responses
*Separation between model logic and API layer
*Docker-based containerization for reproducible environments
*A production-oriented mindset for ML deployment

The goal was to bridge the gap between machine learning experimentation and backend production integration.

## Tech Stack
- Python
- FastAPI
- Scikit-learn
- Numpy
- Docker

## Project Structure
```
 ml-iris-prediction/ 
  ---k8s/ 
  ---src/
      ----/endpoint/ 
                  main.py
      ----/model/ 
  ---.gitignore
  ---Dockerfile
  ---README.md
  ---requirements.txt
 ```

## Installation
### Clone the repository
 ```
 git clone [https://github.com/lupitarios/mediapipe-intro-ln.git](https://github.com/lupitarios/ml-iris-prediction.git)
 cd ml-iris-prediction
 ```
 ### Install dependencies
 ```
 pip install -r requirements.txt
 ```
### Execution
Build Docker Inage
```
docker build -t iris-predictor-integration .
```
Run the container:
```
docker run -d -p 8000:8000 iris-predictor-integration
```
## Preview Excution
Container running:
<img width="1053" height="120" alt="image" src="https://github.com/user-attachments/assets/7d433ca1-dcc4-4289-904f-7f27bfd397f2" />

Endpoint running from Postman
<img width="1313" height="642" alt="image" src="https://github.com/user-attachments/assets/c3ee01ae-2cc9-4a56-9311-d96444419500" />

