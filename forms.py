from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import EmailInput


class ContactForm(FlaskForm):
    name = StringField(
        name='nom-complet',
        label='Nom complet *',
        render_kw={"placeholder": "nom complet"},
        validators=[DataRequired(message="Votre nom est requis.")]
    )
    profession = SelectField(
        name='profession',
        choices=['Éducateur canin', 'Particulier', 'Autre (préciser)'],
        label="Vous êtes un:"
    )
    email = StringField(
        name='email',
        label="Email *",
        render_kw={"placeholder": "email"},
        widget=EmailInput(),
        validators=[DataRequired(message="Votre email est requis."), Email()]
    )
    phone = StringField(
        name='telephone',
        label="Téléphone",
        render_kw={"placeholder": "téléphone"}
    )
    message = TextAreaField(
        name='message',
        label="Votre message *",
        render_kw={"placeholder": "votre message"},
        validators=[DataRequired(message="Ce champ est requis.")]
    )
