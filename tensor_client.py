import json
import numpy as np
import requests

SERVER_URL = 'http://localhost:8501/v1/models/linear-model:predict'

def main():
    # Entradas para predecir
    predict_request = '{"instances" : [ [0.0], [1.0], [2.0], [3.0] ]}'

    total_time = 0
    num_requests = 10

    for _ in range(num_requests):
        response = requests.post(SERVER_URL, data=predict_request)
        response.raise_for_status()
        total_time += response.elapsed.total_seconds()
        prediction = response.json()
        print('Predictions:', prediction['predictions'])

    avg_latency_ms = (total_time * 1000) / num_requests
    print('Average latency: {:.2f} ms'.format(avg_latency_ms))

if __name__ == '__main__':
    main()
