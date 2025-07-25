from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
cart = []

menu = [
    # Veg
    {"id": 1, "name": "Paneer Tikka", "price": 150, "image": "paneer.jpg", "desc": "Grilled paneer skewers", "category": "Veg"},
    {"id": 2, "name": "Veg Biryani", "price": 120, "image": "vegbiryani.jpg", "desc": "Aromatic rice with vegetables", "category": "Veg"},
    {"id": 3, "name": "Aloo Paratha", "price": 70, "image": "paratha.jpg", "desc": "Stuffed potato flatbread", "category": "Veg"},
    {"id": 4, "name": "Masala Dosa", "price": 90, "image": "masaladosa.jpg", "desc": "Crispy dosa with potato masala", "category": "Veg"},
    {"id": 5, "name": "mushroom briyani", "price": 100, "image": "mushroom.jpg", "desc": "Aromatic rice with mushroom", "category": "Veg"},
    {"id": 6, "name": "Veg Manchurian", "price": 130, "image": "manchurian.jpg", "desc": "Fried veggie balls in sauce", "category": "Veg"},
    {"id": 7, "name": "Fried Rice", "price": 90, "image": "fried.jpg", "desc": "Spiced rice with veggies", "category": "Veg"},
    {"id": 8, "name": "Spring Rolls", "price": 80, "image": "rolls.jpg", "desc": "Veg-stuffed crispy rolls", "category": "Veg"},

    # Non-Veg
    {"id": 9, "name": "Chicken Biryani", "price": 180, "image": "chicken.jpg", "desc": "Fragrant rice with chicken", "category": "Non-Veg"},
    {"id": 10, "name": "Butter Chicken", "price": 200, "image": "butter.jpg", "desc": "Creamy tomato chicken curry", "category": "Non-Veg"},
    {"id": 11, "name": "Chicken Lollipop", "price": 160, "image": "lollipop.jpg", "desc": "Fried chicken drumsticks", "category": "Non-Veg"},
    {"id": 12, "name": "Egg Fried Rice", "price": 110, "image": "egg.jpg", "desc": "Fried rice with egg bits", "category": "Non-Veg"},
    {"id": 13, "name": "Fish Fry", "price": 170, "image": "fish.jpg", "desc": "Spicy fried fish fillets", "category": "Non-Veg"},
    {"id": 14, "name": "Mutton Curry", "price": 220, "image": "mutton.jpg", "desc": "Slow-cooked mutton curry", "category": "Non-Veg"},
    {"id": 15, "name": "Prawn Masala", "price": 190, "image": "prawns.jpg", "desc": "Tangy prawn curry", "category": "Non-Veg"},
    {"id": 16, "name": "Tandoori Chicken", "price": 180, "image": "tandoori.jpg", "desc": "Char-grilled chicken", "category": "Non-Veg"},
    {"id": 17, "name": "Grill Chicken", "price": 200, "image": "grill.jpg", "desc": "spicy grilled chicken", "category": "Non-Veg"},
    {"id": 18, "name": "Mutton Thokku", "price": 180, "image": "thokku.jpg", "desc": "Char-grilled chicken", "category": "Non-Veg"},
    {"id": 19, "name": "Japan Chicken", "price": 250, "image": "japan.jpg", "desc": "japan realistics chicken with white sweet sauce ", "category": "Non-Veg"},
    {"id": 20, "name": "Pallipalayam Chicken", "price": 200, "image": "palli.jpg", "desc": "pallipalaym special chicken and spicy", "category": "Non-Veg"},
    {"id": 21, "name": "Pepper Chicken", "price": 150, "image": "pepper.jpg", "desc": "pepper flavour chicken", "category": "Non-Veg"},

    # Drinks
    {"id": 22, "name": "Cold Coffee", "price": 60, "image": "coffee.jpg", "desc": "Chilled coffee drink", "category": "Drinks"},
    {"id": 23, "name": "Lassi", "price": 50, "image": "lassi.jpg", "desc": "Sweet curd-based drink", "category": "Drinks"},
    {"id": 24, "name": "Lemon Soda", "price": 30, "image": "lemon.jpg", "desc": "Sour fizzy drink", "category": "Drinks"},
    {"id": 25, "name": "Mango Juice", "price": 40, "image": "mango.jpg", "desc": "Fresh mango juice", "category": "Drinks"},
    {"id": 26, "name": "Buttermilk", "price": 25, "image": "buttermilk.jpg", "desc": "Spiced yogurt drink", "category": "Drinks"},
    {"id": 27, "name": "Orange Juice", "price": 50, "image": "orange.jpg", "desc": "100% pure orange juice", "category": "Drinks"},
    {"id": 28, "name": "Chocolate Milkshake", "price": 50, "image": "chocolate.jpg", "desc": "fully chocolate with icecream fulfilled shake", "category": "Drinks"},
    {"id": 29, "name": "Oreo Milkshake", "price": 50, "image": "oreo.jpg", "desc": "fulfilled with oreo with icecream", "category": "Drinks"},
    {"id": 30, "name": "KitKat Milkshake", "price": 50, "image": "kitkat.jpg", "desc": "fulfilled with kitkat chocolate with chocolate icecream", "category": "Drinks"},
    {"id": 31, "name": "Strawberry Milkshake", "price": 50, "image": "strawberry.jpg", "desc": "fresh strawberry shake with icecream", "category": "Drinks"},
    {"id": 32, "name": "Blackcurrant Milkshake", "price": 50, "image": "blackcurrant.jpg", "desc": "blackcurrant flavour", "category": "Drinks"},
    {"id": 33, "name": "Rose Shake", "price": 50, "image": "rose.jpg", "desc": "it like a rosemilk", "category": "Drinks"},
    {"id": 34, "name": "Butterscotch Shake", "price": 50, "image": "butterscotch.jpg", "desc": "it flavour with butterscotch with icecream", "category": "Drinks"},

    # Desserts
    {"id": 35, "name": "Gulab Jamun", "price": 40, "image": "gulabjamun.jpg", "desc": "Syrupy fried sweet balls", "category": "Desserts"},
    {"id": 36, "name": "Rasmalai", "price": 50, "image": "rasmalai.jpg", "desc": "Soft chenna in sweet milk", "category": "Desserts"},
    {"id": 37, "name": "Ice Cream", "price": 60, "image": "ice.jpg", "desc": "Vanilla, chocolate, or strawberry", "category": "Desserts"},
    {"id": 38, "name": "Chocolate Cake", "price": 70, "image": "chococake.jpg", "desc": "Rich chocolate sponge cake", "category": "Desserts"},
    {"id": 39, "name": "Kheer", "price": 50, "image": "kheer.jpg", "desc": "Rice pudding dessert", "category": "Desserts"},
    {"id": 40, "name": "Jalebi", "price": 40, "image": "jalebi.jpg", "desc": "Crispy spiral sweet", "category": "Desserts"},
    {"id": 41, "name": "Brownie", "price": 60, "image": "brownie.jpg", "desc": "Chocolate fudge square", "category": "Desserts"},
    {"id": 42, "name": "Falooda", "price": 80, "image": "falooda.jpg", "desc": "Milkshake with vermicelli and ice cream", "category": "Desserts"},

    #fastfood
    {"id": 42, "name": "Margherita Pizza", "price": 150, "image": "pizza.jpg", "category": "Fast Food"},
    {"id": 43, "name": "Cheese Burst Pizza", "price": 180, "image": "cheese.jpg", "category": "Fast Food"},
    {"id": 44, "name": "Classic Veg Burger", "price": 100, "image": "burger.jpg", "category": "Fast Food"},
    {"id": 45, "name": "Chicken Zinger Burger", "price": 120, "image": "zinger.jpg", "category": "Fast Food"},
    {"id": 46, "name": "Veg Sandwich", "price": 70, "image": "veg.jpg", "category": "Fast Food"},
    {"id": 47, "name": "Paneer Roll", "price": 90, "image": "paneer.jpg", "category": "Fast Food"},
    {"id": 48, "name": "French Fries", "price": 60, "image": "fries.jpg", "category": "Fast Food"},
    {"id": 49, "name": "Samosa", "price": 20, "image": "samosa.jpg", "category": "Fast Food"},
    {"id": 50, "name": "Aloo Tikki Burger", "price": 80, "image": "aloo.jpg", "category": "Fast Food"},
    {"id": 51, "name": "Chilli Cheese Toast", "price": 85, "image": "chilli.jpg", "category": "Fast Food"},
    {"id": 52, "name": "Grilled Sandwich", "price": 95, "image": "grillsand.jpg", "category": "Fast Food"},
    {"id": 53, "name": "Chicken Nuggets", "price": 110, "image": "chickennugg.jpg", "category": "Fast Food"},
    {"id": 54, "name": "Corn Cheese Balls", "price": 100, "image": "cheeseballs.jpg", "category": "Fast Food"},
    {"id": 55, "name": "Pav Bhaji", "price": 90, "image": "pavbhaji.jpg", "category": "Fast Food"},
    {"id": 56, "name": "Chicken Spring Roll", "price": 75, "image": "chickenspring.jpg", "category": "Fast Food"},

]
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def show_menu():
    category = request.args.get('category')
    if category:
        filtered_menu = [item for item in menu if item['category'] == category]
    else:
        filtered_menu = menu
    return render_template('menu.html', menu=filtered_menu)

