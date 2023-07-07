from flask import Flask, render_template

app = Flask(__name__)

class Homepage:
    def render(self):
        return render_template('homepage.html')

@app.route('/')
def home():
    homepage = Homepage()
    return homepage.render()

if __name__ == '__main__':
    app.run()
