import time

start_time = time.time()
end_time = start_time + 5

while time.time() < end_time:
    remaining_time = end_time - time.time()
    print("Tempo restante: {:.0f} segundos".format(remaining_time))
    time.sleep(1)

print("Tempo decorrido: 5 segundos")
