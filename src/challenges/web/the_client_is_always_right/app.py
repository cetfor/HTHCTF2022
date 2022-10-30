from flask import Flask, make_response, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def root():
    admin = request.cookies.get('admin')
    resp = make_response(render_template('check.html', admin=admin))
    if not admin:
        resp.set_cookie('admin', 'false')
    return resp

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7502)
