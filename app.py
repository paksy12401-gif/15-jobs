# from flask import Flask,render_template,request, send_file  #requests 랑은 다름 
# from test2 import search_a
# from file import save_to_csv

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template("index.html")

# @app.route("/search")
# def search():
#     keyword = request.args.get("keyword")
#     # print(keyword)
#     jobs = search_a(keyword,1)
    
#     return render_template("search.html",jobs=enumerate(jobs),keyword = keyword)

# # @app.route("/file")
# # def file():
# #     keywords = request.args.get("keyword")
# #     jobs = search_incruit(keywords,1)
# #     save_to_csv(jobs)
# #     print(keywords)
# #     return send_file("downloads.csv",as_attachment=True)
# @app.route("/file")
# def yy():
#     keywords = request.args.get("keyword")
#     jobs = search_a(keywords,1)
#     save_to_csv(jobs)
#     print(keywords)
#     return send_file("downloads.csv",as_attachment=True)

   
# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask
# from flask import render_template
# from flask import request
# from flask import send_file

# from test2 import search_a
# from file import save_to_csv
# from ranking import ranking_products


# app = Flask(__name__)


# # ==============================
# # 메인 페이지
# # ==============================

# @app.route("/")
# def home():

#     return render_template(
#         "index.html"
#     )


# # ==============================
# # 검색 결과 페이지
# # ==============================

# @app.route("/search")
# def search():

#     keyword = request.args.get(
#         "keyword"
#     )

#     products = search_a(
#         keyword,
#         1
#     )

#     return render_template(

#         "search.html",

#         products=enumerate(products),

#         keyword=keyword
#     )


# # ==============================
# # CSV 다운로드
# # ==============================

# from flask import Flask, render_template, request
# from test2 import search_a
# from ranking import ranking_products

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/search")
# def search():

#     keyword = request.args.get("keyword")

#     products = search_a(keyword, 1)

#     products = ranking_products(products)

#     return render_template(
#         "search.html",
#         products=products,
#         keyword=keyword
#     )


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
from test2 import search_a

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/search")
def search():

    keyword = request.args.get("keyword")

    jobs = search_a(keyword, 1)

    return render_template(
        "search.html",
        products=jobs,
        keyword=keyword
    )


if __name__ == '__main__':
    app.run(debug=True)