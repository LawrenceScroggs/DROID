from droid import db
from datetime import datetime


class Admins(db.Model):
    ADMIN_ID = db.Column(db.String, primary_key=True)
    EMAIL_ADMIN = db.Column(db.String, unique=True, nullable=False)
    ACTIVE = db.Column(db.Boolean)
    def __repr__(self):
        return f"Admins('{self.ADMIN_ID}','{self.EMAIL_ADMIN}','{self.ACTIVE}')"

class Approval(db.Model):
    APPROVAL_ID = db.Column(db.String, primary_key=True)
    PIC_ID = db.Column(db.String, unique=True)
    ADMIN_ID = db.Column(db.String, unique=True)
    DATE_SUB = db.Column(db.DateTime, nullable=False)
    EDITED_PIC_ID = db.Column(db.String, unique=True)
    DATE_APPR = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return f"Approval('{self.APPROVAL_ID}','{self.PIC_ID}','{self.ADMIN_ID}','{self.DATE_SUB}','{self.EDITED_PIC_ID}','{self.DATE_APPR}')" 
