

class Quiz:

    def __init__(self, text):
        self.text = text
        self.yes = None
        self.no = None


q1 = Quiz("sns 사진 올린다.")
q2 = Quiz("먹는걸 좋아한다.")
q3 = Quiz("힙하다는 얘기를 자주 듣는다.")


q1.yes = q2
q1.no = q3

current = q1

answer = input(current.text)

if answer == 'y':
    current = current.yes

elif answer == 'n':
    current = current.no
