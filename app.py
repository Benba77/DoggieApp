from flask import Flask, render_template, request, jsonify
import data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        if ('127.0.0' in request.host_url or 'localhost' in request.host_url):
            hostUrl = request.host_url
            baseUrl = 'http://127.0.0.1:5000/'
        else: 
            baseUrl = 'https://doggie-app2.azurewebsites.net/' #wird noch angepasst
        
        # print('\033[35m Die hostUrl lautet:  \033[0m', hostUrl)
        return render_template('index.html' , baseUrl=baseUrl, hostUrl=hostUrl)
    

    elif request.method=='POST':
        print(f'\033[32m {request.json} \033[0m')
        data.add_row(request.json)
        return 'ok.'

@app.route('/all-dogs/')
def all_dogs():
    all_dogs = data.get_all_dogs()
    return render_template('all-dogs.html', all_doggies=all_dogs)

@app.route('/<id_dog>/')
def getDog(id_dog):
    return data.get_dog_info(id_dog)

if __name__=='__main__':
    app.run(debug=True, port=5005)
