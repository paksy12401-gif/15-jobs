from flask import Flask,render_template,request, send_file  #requests 랑은 다름 
from scrapper import search_incruit
from file import save_to_csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # print(keyword)
    jobs = search_incruit(keyword,1)
    
    return render_template("search.html",jobs=enumerate(jobs),keyword = keyword)

@app.route("/file")
def file():
    keywords = request.args.get("keyword")
    jobs = search_incruit(keywords,1)
    save_to_csv(jobs)
    print(keywords)
    return send_file("downloads.csv",as_attachment=True)

   
if __name__ == '__main__':
    app.run(debug=True)




