from flask import Flask, render_template, request, redirect, url_for

app = Flask('Storyforge')

# Home page
@app.route('/')
def home():
    return render_template('Story-forge.html')

# About page
@app.route('/about')
def about():
    return render_template('Story-Forge-About.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('Story-Forge-Contact.html')

# Layout page
@app.route('/Layout')
def layout():
    return render_template('Layout.html')

# Dynamic page that displays a number
@app.route('/display_number/<int:number>')
def display_number(number):
    return f"Number {number}"

# Dynamic page that displays a user's profile
@app.route('/dynamic', methods=['GET', 'POST'])
def dynamic():
    if request.method == 'POST':
        number = request.form['number']
        return redirect(url_for('display_number', number=number))
    return render_template('dynamic.html')

if __name__ == '__main__':
    app.run(debug=True)
