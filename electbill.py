# electronicsgst=18%
def calelectgst(a,b):
    amt=a+b
    return amt + (amt*18/100) 

# fashiongst=13%
def calfashiongst(c,d):
    amt=c+d
    return amt + (amt*13/100)

# foodgst=7%
def calfoodgst(e):
    return e + (e*7/100)

# totalbill
def totalbill(a,b,c,d,e):
    elect=calelectgst(a,b)
    fashion=calfashiongst(c,d)
    food=calfoodgst(e)
    return elect+fashion+food

# cal discount bill
def caldiscountbill(a,b,c,d,e):
    total=totalbill(a,b,c,d,e)
    discount=total*20/100
    return total-discount

# sample value
a=100
b=100
c=100
d=100
e=100

total=totalbill(a,b,c,d,e)
discount=total*20/100
final_amt=caldiscountbill(a,b,c,d,e)

print(f"total after gst={total:.2f}")
print(f"discount={discount:.2f}")
