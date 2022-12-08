from itertools import combinations

from ...core.exceptions import ValidationError


class MathsService:

    def _max_common_multiple(self, a: int, b: int):
        if b == 0:
            return a
        return self._max_common_multiple(b, a % b)

    def _least_common_multiple(self, a: int, b: int):
        return (a * b) / self._max_common_multiple(a, b)

    def get_least_common_multiple(self, numbers: list[int]):
        if len(numbers) == 1:
            raise ValidationError("You cannot get the least common multiple for a single number.")
        comb = combinations(numbers, 2)
        least_common_multiple_list = {}
        for i in list(comb):
            least_common_multiple_list[f"least common multiple for {i}"] = self._least_common_multiple(*i)
        return least_common_multiple_list
