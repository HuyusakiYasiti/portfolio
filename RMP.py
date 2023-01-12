#リーチ麻雀の得失点を算出する

class Points:

    def __init__(self, base=20, default=2, limit=2000, digit=100, magnification=2, player=4):

        self.base = base #符底

        self.default = default #場ゾロ

        self.limit = limit #満貫

        self.digit = digit #単位

        self.magnification = magnification #倍払い

        self.player = player #競技人数




    #基本点の算出

    def __base_point(self, fu, fun):

        r = fu + self.base

        r = r if r % 10 == 0 else (r // 10 + 1) * 10

        r =  r * 2 ** (fun + self.default)


        #役満貫の判定

        if r < self.limit:

            pass

        else:

            if fun < 7:

                r = self.limit

            elif fun < 10:

                r = self.limit + int(self.limit // 2)

            elif fun < 13:

                r = self.limit * 2

            elif fun < 15:

                r = self.limit * 3

            else:

                r = self.limit * 4


        return r




    #得失点の算出

    def invoice(self, fu, fun, unit=4):

        u = unit

        r = self.__base_point(fu, fun) * u

        return r if r % self.digit == 0 else (r // self.digit + 1) * self.digit









if __name__ == '__main__':

    res = Points()

    #点数表を書く

    for i in range(2, 50, 10):

        for j in range(1, 5):

            print(res.invoice(i, j), end=' ')

        print('')



