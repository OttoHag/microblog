from app import create_app, db
from app.models import Post

app = create_app()
with app.app_context():
    posts = db.session.execute(db.select(Post).order_by(Post.timestamp.desc()).limit(5)).scalars().all()
    for p in posts:
        print(f'Post ID: {p.id}, Body: {p.body[:50]}..., Language: "{p.language}"')
