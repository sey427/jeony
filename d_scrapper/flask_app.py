from flask import Flask, render_template, request
from scrapper import get_site
import random

app = Flask(__name__)


@app.route("/")
def home():
    order_by = request.args.get("order_by")
    if order_by:
        if order_by == "happydesign":
            blogs = get_site("happydesign")
        elif order_by == "maison":
            blogs = get_site("maison")
        elif order_by == "livingsense":
            blogs = get_site("livingsense")
        elif order_by == "inhouse":
            blogs = get_site("inhouse")
        elif order_by == "ohouse":
            blogs = get_site("ohouse")
        else:
            blogs = []
        return render_template("index.html", blogs=blogs, order_by=order_by)
    else:
        sites = [
            "betterhomes",
            "interiordesign",
            "idealhome",
            "homedesigning",
            "trendir",
            "elledecor",
            "homesandgardens",
        ]
        order_by = random.choice(sites)
        if order_by == "betterhomes":
            blogs = get_site("betterhomes")
        elif order_by == "interiordesign":
            blogs = get_site("interiordesign")
        elif order_by == "idealhome":
            blogs = get_site("idealhome")
        elif order_by == "trendir":
            blogs = get_site("trendir")
        elif order_by == "elledecor":
            blogs = get_site("elledecor")
        elif order_by == "homesandgardens":
            blogs = get_site("homesandgardens")
        elif order_by == "homedesigning":
            blogs = get_site("homedesigning")
        else:
            blogs = []
        return render_template("index.html", blogs=blogs, order_by=order_by)


if __name__ == "__main__":
    app.run(debug=True)