from model import InputForm
from flask import Flask, render_template, request
from compute import compute

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.a.data, form.b.data,form.c.data, form.d.data,form.e.data,form.z.data,form.g.data,form.h.data,form.i.data)
                         
    else:
        result = None

    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug = True)