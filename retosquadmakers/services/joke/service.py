import random

from fastapi import Depends

from retosquadmakers.services.joke.enums import JokeProviderEnum
from retosquadmakers.services.joke.repositories import Repository


class JokeService:

    def __init__(self, repository: Repository = Depends()):
        self.repositories = repository

    async def get_joke(self, provider: JokeProviderEnum | None):
        if provider == JokeProviderEnum.Chuck:
            return await self.repositories.chuck_norris_repository.get_random_joke()
        if provider == JokeProviderEnum.Dad:
            return await self.repositories.can_haz_dad_joke_repository.get_random_joke()
        if provider == JokeProviderEnum.Random or provider is None:
            providers = [self.repositories.chuck_norris_repository, self.repositories.can_haz_dad_joke_repository]
            provider = providers[random.randint(0, len(providers) - 1)]
            return await provider.get_random_joke()
