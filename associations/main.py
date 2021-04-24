import logging
from uuid import uuid4, UUID

from fastapi import FastAPI

from game import Game

app = FastAPI()

games: dict[UUID, Game] = {}
MAX_GAMES = 5


@app.get("/")
def intro() -> dict:
    """
    intro info
    :return: message
    """
    return {"msg": "please open Swagger: host:8080/docs"}


@app.get("/start")
def start_new_game() -> dict:
    """
    Start new game
    :return: message
    """
    if len(games) < MAX_GAMES:
        uuid = uuid4()
        games[uuid] = Game()
        return {"uuid": f"{uuid}"}
    else:
        return {"Error": "Sorry! We can't create new games."}


@app.get("/stop")
def stop_all_games() -> dict:
    """
    Stop all games
    :return: message
    """
    games.clear()
    return {"msg": "All games stopped"}


@app.get("/games/uuids")
def games_run_now() -> dict:
    """
    :return: message for all run games
    """
    return {"uuids": list(games.keys())}


@app.get("/games/{uuid}")
def game_info(uuid: str) -> dict:
    """
    return info about game by uuid
    :param uuid:
    :return: message
    """
    logging.info(uuid)
    logging.info(games.keys())
    if UUID(uuid) in games.keys():
        select_game: Game = games.get(UUID(uuid))
        return {
            "uuid": uuid,
            "start_time": select_game.start_time,
            "field": select_game.field,
        }
    else:
        return {"Error": f"{uuid} game not found!"}
