from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/leafy')
def leafy():
    leafs = ['Boston Lettuce', 'Iceberg Lettuce', 'Leaf Lettuce', 'Romaine', 'Arugula', 'Dandelion', 'Spinach', 'Chard']
    vegetables = ['Apples', 'Avocado', 'Bell pepper', 'Celery', 'Carrot',\
              'Cucumber', 'Mushrooms', 'Onion', 'Pear', 'Radishes',\
              'Snap Peas', 'Snow Peas', 'Summer Squash', 'Tomato']
    protein = ['Ham', 'Chicken', 'Egg', 'Tofu', 'None']
    starch = ['Chickpeas', 'White Beans', 'Quinoa', 'Farro']
    
    leaf = random.choice(leafs)
    veg_1 = random.choice(vegetables)
    veg_2 = random.choice(vegetables)
    while veg_2 == veg_1:
        veg_2 = random.choice(vegetables)
    pro = random.choice(protein)
    sta = random.choice(starch)
    
    salad_list = [leaf, veg_1, veg_2, pro, sta]
    
    return render_template("leafy.html", salad=salad_list)

if __name__ == "__main__":
    app.run(debug=True)