from flask import Flask, render_template, request
from idea_scrapper import get_site
import random

app = Flask(__name__)


@app.route("/")
def home():
    order_by = request.args.get("order_by")
    page_name = "INTERIOR"
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
        return render_template(
            "index.html", blogs=blogs, order_by=order_by, page=page_name
        )
    else:
        sites = [
            "betterhomes",
            "interiordesign",
            "idealhome",
            "homedesigning",
            "trendir",
            "homesandgardens",
        ]
        order_by = random.choice(sites)
        page_name = "INTERIOR"
        if order_by == "betterhomes":
            blogs = get_site("betterhomes")
        elif order_by == "interiordesign":
            blogs = get_site("interiordesign")
        elif order_by == "idealhome":
            blogs = get_site("idealhome")
        elif order_by == "trendir":
            blogs = get_site("trendir")
        elif order_by == "homesandgardens":
            blogs = get_site("homesandgardens")
        elif order_by == "homedesigning":
            blogs = get_site("homedesigning")
        else:
            blogs = []
        return render_template(
            "index.html", blogs=blogs, order_by=order_by, page=page_name
        )


@app.route("/unsplash")
def calendar():
    return render_template("unsplash.html")


app.run(host="0.0.0.0")
