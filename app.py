import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
	jsonStr = request.get_json()
	jsonObj = json.loads(jsonStr)
	lis=eval(jsonObj['t'])
	
	new=[] 
	for i in lis:
		if len(i)!=0:
			new.append(i)

	response="<b> "+str(new)+".</b><br>"
	return response
if __name__ == "__main__":
	app.run()

    
