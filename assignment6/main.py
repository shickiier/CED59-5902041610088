from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def member():
    return render_template('member.html')

@app.route('/', method=["POST"])
def register():
    return 'Done!'

if __name__ == "__main__":
    app.run()
