
class game(object):

    #历史最高分
    top_socre = 0

    def __init__(self, player_nmae):
        self.player_name = player_nmae

    @staticmethod
    def show_help():
        print("游戏帮助信息：让你体验非凡之旅....")

    @classmethod
    def current_score(cls):
        print("当前分数为 [%d]" % cls.top_socre)

    def start_game(self):
        print("beginning　play game [%s]" % self.player_name)
        game.top_socre += 50




game.show_help()
game.current_score()
print("**************************")
game1 = game("xiaoming")
game1.start_game()

game.show_help()
game.current_score()
print("**************************")
game1.start_game()
game1.start_game()
game1.start_game()
game1.start_game()
game.current_score()