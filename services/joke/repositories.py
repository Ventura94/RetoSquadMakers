from data_access.repositories import ChuckNorrisRepository, CanHazDadJokeRepository, JokeRepository


class Repository:
    def __init__(self):
        self.chuck_norris_repository = ChuckNorrisRepository()
        self.can_haz_dad_joke_repository = CanHazDadJokeRepository()
        self.joke_database_repository = JokeRepository()
