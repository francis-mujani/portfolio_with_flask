from flask import Flask, render_template
import netifaces
import platform
app = Flask(__name__)

# route 
@app.route('/')
def index():
    message = 'bonjour'

    # affichage
    return render_template('index.html', title='home', message=message)


# create port
port = 8000
# print(f'server est lancé sur le port {port}')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port= port, debug=True)