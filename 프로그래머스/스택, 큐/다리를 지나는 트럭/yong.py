bridge_length = 100
weight = 100
truck_weights = [,10,10,10,10,10,10,10,10,10]

bridge = [0 for _ in range(bridge_length)]  # 다리 배열 []
result = 0

while bridge:
    result += 1
    bridge.pop(0)

    if truck_weights:
        if sum(bridge) + truck_weights[0] <= weight:
            # 기존에 다리에 올라와있는 트럭과 앞으로 올라갈 트럭 비교
            t = truck_weights.pop(0)
            bridge.append(t)
        else:
            bridge.append(0)

print(result)