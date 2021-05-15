from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("profile.html", num=3, color="blue")

    @app.route('/play/<int:num>')
    def play_num(num):
        return render_template("profile.html", num=num)

    @app.route('/play/<int:num>/ <color>')
    def play_num(num, color):
        return render_template("profile.html", num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
