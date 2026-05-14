TARGET = {

    "shoulder": 55,

    "chest": 58,

    "length": 70
}


# =========================================
# 점수 계산
# =========================================

def ranking_products(products):

    TARGET = {
        "shoulder": 52,
        "chest": 58,
        "length": 68
    }

    def score(p):

        s = 100

        s -= abs(p["shoulder"] - TARGET["shoulder"]) * 3
        s -= abs(p["chest"] - TARGET["chest"]) * 2
        s -= abs(p["length"] - TARGET["length"]) * 2

        return round(s, 1)

    for p in products:
        p["score"] = score(p)

    products = sorted(products, key=lambda x: x["score"], reverse=True)

    for i, p in enumerate(products):
        p["rank"] = i + 1

    return products