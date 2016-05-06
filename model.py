from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def example_data():
    """Create example data for the test database."""
    
    Game.query.delete()

    monopoly = Game(name= "Monopoly", description="Great capitalist game!")
    life = Game(name= "Life", description="Practice for the real thing!")
    resistance = Game(name= "Resistance", description="Ruin your friendships today!")

    db.session.add_all([monopoly, life, resistance])
    db.session.commit()
    #FIXME: write a function that creates a game and adds it to the database.
    print "FIXED"


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
