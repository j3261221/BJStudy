def max_temperature_sum(N, K, temperatures):
    current_sum = sum(temperatures[:K])
    max_sum = current_sum

    for i in range(K, N):
        current_sum += temperatures[i] - temperatures[i - K]
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

print(max_temperature_sum(N, K, temperatures))