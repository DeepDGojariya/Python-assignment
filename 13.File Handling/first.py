planets = ["Mercury","Venus","Earth","Mars","Jupiter"]

file=open("new_text_file.txt","w")
for planet in planets:
    file.write(planet+"\n")
file.close()

file = open("new_text_file.txt","r")
for line in file.readlines():
    planets.append(line)
file.close()

newPlanets = ["Saturn","Pluto"]
file = open("new_text_file.txt","a")
for planet in newPlanets:
    file.write(planet+"\n")
file.close()
