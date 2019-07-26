# For more details, see
# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#declare-a-mapping
from anthill.framework.db import db
from anthill.framework.utils.asynchronous import as_future
from sqlalchemy_utils.types import URLType, JSONType, ColorType


class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    title = db.Column(db.String(512), nullable=False, unique=True)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    versions = db.relationship('ApplicationVersion', backref='application', lazy='dynamic')

    @as_future
    def latest_version(self):
        return self.versions.last()


class ApplicationVersion(db.Model):
    __tablename__ = 'application_versions'
    __table_args__ = (
        db.UniqueConstraint('value', 'application_id'),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String(128), nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('applications.id'), nullable=False)
    environment_id = db.Column(db.Integer, db.ForeignKey('environments.id'), nullable=False)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    def __lt__(self, other):
        return self.value < other.value


class Environment(db.Model):
    __tablename__ = 'environments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(512), nullable=False)
    discovery = db.Column(URLType, nullable=False)
    payload = db.Column(JSONType, nullable=False, default={})
    color = db.Column(ColorType)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    app_versions = db.relationship('ApplicationVersion', backref='environment', lazy='dynamic')
