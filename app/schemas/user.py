from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FieldList, FormField,Field
from wtforms.validators import InputRequired

class ListField(Field):
    def process_formdata(self, valuelist):
        print(valuelist)
        self.data = valuelist

class OverlayItemForm(FlaskForm):
    type = SelectField("Type", choices=[("image", "Image"), ("text", "Text")], validators=[InputRequired()])
    content = StringField("Content")
    dragX = IntegerField("Drag X", validators=[InputRequired()])
    dragY = IntegerField("Drag Y", validators=[InputRequired()])
    resizeW = IntegerField("Resize Width", validators=[InputRequired()])
    resizeH = IntegerField("Resize Height", validators=[InputRequired()])
    class Meta:
        csrf = False

class User(FlaskForm):
    user_name = StringField("UserName",validators=[InputRequired()])
    overlays = ListField()


    class Meta:
        csrf = False

class GetUser(User):
    pass

class AddUser(User):
    rtsp_url = StringField("RtspUrl", validators=[InputRequired()])
    class Meta:
        csrf = False









 
    


