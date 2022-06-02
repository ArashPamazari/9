class saAt:

    def __init__(self,h,m,s):
        self.hour = h
        self.min = m
        self.sec = s

    def sum(self,mehman):
        result = saAt(None,None,None)
        result.hour = self.hour + mehman.hour
        result.min = self.min + mehman.min
        result.sec = self.sec + mehman.sec

        if result.sec >= 60:
            result.sec -= 60
            result.min += 1  

        if result.min >= 60:
            result.min -= 60
            result.hour += 1 

        return result

    def sub(self,mehman):
        result = saAt(None,None,None)
        result.hour = self.hour - mehman.hour
        result.min = self.min - mehman.min
        result.sec = self.sec - mehman.sec

        if result.sec <= 60:
            result.sec += 60
            result.min -= 1  

        if result.min <= 60:
            result.min += 60
            result.hour -= 1 

        return result

    def Con_Sec_To_Time(self,mehman):
        result = saAt(None,None,None)

        result.sec = (self.hour*3600) + (self.min*60) + (self.sec)

        return result


    def show(self):
        print(self.hour,':',self.min , ':' , self.sec )




t1 =saAt(2,30,45)
t2 =saAt(3,17,40)


a = t1.sum(t2)
a.show()

b = t2.sub(t1)
b.show()

c = t1.Con_Sec_To_Time(t1)
c.show()
