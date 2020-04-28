from flask import Flask, render_template, redirect

# Create an instance of Flask
app = Flask(__name__)
            

@app.route('/', methods=['GET', 'POST'])
def home():
    print("Home Page")
    return render_template('index.html')


@app.route("/about", methods=['GET', 'POST'])
def about():
    print('About Page')
    return render_template('about.html')

@app.route("/beauty", methods=['GET', 'POST'])
def beauty():
    print('Beauty Project')
    return render_template('beauty.html')

@app.route("/galaxy", methods=['GET', 'POST'])
def galaxy():
    print('Galaxy Page')
    return render_template('galaxy.html')

@app.route("/homeslice", methods=['GET', 'POST'])
def homeslice():
    print('HomeSlice Page')
    return render_template('homeslice.html')

@app.route("/music", methods=['GET', 'POST'])
def music():
    print('Musics Page')
    return render_template('music.html')

@app.route("/photometry", methods=['GET', 'POST'])
def photometry():
    print('Photometry Page')
    return render_template('photometry.html')

if __name__ == "__main__":
    app.run(debug=True)


