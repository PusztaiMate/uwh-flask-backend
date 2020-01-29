from flask.cli import FlaskGroup

from project import create_app, db
from project.tests.db_utils import (
    add_club_if_not_present,
    add_player_if_not_present,
    add_training,
)


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    p = add_player_if_not_present("Jakab Gipsz")
    c = add_club_if_not_present("Egyszusz VSE")
    add_club_if_not_present("Piranha Pécs", players=[p,])
    add_training(players=[p], club_id=c.id)
    c.players.append(p)
    db.session.add(c)
    db.session.commit()


if __name__ == "__main__":
    cli()
