import random

class num_baseball_Game:

    def __init__(self):
        self.ch =0  #게임 스타트 판단 변수
        self.user = []  #유저 답
        self.com = []   #컴퓨터 수비 답
        self.strike = 0 #맞은거 판단
        self.ball = 0   #ball판단
        self.out = 0    #틀린거 판단
        self.round_collect = {} # 내가 제출한 정답 저장
        self.user_send = {}
        self.round_game = 1 #몇판했는지

    def make_com_num(self):
        print("★게임을 시작합니다.★\n======================")
        self.com = []
        while True:
            a = random.randrange(0, 10)
            if a not in self.com:
                self.com.append(a) # 컴퓨터 숫자 생성
                if len(self.com) > 2:
                    break


    def user_num(self):
        while True:
            print("0~9까지 3개의 숫자를 입력하세요")
            try:
                user_num1 = int(input("1번째 숫자를 입력하세요 : "))
                user_num2 = int(input("2번째 숫자를 입력하세요 : "))
                user_num3 = int(input("3번째 숫자를 입력하세요 : "))

                if user_num1 > 9 and user_num2 > 9 and user_num3 > 9:
                    print("\n숫자 범위가 넘었습니다. \n 다시 입력해주세요.\n")
                else:
                    self.user = [user_num1, user_num2, user_num3]
                    self.user_send = {self.round_game : self.user}
                    break

            except ValueError:
                print("\n잘못된 형태의 정보를 입력했습니다. \n 다시 입력해 주세요\n")


    def playGame(self):
        self.make_com_num()
        while True:
            if self.ch == 0:
                self.user_num()
            else:
                try:
                    print("다시 플레이 하시겠습니까?")
                    replay = int(input("다시하시길 원하시면 숫자 1입력, 그만하길 원하면 0입력 : "))
                    print("")
                    if replay == 0:
                        print("\n================\n게임이 종료됐습니다.\n================")
                        break
                    else:
                        self.round_collect = {}
                        self.round_game = 0
                        self.make_com_num()
                        self.user_num()
                        self.ch = 0
                except ValueError:
                    print("\n================\n잘못입력했습니다. 게임을 종료합니다.\n================\n")
                    break


            if self.com == self.user:
                self.round_game += 1
                print("\n========================")
                print("총 라운드는 ", self.round_game, "\n승리!!!!!!!\n")
                self.ch = 1
            else:
                for i in range(len(self.user)):
                    if self.user[i] == self.com[i]:
                        self.strike += 1
                    elif self.user[i] in self.com:
                        self.ball += 1
                    else:
                        self.out += 1
                self.round_collect.update({str(self.round_game) + ": " + str(self.user_send[self.round_game]): {
                    "strike": self.strike,
                    "ball": self.ball,
                    "out":self.out}
                })

                self.round_game += 1
                print("========== 내 play list ===========\n")
                for i, j in self.round_collect.items():
                    print("{!r:10s} : {}".format(i, j))
                print("\n================================\n")

            self.strike = 0
            self.ball = 0
            self.out = 0


if __name__ == "__main__":
    play = num_baseball_Game()
    play.playGame()