#!python3
from flask import Flask, request, render_template
app= Flask(__name__)

@app.route('/',methods=['POST','GET'])
def rootpage():
    name=''
    height=''
    weight=''
    bmi=''
    if request.method == 'POST' and 'username' in request.form:
        name=request.form.get('username')
        height=request.form.get('height')
        weight=request.form.get('weight')
        bmi=round(int(weight)/int(height),2)
        
    return render_template('index.html',name=name, weight=weight,height=height,bmi=bmi )
app.run()
#serve(app, host='0.0.0.0', port=8080, threads=1)
