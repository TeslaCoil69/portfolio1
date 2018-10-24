scores = []

def avg():
      for x in range(10):
        scores.insert(x,int(input("score?:")))
      total = sum(scores)
      output = total/10
      return output
a=avg()
b="a"
if a >= 90:
      b="A"
elif a > 80 & a<90:
      b="b"

elif a > 70 & a<80:
      b="c"
elif a > 60 & a<70:
      b="d"
elif a > 50 & a<60:
      b="f"
elif a > 40 & a<50:
      b="f"
elif a > 30 & a<40:
      b="f"
elif a > 20 & a<30:
      b="f"
elif a > 10 & a<20:
      b="f"
elif a > 0 & a<10:
      b="f"


print(avg," grade "+b)







      
