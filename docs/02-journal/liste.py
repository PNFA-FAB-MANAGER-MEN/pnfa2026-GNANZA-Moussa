machines=["laser", "cnc", " perceuse" ]
machines.appent("imprimante 3D")
machines.remove("perceuse")
print(machines[0])
print(len(machines))
print(machines[1:3])

machines.sort()
print(machines)