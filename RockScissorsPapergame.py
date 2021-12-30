import random

class Janggangbo:

    results = {
        'example' : {
            1 : 'Rock',
            2 : 'Paper',
            3 : 'Scissors'
        },
        'person' : {
            'Rock': 1,
            'Paper': 2,
            'Scissors': 3
        }
    }

    def check_collect(self, info):
        while True:
            if self.user_send not in self.results['person'].keys():
                print("잘못된 값입니다. 다시 입력하세요!!")
                self.user_send = input("무엇을 낼지 선택하세요(Rock, Scissors, Paper) => ")
            else:
                break

    def gamePlay(self):
        self.all_count = 0
        print("게임을 시작합니다.\n")
        while True:
            self.com = random.randrange(1, 4)

            print("게임을 종료하고 싶으면 0을 입력하세요")
            print(self.results['example'].values())

            self.user_send = input("무엇을 낼지 선택하세요(Rock, Scissors, Paper) => ")

            if self.user_send == '0':
                break

            self.check_collect(self.user_send)


            user_check = self.results['person']
            self.winning_count = 0

            if self.com == user_check[self.user_send]:
                print("비겼습니다")
            elif self.com != user_check[self.user_send]:
                if self.com < user_check[self.user_send] or (self.com == 3 and user_check[self.user_send] == 1):
                    print("이겼습니다.")
                    self.winning_count += 1
                else:
                    print("졌습니다.")

            self.all_count += 1
            print("\n")
            print("===============================================")
            print("컴퓨터 : " + str(self.results['example'][self.com]))
            print(" 유 저 : " + str(self.results['example'][user_check[self.user_send]]))
            print("현재까지 플레이한 횟수 : " + str(self.all_count) +"\n현재까지 승률 : " + str(self.winning_count / self.all_count * 100))
            print("===============================================")
            print("\n")

if __name__ == "__main__":
    play = Janggangbo()
    play.gamePlay()
