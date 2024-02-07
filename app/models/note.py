import mongoengine as db
from app.models.user import User
from datetime import datetime


class Note(db.Document):
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)
    name = db.StringField()
    heading = db.StringField()
    description = db.StringField(required=True)
    user = db.ReferenceField(User,reverse_delete_rule=2)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(Note, self).save(*args, **kwargs)