import random
import flask
app = flask.Flask(__name__)

@app.route('/createroom')
def home():
    user = flask.request.args['name']
    code = random.randint(0,9999)
    f1 = open(str(code) + ".txt", "w")
    f1.write("0")
    f1.close()
    return str(code)

@app.route('/joingame')
def joingame():
    user = flask.request.args['name']
    gameid = flask.request.args['id']
    f2r = open(gameid + ".txt", "r")
    f = f2r.read().split('|')
    f.append(user)
    fr = f2r.read()
    if fr.find("|Game Started|") != -1:
        return "error"
    pno = int(f[0])
    pno1 = pno + 1
    print(str(pno1))
    f2 = open(gameid +".txt", "w")
    f[0] =  pno1
    for t in f:
        f2.write(str(t))
        f2.write('|')
    f2.close()
    f2r.close()
    return "200"

@app.route('/startgame')
def startGame():
    gameid = flask.request.args['id']
    f69 = open(gameid + '.txt', 'a')
    f69.write('Game Started|')
    return ''

@app.route('/refresh')
def refresh():
    gameid = flask.request.args['id']
    f = open(gameid + ".txt","r")
    return f.read()

#@app.route('/gp.pdf')
def slide1():
    return flask.send_file('gp.pdf')

@app.route('/pdfs')
def answers():
    return flask.send_file('cheatpdf.html')

@app.route('/pdftest')
def test1():
    filepath = '/'
    return flask.send_file("periodic-table-8g2.pdf")
@app.route('/pdftest/download')
def download():
    return flask.send_file("periodic-table-8g2.pdf","file/pdf")
#@app.route('/list')
def hello_name():
    return flask.send_file("test.html") 

@app.route('/favicon.ico')
def favicon():
    return flask.send_file("favicon2.png", mimetype='image/gif')

@app.route('/test')
def appleIcon():
    return flask.send_file("sheesh.webarchive")


#@app.route('/apple-touch-icon-precomposed.png')
def applePreIcon():
    return flask.send_file("favicon2.png", mimetype='image/gif')

@app.route('/video')
def test():
    return flask.send_file("video.MP4")



if __name__ == '__main__':
           app.run(port=80)
