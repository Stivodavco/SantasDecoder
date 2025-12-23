from flask import Flask, request, render_template
from verifier import Verifier

app = Flask(__name__)

@app.route('/')
def index():
    person = request.args.get("person")
    code = request.args.get("code")

    if code:
        try:
            int(code)
        except ValueError:
            return render_template("index.html", correct=False, person=person, code=code)

        verif = Verifier()

        correct, present = verif.verify(person, int(code))

        return render_template("index.html", correct=correct, present=present, person=person, code=code)
    else:
        return render_template("index.html", person=person, code=code)


if __name__ == '__main__':
    app.run()
