"""Data models."""
from server import db
from server.constant import Constant


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )

    role = db.Column(
        db.Enum(Constant.ROLE['USER_ROLE']),
        default=Constant.ROLE['USER_ROLE'].user
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)
