import time
import logging
from flask import Flask

logging.basicConfig(level=logging.DEBUG)

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        start_time = time.time()
        response = 'pong'
        end_time = time.time()
        logging.debug(f"Ping endpoint took {end_time - start_time} seconds")
        return response

    @app.route('/fizzbuzz/<int:min>/<int:max>')
    def fizzbuzz(min, max):
        start_time = time.time()
        if min > max:
            response = {'error': 'Invalid range: min must be less than or equal to max'}, 400
        else:
            results = []
            for i in range(min, max + 1):
                if i % 3 == 0 and i % 5 == 0:
                    results.append('FizzBuzz')
                elif i % 3 == 0:
                    results.append('Fizz')
                elif i % 5 == 0:
                    results.append('Buzz')
                else:
                    results.append(str(i))
            response = {'results': results}
        end_time = time.time()
        logging.debug(f"FizzBuzz endpoint took {end_time - start_time} seconds")
        return response

    @app.route('/fibonacci/<int:max_val>')
    def fibonacci(max_val):
        start_time = time.time()
        sequence = [0, 1]
        while sequence[-1] + sequence[-2] <= max_val:
            sequence.append(sequence[-1] + sequence[-2])
        end_time = time.time()
        logging.debug(f"Fibonacci endpoint took {end_time - start_time} seconds")
        return {'sequence': sequence}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
