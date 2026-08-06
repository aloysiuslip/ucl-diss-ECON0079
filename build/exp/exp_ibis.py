import ibis

xy = ibis.schema({"x": int, "y": str})
xy2 = ibis.schema({"x": int, "y": str})
yx = ibis.schema({"y": str, "x": int})
xy_float = ibis.schema({"x": float, "y": str})

import time

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

for i in range(5, 0, -1):
    print(f"\rCountdown: {strike('my number ' + str(i))}  ", end="", flush=True)
    time.sleep(1)
print("\rDone!       ")  

