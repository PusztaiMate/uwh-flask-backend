from project import db
from project.api.models import Club, Player, Training


def add_player(name: str) -> Player:
    fname, lname = name.split(" ")
    p = Player(fname=fname, lname=lname, email=f"{fname.lower()}@{lname.lower()}.hu")
    db.session.add(p)
    db.session.commit()
    return p


def add_player_if_not_present(name: str) -> Player:
    fname, lname = name.split(" ")
    email = f"{fname.lower()}@{lname.lower()}.hu"
    p = Player.query.filter_by(email=email).first()
    if not p:
        p = Player(fname=fname, lname=lname, email=email)
        db.session.add(p)
        db.session.commit()
    return p


def add_training(players: list = None, club_id: int = None) -> Training:
    if players:
        player_ids = [p.id for p in players]
    else:
        player_ids = []
    t = Training(player_ids=player_ids, club_id=club_id)
    db.session.add(t)
    db.session.commit()
    return t


def add_club(name: str, players: list = None) -> Club:
    players = players or []
    c = Club(name=name, player_ids=[p.id for p in players], training_ids=None)
    db.session.add(c)
    db.session.commit()
    return c


def add_club_if_not_present(name: str, players: list = None) -> Club:
    players = players or []
    c = Club.query.filter_by(name=name).first()
    if not c:
        c = Club(name=name, player_ids=[p.id for p in players], training_ids=None)
        db.session.add(c)
        db.session.commit()
    return c
