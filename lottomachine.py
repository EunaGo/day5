import random

def makenums():

    balls = [i for i in range(1,46)]

    random.shuffle(balls)

    return balls[0:6]

def input_display():
    money = int(input("금액을 입력하세요"))
    if money % 1000 != 0:
        print("다시요...")
        return input_display()          #재귀함수
    else:

        return money / 1000

def main():
    count = input_display()
    for x in range(int(count)):
        nums = makenums()
        print(sorted(nums))
    print("........00.............")


if __name__ == "__main__":
    main()