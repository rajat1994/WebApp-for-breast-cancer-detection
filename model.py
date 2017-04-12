from wtforms import Form, FloatField, validators


class InputForm(Form):
    a = FloatField(
        label='Clump Thickness', default=1,
        validators=[validators.InputRequired()])
    b = FloatField(
        label='Uniformity of Cell Size', default=1,
        validators=[validators.InputRequired()])
    c = FloatField(
        label='Uniformity of Cell Shape', default=1,
        validators=[validators.InputRequired()])
    d = FloatField(
        label='Marginal Adhesion', default=1,
        validators=[validators.InputRequired()])
    e = FloatField(
        label='Single Epithelial Cell Size', default=1,
        validators=[validators.InputRequired()])
    z = FloatField(
        label='Bare Nuclei', default=1,
        validators=[validators.InputRequired()])
    g = FloatField(
        label='Bland Chromatin', default=1,
        validators=[validators.InputRequired()])
    h = FloatField(
        label='Normal Nucleoli', default=1,
        validators=[validators.InputRequired()])
    i = FloatField(
        label='Mitoses', default=1,
        validators=[validators.InputRequired()])