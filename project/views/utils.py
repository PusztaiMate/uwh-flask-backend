from project.api.models import Player


def get_all_players_sorted() -> list:
    return Player.query.order_by(Player.lname)


def sort_player_list_by_name(players: list) -> list:
    return sorted(players, key=lambda p: p.lname)
