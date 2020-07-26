class Square():
    square_list = list()

    def __init__(self,s):
        self.site = s
        self.area = s**2
        self.square_list.append(self.site)

    def __repr__(self):
        return "{} на {} на {} на {}".format(str(self.site),
                                             str(self.site),
                                             str(self.site),
                                             str(self.site))

s1 = Square(10)
s2 = Square(23)
s22 = s2
s3 = Square(30)

print(Square.square_list)
print(s2)
print(s22 is s2)
print(s2.area)
