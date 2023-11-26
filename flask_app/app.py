from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return 'pong'

    @app.route('/fizzbuzz')
    def fizzbuzz():
        results = []
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return {'results': results}

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
