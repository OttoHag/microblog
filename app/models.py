from datetime import datetime, timezone
from hashlib import md5
from typing import Optional, List
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

followers = sa.Table(
    'followers',
    db.metadata,
    sa.Column('follower_id', sa.Integer, sa.ForeignKey('user.id'), primary_key=True),
    sa.Column('followed_id', sa.Integer, sa.ForeignKey('user.id'), primary_key=True)
)

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    about_me: so.Mapped[Optional[str]] = so.mapped_column(sa.String(140))
    last_seen: so.Mapped[Optional[datetime]] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc)) 

    posts: so.Mapped[List['Post']] = so.relationship(
        back_populates='author',
        lazy='dynamic'
    )

    following: so.Mapped[List['User']] = so.relationship(
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    followers: so.Mapped[List['User']] = so.relationship(
        secondary=followers,
        primaryjoin=(followers.c.followed_id == id),
        secondaryjoin=(followers.c.follower_id == id),
        backref=backref('following', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def follow(self, user):
        if not self.is_following(user):
            self.following.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.following.remove(user)
    
    def followers_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()

    def followed_posts(self):
        followed_ids = self.following.with_entities(User.id).subquery()
        return (
            sa.select(Post)
            .where(
                sa.or_(
                    Post.user_id == self.id,
                    Post.user_id.in_(followed_ids)
                )
           )
            .order_by(Post.timestamp.desc())
       )

@login.user_loader
def load_user(id):
    return db.session.execute(sa.select(User).where(User.id == int(id))).scalar_one_or_none()

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey('user.id'), index=True)
    author: so.Mapped['User'] = so.relationship(
        back_populates='posts')
    
    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
    def __str__(self):
        return f'Post(id={self.id}, body="{self.body}", timestamp={self.timestamp}, user_id={self.user_id})'

