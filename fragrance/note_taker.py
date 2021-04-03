

company_name = input("Company name: ")

file = open(company_name+".txt", 'w')
while True:
    name = input("name: ")
    if name == "":
        break
    file.write(name + '\n')
   # for i in range(3):
   #     note = input("note: ")
   #     file.write(note +"\n")
    top = input("top: ")
    input("pass")
    file.write(top+ '\n')
    mid = input("mid: ")
    input("pass")
    file.write(mid+ '\n')
    bot = input("bot: ")
    input("pass")
    file.write(bot+ '\n')
file.close()
