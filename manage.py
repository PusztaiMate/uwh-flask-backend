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
    p1 = add_player_if_not_present("Jakab Gipsz")
    p2 = add_player_if_not_present("Júlia Gipsz")
    p3 = add_player_if_not_present("János Gipsz")
    p4 = add_player_if_not_present("József Gipsz")
    p5 = add_player_if_not_present("Janka Gipsz")
    p6 = add_player_if_not_present("Jenő Gipsz")
    c1 = add_club_if_not_present("Egyszusz VSE", players=[p1, p2, p3])
    c2 = add_club_if_not_present("Piranha VSE", players=[p6, p4, p5])
    add_training(players=[p1, p2, p3, p4, p5, p6], club_id=c1.id, date="2020-01-01")
    add_training(players=[p1, p2, p3, p4, p5], club_id=c1.id, date="2020-01-03")
    add_training(players=[p1, p2, p3, p4], club_id=c1.id, date="2020-01-08")
    add_training(players=[p1, p2, p3], club_id=c2.id, date="2020-01-10")
    add_training(players=[p1, p2], club_id=c2.id, date="2020-01-15")


if __name__ == "__main__":
    cli()