@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    item = next((item for item in menu if item['id'] == item_id), None)
    if item:
        cart.append(item)
    return redirect(url_for('show_menu'))

@app.route('/cart', methods=['GET', 'POST'])
def show_cart():
    total = sum(item['price'] for item in cart)
    discount = 0

    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        address = request.form['address']
        coupon = request.form.get('coupon', '').strip().upper()

        # Coupon logic
        if coupon == "FOOD50" and total >= 500:
            discount = 50
        elif coupon == "FIRSTORDER":
            discount = int(total * 0.10)
        elif coupon == "FREEDRINK" and total >= 299:
            cart.append({"name": "Free Soft Drink", "price": 0})
        elif coupon == "DELIVERYFREE":
            discount = 30  # Example delivery charge waived
        elif coupon == "SWEET20":
            dessert_total = sum(item['price'] for item in cart if item.get('category') == 'Desserts')
            discount = int(dessert_total * 0.2)
        elif coupon == "SNACKIT":
            snacks = [item for item in cart if item.get('category') == 'Veg']
            if len(snacks) >= 3:
                discount = snacks[0]['price']  # Give one for free

        final_total = total - discount

        with open("orders.txt", "a", encoding='utf-8') as f:
            f.write(f"Name: {name}, Contact: {contact}, Address: {address}\n")
            for item in cart:
                f.write(f"  - {item['name']} - ₹{item['price']}\n")
            f.write(f"Coupon: {coupon} | Discount: ₹{discount}\n")
            f.write(f"Total: ₹{final_total}\n---\n")

        cart.clear()
        return render_template("success.html", message=f"Order placed successfully! Coupon '{coupon}' applied. You saved ₹{discount}.")

    return render_template('cart.html', cart=cart, total=total)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with open("contact_queries.txt", "a", encoding='utf-8') as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

        return render_template("success.html", message="Thank you for contacting us! We'll get back to you soon.")
    
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        feedback_msg = request.form['feedback']
        with open("feedback.txt", "a") as f:
            f.write(f"{name}: {feedback_msg}\n")
        return render_template("success.html", message="Feedback submitted!")
    return render_template('feedback.html')

@app.route('/offers')
def offers():
    return render_template('offers.html')

if __name__ == '__main__':
    app.run(debug=True)
