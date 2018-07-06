population = {"Chicago":2.7, "New York":8.17, "Rome":2.87,
              "Paris":2.24, "London":8.78}
status = {200:"ok", 404:"not found", 400:"bad request"}

print(status[200])
print(301 in status)
population["Rome"] += 0.11
print(population["Rome"])
