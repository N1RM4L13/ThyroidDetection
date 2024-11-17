
# Thyroid Detection

## Problem Statement
This project aims to build a classification model to predict thyroid types, specifically identifying hypothyroid or hyperthyroid conditions, using the provided training dataset. The goal is to develop a reliable methodology to support accurate diagnosis and effective disorder management.

## Sections
1. [Dataset Description](dataset/README.md)
2. [Training Workflow](training/README.md)
3. [Prediction Workflow](prediction/README.md)

## Application Flow
<img src="assets\FlowDiagram.png" alt="Thyroid Classification Overview" width="500" height="500">

## Run Locally

1. Clone the project
```bash
  git clone https://github.com/N1RM4L13/ThyroidDetection.git
```

2. Install dependencies
```bash
  pip install -r requirements.txt
```

3. Start the Service

```bash
  python main.py
```

4. The API will start running on http://127.0.0.1:5000 by default (or any specified port in your configuration).

5. You can test the API using tools like Postman or cURL.

To test the API, use the following cURL command with JSON input:
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"folderPath":"Prediction_Batch_Files"}'
```
Alternatively, if you prefer to use localhost instead of the IP address, you can replace http://127.0.0.1:5000 with http://localhost:5000 in the cURL command.


## Usecase

The model can be utilized by hospitals as a first level of scrutinization. Initially, the model predicts whether a person is suffering from thyroid-related conditions, such as hypothyroidism or hyperthyroidism. If the prediction is positive, the treatment process is fast-tracked, ensuring doctors address the case with priority. For negative predictions, the patient’s file is reviewed by a junior doctor to verify the model's accuracy. While the model is designed for high accuracy, human oversight is crucial in medical cases. If the junior doctor concurs with the model’s negative prediction, the patient is released. However, if the junior doctor identifies inconsistencies, the case is escalated to a senior doctor for further evaluation and treatment. This workflow ensures efficient use of resources while maintaining the reliability and safety of medical care.

---


