import mongoengine as db
# from mongoengine import Document, EmbeddedDocument, StringField, IntField, ListField
from datetime import datetime

class OverlayItem(db.EmbeddedDocument):
    type = db.StringField(choices=["image", "text"], required=True)
    content = db.StringField() 
    dragX = db.IntField(required=True)
    dragY = db.IntField(required=True)
    resizeW = db.IntField(required=True)
    resizeH = db.IntField(required=True)

class User(db.Document):
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)
    user_name = db.StringField(unique=True,required=True,max_length=25)
    rtsp_url = db.StringField(required=True)
    overlays =  db.ListField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(User, self).save(*args, **kwargs)