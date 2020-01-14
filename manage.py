from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Player, Training, Club


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    p = Player("Jakab", "Gipsz", "jakab@gipsz.hu")
    db.session.add(p)
    db.session.commit()
    c = Club("Best VSE")
    db.session.add(c)
    db.session.commit()
    t = Training(c.id, "2020-01-01T19:30:00", players=[p])
    db.session.add(t)
    db.session.commit()


if __name__ == "__main__":
    cli()
