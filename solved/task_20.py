"""
https://www.codewars.com/kata/51fda2d95d6efda45e00004e
Codewars style ranking system
"""


class User:
    rank = -8
    progress = 0

    def inc_progress(self, new_rank):
        if new_rank < -8 or new_rank == 0 or new_rank > 8:
            raise RuntimeError("Неверный ранг")
        delta = new_rank - self.rank
        if self.rank < 0 < new_rank:
            delta -= 1
        elif new_rank < 0 < self.rank:
            delta += 1

        if delta == -1:
            self.progress += 1
        elif delta == 0:
            self.progress += 3
        elif delta > 0:
            self.progress += 10 * (delta ** 2)
        if self.progress >= 100:
            rank_up = self.progress // 100
            if (self.rank+rank_up)*self.rank <= 0:
                rank_up += 1
            self.rank += rank_up
            self.progress %= 100
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0




# 7 4 -3 -3 -6 2 2 3 4 7
user = User()
user.inc_progress(7)
user.inc_progress(4) # will add 90 progress
user.inc_progress(-3)
user.inc_progress(-3)
user.inc_progress(-6)
user.inc_progress(2)
user.inc_progress(2)
user.inc_progress(3)
user.inc_progress(4)
print(user.rank)
print(user.progress)
user.inc_progress(7)
print(user.rank)
print(user.progress)

user.inc_progress(9)
