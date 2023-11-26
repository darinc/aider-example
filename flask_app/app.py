from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return 'pong'

    @app.route('/fizzbuzz/<int:min>/<int:max>')
    def fizzbuzz(min, max):
        if min > max:
            return {'error': 'Invalid range: min must be less than or equal to max'}, 400
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
        return {'results': results}

    @app.route('/fibonacci/<int:max_val>')
    def fibonacci(max_val):
        sequence = [0, 1]
        while sequence[-1] + sequence[-2] <= max_val:
            sequence.append(sequence[-1] + sequence[-2])
        return {'sequence': sequence}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
