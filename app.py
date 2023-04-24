from flask import Flask, render_template,url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/algoritm", methods=['POST','GET'])
def algoritm():
    if request.method=="POST":
        name=request.form['name']
        kol=request.form['kol']
        from Algoritm import algoritm
        map=algoritm(name,kol)
        map.save("templates/map.html")
        return redirect("/rezult")
        #render_template("map.html")
        #return render_template("rezult.html",name=name,kol=kol,pr=pr,map=map)
    else:
        return render_template("algoritm.html")

@app.route("/rezult")
def rezult():
    return render_template("map.html")


if __name__=="__main__":
    app.run(debug=True)
