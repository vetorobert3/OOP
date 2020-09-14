class Bicycle():
    def exclaim(self):
        print("I'm a Bicycle!")

class Specialized(Bicycle):
    def exclaim(self):
        print("I'm a Specialized! I'm a more specialized version of a Bicycle!")

a_bicycle = Bicycle()
a_specialized = Specialized()

print(a_bicycle.exclaim())
print(a_specialized.exclaim())