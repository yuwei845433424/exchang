from flask import Flask
from flask import session,redirect,url_for,request,render_template
from werkzeug import secure_filename
import os
from Resource import Resource

app = Flask(__name__)
UPLOAD_FOLDER = 'web_test/static/images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/index')
def hello_world():
	username = "yuwei"
	if 'username' in session and session['username'] == username:
		return render_template('index.html',name=username)
	return render_template('index.html')

#organize data 
def getData(resource):
	dataobj = open("web_test/static/js/data.json","r")
	datastr = ""
	datalist = []
	for line in dataobj:
		datalist.append(line)
	dataobj.close()
	datastr = "".join(datalist)
	begin = datastr.index("[")
	newData = datastr[:begin+1]+resource.toJsonStr()+","+datastr[begin+1:]
	dataWrite = open("web_test/static/js/data.json","w")
	dataWrite.write(newData)
	dataWrite.flush() 
	dataWrite.close()

@app.route('/logo.png')
def favicon():
    return redirect(url_for('static', filename='logo.png'), code=301)

@app.route('/login',methods = ['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username == "yuwei" and password =="123456":
		session['username'] = username
		return render_template('index.html',name=username)
	return render_template('data.html',result="error")



@app.route('/upload', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		title = request.form['things']
		will = request.form['will']
		contact = request.form['contact']
		imgfile = request.files['files']
		try:
			if imgfile and allowed_file(imgfile.filename):
				filename = secure_filename(imgfile.filename)
				imgfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				url = "static/images/"+filename
				resource = Resource(url,title,will,1)
				getData(resource)
				return redirect('index')
		except Exception:
			return render_template("error.html")

@app.route('/logout')
def logout():
	#how to use url_for
	session.pop('username', None)
	return redirect("index")   

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run()

