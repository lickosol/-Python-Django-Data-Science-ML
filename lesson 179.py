'''
создать магичекий оператор сравнения, чтобы при print(first_comment == second_comment) выводило True/False
при сравнении текстов или количества votes_qty этих комментариев
'''

class Comment:

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __eq__(self, other):
        if self.text == other.text:
            return True
        else:
            return False

first_comment = Comment("First comment")
second_comment = Comment("First comment")

print(first_comment == second_comment)