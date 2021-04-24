from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def connectivity():
    return render_template("untitled.html")
@app.route("/detail",methods=['GET','POST'])
def summision():
    if(request.method=='POST'):
        a=int(request.form['a'])
        b=int(request.form['b'])
        total=a+b
        return render_template('untitled.html',card=total)
if __name__=="__main__":
    app.run()
