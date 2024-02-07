from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Length,Optional

class Note(FlaskForm):
    name = StringField(validators=[Optional()],default="")
    heading = StringField(validators=[Optional()], default="")
    description = StringField(validators=[DataRequired()])

    class Meta:
        csrf = False
    

class AddNote(Note):
    pass

class UpdateNote(Note):
    pass
    

