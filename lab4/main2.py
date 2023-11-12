# TODO решите задачу
import json
txt = "input.json"

def task() -> float:
    data3 = 0
    with open(txt,"r") as f:
        data = json.load(f)
        data1 =[i['score'] for i in data]
        data2 =[i['weight'] for i in data]
        for i in range(0,(len(data1))):
            data3 += data1[i]/data2[i]
        return (f"{data3:.3f}")
print(task())
