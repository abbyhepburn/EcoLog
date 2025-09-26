import webbrowser
import os
fwpoints, swpoints, fpoints, apoints, gpoints = 0,0,0,0,0
fwcount, swcount, fcount, acount, gcount  = 0,0,0,0,0
total = ""
type = ""
times = 0
def points(n):
    global total
    global fwcount, swcount, fcount, gcount, acount
    if (n >= 1) and (n <= 4):
        if (fwcount != 0) and (swcount != 0) and(fcount != 0) and(acount != 0) and(gcount != 0):
            print("")
        else:
            if fwcount == 0:
                if type == "freshwater":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/freshwater/babysal.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Salmon, "
                    fwcount += 1
            if swcount == 0:
                if type == "saltwater":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/saltwater/babyhc.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Crab, "
                    swcount += 1
            if fcount == 0:
                if type == "forest":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/forest/babyred.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Red Panda, "
                    fcount += 1
            if acount == 0:
                if type == "arctic":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/arctic/babyseal.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Seal, "
                    acount += 1
            if gcount == 0:
                if type == "grassland":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/grassland/babyham.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Hamster, "
                    gcount += 1
    if n >= 10 and n < 20:
        if (fwcount != 1) and (swcount != 1) and (fcount != 1) and (acount != 1) and (gcount != 1):
            print("")
        else:
            if fwcount == 1:
                if type == "freshwater":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/freshwater/juvsal.html")
                    webbrowser.open(f"file://{file_path}")
                    fwcount += 1
            if swcount == 1:
                if type == "saltwater":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/saltwater/juvhc.html")
                    webbrowser.open(f"file://{file_path}")
                    swcount += 1
            if fcount == 1:
                if type == "forest":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/forest/juvred.html")
                    webbrowser.open(f"file://{file_path}")
                    fcount += 1
            if acount == 1:
                if type == "arctic":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/arctic/juvseal.html")
                    webbrowser.open(f"file://{file_path}")
                    acount += 1
            if gcount == 1:
                if type == "grassland":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/grassland/juvham.html")
                    webbrowser.open(f"file://{file_path}")
                    gcount += 1
    if n >= 20 and n < 30:
        if (fwcount != 2) and (swcount != 2) and (fcount != 2) and (acount != 2) and (gcount != 2):
            print("")
        else:
            if fwcount == 2:
                if type == "freshwater":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/freshwater/adultsal.html")
                    webbrowser.open(f"file://{file_path}")
                    fwcount += 1
            if swcount == 2:
                if type == "saltwater":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/saltwater/adulthc.html")
                    webbrowser.open(f"file://{file_path}")
                    swcount += 1
            if fcount == 2:
                if type == "forest":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/forest/adultred.html")
                    webbrowser.open(f"file://{file_path}")
                    fcount += 1
            if acount == 2:
                if type == "arctic":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/arctic/adultseal.html")
                    webbrowser.open(f"file://{file_path}")
                    acount += 1
            if gcount == 2:
                if type == "grassland":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/grassland/adultham.html")
                    webbrowser.open(f"file://{file_path}")
                    gcount += 1
    if n >= 30 and n < 40:
        if (fwcount != 3) and (swcount != 3) and (fcount != 3) and (acount != 3) and (gcount != 3):
            print("")
        else:
            if fwcount == 3:
                if type == "freshwater":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/freshwater/babyax.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Axolotl, "
                    fwcount += 1
            if swcount == 3:
                if type == "saltwater":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/saltwater/babyturt.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Turtle, "
                    swcount += 1
            if fcount == 3:
                if type == "forest":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/forest/babybrown.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Brown Bear, "
                    fcount += 1
            if acount == 3:
                if type == "arctic":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/arctic/babypeng.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Penguin, "
                    acount += 1
            if gcount == 3:
                if type == "grassland":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/grassland/babymw.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Maned Wolf, "
                    gcount += 1
    if n >= 40 and n < 50:
        if (fwcount != 4) and (swcount != 4) and (fcount != 4) and (acount != 4) and (gcount != 4):
            print("")
        else:
            if fwcount == 4:
                if type == "freshwater":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/freshwater/juvax.html")
                    webbrowser.open(f"file://{file_path}")
                    fwcount += 1
            if swcount == 4:
                if type == "saltwater":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/saltwater/juvturt.html")
                    webbrowser.open(f"file://{file_path}")
                    swcount += 1
            if fcount == 4:
                if type == "forest":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/forest/juvbrown.html")
                    webbrowser.open(f"file://{file_path}")
                    fcount += 1
            if acount == 4:
                if type == "arctic":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/arctic/juvpeng.html")
                    webbrowser.open(f"file://{file_path}")
                    acount += 1
            if gcount == 4:
                if type == "grassland":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/grassland/juvmw.html")
                    webbrowser.open(f"file://{file_path}")
                    gcount += 1
    if n >= 50 and n < 60:
        if (fwcount != 5) and (swcount != 5) and (fcount != 5) and (acount != 5) and (gcount != 5):
            print("")
        else:
            if fwcount == 5:
                if type == "freshwater":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/freshwater/adultax.html")
                    webbrowser.open(f"file://{file_path}")
                    fwcount += 1
            if swcount == 5:
                if type == "saltwater":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/saltwater/adultturt.html")
                    webbrowser.open(f"file://{file_path}")
                    swcount += 1
            if fcount == 5:
                if type == "forest":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/forest/adultbrown.html")
                    webbrowser.open(f"file://{file_path}")
                    fcount += 1
            if acount == 5:
                if type == "arctic":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/arctic/adultpeng.html")
                    webbrowser.open(f"file://{file_path}")
                    acount += 1
            if gcount == 5:
                if type == "grassland":
                    print(f"Your {type} animal is all grown up!")
                    file_path = os.path.abspath("unlock html/grassland/adultmw.html")
                    webbrowser.open(f"file://{file_path}")
                    gcount += 1
    if n >= 60 and n < 70:
        if (fwcount != 6) and (swcount != 6) and (fcount != 6) and (acount != 6) and (gcount != 6):
            print("")
        else:
            if fwcount == 6:
                if type == "freshwater":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/freshwater/babydol.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Dolphin, "
                    fwcount += 1
            if swcount == 6:
                if type == "saltwater":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/saltwater/babywhale.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Whale, "
                    swcount += 1
            if fcount == 6:
                if type == "forest":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/forest/babyspec.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Spectacled Bear, "
                    fcount += 1
            if acount == 6:
                if type == "arctic":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/arctic/babypol.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Polar Bear, "
                    acount += 1
            if gcount == 6:
                if type == "grassland":
                    print(f"Unlocked a new {type} animal!")
                    file_path = os.path.abspath("unlock html/grassland/babyele.html")
                    webbrowser.open(f"file://{file_path}")
                    total += "Elephant, "
                    gcount += 1
    if n >= 70 and n < 80:
        if (fwcount != 7) and (swcount != 7) and (fcount != 7) and (acount != 7) and (gcount != 7):
            print("")
        else:
            if fwcount == 7:
                if type == "freshwater":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/freshwater/juvdol.html")
                    webbrowser.open(f"file://{file_path}")
                    fwcount += 1
            if swcount == 7:
                if type == "saltwater":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/saltwater/juvwhale.html")
                    webbrowser.open(f"file://{file_path}")
                    swcount += 1
            if fcount == 7:
                if type == "forest":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/forest/juvspec.html")
                    webbrowser.open(f"file://{file_path}")
                    fcount += 1
            if acount == 7:
                if type == "arctic":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/arctic/juvpol.html")
                    webbrowser.open(f"file://{file_path}")
                    acount += 1
            if gcount == 7:
                if type == "grassland":
                    print(f"Your {type} animal grew!")
                    file_path = os.path.abspath("unlock html/grassland/juvele.html")
                    webbrowser.open(f"file://{file_path}")
                    gcount += 1
    if n >= 80:
        if (fwcount != 8) and (swcount != 8) and (fcount != 8) and (acount != 8) and (gcount != 8):
            print("")
        else:
            if fwcount == 8:
                if type == "freshwater":
                    print(f"Your animal is all grown up! You unlocked all the {type} animals!")
                    file_path = os.path.abspath("unlock html/freshwater/adultdol.html")
                    webbrowser.open(f"file://{file_path}")
                    fwcount += 1
            if swcount == 8:
                if type == "saltwater":
                    print(f"Your animal is all grown up! You unlocked all the {type} animals!")
                    file_path = os.path.abspath("unlock html/saltwater/adultwhale.html")
                    webbrowser.open(f"file://{file_path}")
                    swcount += 1
            if fcount == 8:
                if type == "forest":
                    print(f"Your animal is all grown up! You unlocked all the {type} animals!")
                    file_path = os.path.abspath("unlock html/forest/adultspec.html")
                    webbrowser.open(f"file://{file_path}")
                    fcount += 1
            if acount == 8:
                if type == "arctic":
                    print(f"Your animal is all grown up! You unlocked all the {type} animals!")
                    file_path = os.path.abspath("unlock html/arctic/adultpol.html")
                    webbrowser.open(f"file://{file_path}")
                    acount += 1
            if gcount == 8:
                if type == "grassland":
                    print(f"Your animal is all grown up! You unlocked all the {type} animals!")
                    file_path = os.path.abspath("unlock html/grassland/adultele.html")
                    webbrowser.open(f"file://{file_path}")
                    gcount += 1

def logit(num,habitat):
    global type
    global fwpoints, swpoints, fpoints, apoints, gpoints
    global times
    times += 1
    type = habitat
    if habitat == "freshwater":
        fwpoints += num
        points(fwpoints)
    if habitat == "saltwater":
        swpoints += num
        points(swpoints)
    if habitat == "forest":
        fpoints += num
        points(fpoints)
    if habitat == "arctic":
        apoints += num
        points(apoints)
    if habitat == "grassland":
        gpoints += num
        points(gpoints)
    print(f"You contributed in bettering our environment! Gained {num} points!")

def menu():
    print("""How did you help the environment today?
    1) Saved Water
    2) Recycled
    3) Used Sustainable Transportation
    4) Planted vegetation
    5) Conserved Energy
    6) Purchased/Used Reusable Items
    7) Donated unwanted items
    8) Participated in Community Clean-up
    9) Wasted no food
    10) Shopped locally""")

def ilogit(activity, ways, num, animals):
    print(f"You chose '{activity}'")
    print(f"Some ways you can complete this activity are: {ways}")
    print(f"This activity is worth {num} points")
    print(f"Animals you can unlock from it: {animals}")


def anioptit(animal,activity1,activity2, status, relation):
    print(f"You chose {animal}!")
    print(f"Unlocked through the '{activity1}' and '{activity2}' activities")
    print(f"Animal status: {status}")
    print(f"Threats: {relation} ")

def viewit(animal,count):
    if (animal == "salmon") or (animal == "crab") or (animal == "seal") or (animal == "red panda") or (animal == "hamster"):
        if count == 0:
            print("You have not unlocked this animal yet :(")
        if count == 1:
            if animal == "salmon":
                file_path = os.path.abspath("view html/freshwater/viewbs.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "crab":
                file_path = os.path.abspath("view html/saltwater/viewbhc.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "seal":
                file_path = os.path.abspath("view html/arctic/viewb_s.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "red panda":
                file_path = os.path.abspath("view html/forest/viewbrp.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "hamster":
                file_path = os.path.abspath("view html/grassland/viewbh.html")
                webbrowser.open(f"file://{file_path}")
        if count == 2:
            if animal == "salmon":
                file_path = os.path.abspath("view html/freshwater/viewjs.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "crab":
                file_path = os.path.abspath("view html/saltwater/viewjhc.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "seal":
                file_path = os.path.abspath("view html/arctic/viewj_s.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "red panda":
                file_path = os.path.abspath("view html/forest/viewjrp.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "hamster":
                file_path = os.path.abspath("view html/grassland/viewjh.html")
                webbrowser.open(f"file://{file_path}")
        if count == 3:
            if animal == "salmon":
                file_path = os.path.abspath("view html/freshwater/viewas.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "crab":
                file_path = os.path.abspath("view html/saltwater/viewahc.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "seal":
                file_path = os.path.abspath("view html/arctic/viewa_s.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "red panda":
                file_path = os.path.abspath("view html/forest/viewarp.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "hamster":
                file_path = os.path.abspath("view html/grassland/viewah.html")
                webbrowser.open(f"file://{file_path}")
    if (animal == "axolotl") or (animal == "turtle") or (animal == "penguin") or (animal == "maned wolf") or (animal == "brown bear"):
        if count < 4:
            print("You have not unlocked this animal yet :(")
        if count == 4:
            if animal == "axolotl":
                file_path = os.path.abspath("view html/freshwater/viewba.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "turtle":
                file_path = os.path.abspath("view html/saltwater/viewbt.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "penguin":
                file_path = os.path.abspath("view html/arctic/viewb_p.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "brown bear":
                file_path = os.path.abspath("view html/forest/viewbbb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "maned wolf":
                file_path = os.path.abspath("view html/grassland/viewbmw.html")
                webbrowser.open(f"file://{file_path}")
        if count == 5:
            if animal == "axolotl":
                file_path = os.path.abspath("view html/freshwater/viewja.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "turtle":
                file_path = os.path.abspath("view html/saltwater/viewjt.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "penguin":
                file_path = os.path.abspath("view html/arctic/viewj_p.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "brown bear":
                file_path = os.path.abspath("view html/forest/viewjbb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "maned wolf":
                file_path = os.path.abspath("view html/grassland/viewjmw.html")
                webbrowser.open(f"file://{file_path}")
        if count == 6:
            if animal == "axolotl":
                file_path = os.path.abspath("view html/freshwater/viewaa.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "turtle":
                file_path = os.path.abspath("view html/saltwater/viewat.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "penguin":
                file_path = os.path.abspath("view html/arctic/viewa_p.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "brown bear":
                file_path = os.path.abspath("view html/forest/viewabb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "maned wolf":
                file_path = os.path.abspath("view html/grassland/viewamw.html")
                webbrowser.open(f"file://{file_path}")

    if (animal == "dolphin") or (animal == "whale") or (animal == "polar bear") or (animal == "elephant") or (animal == "spectacled bear"):
        if count < 7:
            print("You have not unlocked this animal yet :(")
        if count == 7:
            if animal == "dolphin":
                file_path = os.path.abspath("view html/freshwater/viewbd.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "whale":
                file_path = os.path.abspath("view html/saltwater/viewbw.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "polar bear":
                file_path = os.path.abspath("view html/arctic/viewb_pb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "spectacled bear":
                file_path = os.path.abspath("view html/forest/viewbsb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "elephant":
                file_path = os.path.abspath("view html/grassland/viewbe.html")
                webbrowser.open(f"file://{file_path}")
        if count == 8:
            if animal == "dolphin":
                file_path = os.path.abspath("view html/freshwater/viewjd.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "whale":
                file_path = os.path.abspath("view html/saltwater/viewjw.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "polar bear":
                file_path = os.path.abspath("view html/arctic/viewj_pb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "spectacled bear":
                file_path = os.path.abspath("view html/forest/viewjsb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "elephant":
                file_path = os.path.abspath("view html/grassland/viewje.html")
                webbrowser.open(f"file://{file_path}")
        if count == 9:
            if animal == "dolphin":
                file_path = os.path.abspath("view html/freshwater/viewad.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "whale":
                file_path = os.path.abspath("view html/saltwater/viewaw.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "polar bear":
                file_path = os.path.abspath("view html/arctic/viewa_pb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "spectacled bear":
                file_path = os.path.abspath("view html/forest/viewasb.html")
                webbrowser.open(f"file://{file_path}")
            if animal == "elephant":
                file_path = os.path.abspath("view html/grassland/viewae.html")
                webbrowser.open(f"file://{file_path}")
    else:
        print("Invalid input")


print("Welcome to EcoLog!")
while True:
    print("""What would you like to do?
    1) Log Activity
    2) Info
    3) My Animals
    4) Reset
    5) Exit""")

    opt = int(input("Choose an option: "))
    if (opt < 1) or (opt > 5):
        print("Invalid input. Please choose an option 1-4")
        continue
    if opt == 1:
        menu()
        log = int(input("Choose an option: "))
        if log == 1:
            logit(2,"freshwater")
        if log == 2:
            logit(1,"saltwater")
        if log == 3:
            logit(2,"arctic")
        if log == 4:
            logit(3,"grassland")
        if log == 5:
            logit(1,"arctic")
        if log == 6:
            logit(3,"saltwater")
        if log == 7:
            logit(2,"forest")
        if log == 8:
            logit(4, "grassland")
        if log == 9:
            logit(1,"forest")
        if log == 10:
            logit(2,"freshwater")
        if (log < 1) or (log > 10):
            print("Invalid input. Please choose an option 1-10.")
            continue

    if opt == 2:
        print("What would you like to know more about?")
        print("1) Activities")
        print("2) Animals")
        print("3) My Stats")
        iopt = int(input("Choose an option: "))
        if (iopt < 1) or (iopt > 3):
            print("Invalid input. Please choose an option 1-2.")
            continue
        if iopt == 1:
            menu()
            ilog = int(input("Choose an activity: "))
            if (ilog > 10) or (ilog < 1):
                print("Invalid input. Please choose an option 1-10")
            if ilog == 1:
                ilogit("Saved Water","taking shorter showers, turning off the sink when brushing your teeth, reusing water from indoors for plants, and running full loads of clothes/dish washers", 2, "Atlantic Salmon, Axolotl, River Dolphin")
            if ilog == 2:
                ilogit("Recycled","sorting paper, glass, and plastics into bins, reusing jars or containers, and dropping off electronics at e-waste recycling centers", 1, "Horseshoe Crab, Loggerhead Sea Turtle, North Atlantic Right Whale")
            if ilog == 3:
                ilogit("Used Sustainable Transportation", "walking to nearby places, riding a bike, taking the bus or train, or carpooling", 2, "Ringed Seal, Emperor Penguin, Polar Bear")
            if ilog == 4:
                ilogit("Planted Vegetation","starting a home garden, planting flowers that attract pollinators, joining a tree-planting project, or growing herbs in pots inside your home", 3, "European Hamster, Maned Wolf, Asian Elephant")
            if ilog == 5:
                ilogit("Conserved Energy","turning off lights when not in use, unplugging electronics, using energy-efficient bulbs, and letting sunlight warm or brighten your home instead of always using electricity", 1, "Ringed Seal, Emperor Penguin, Polar Bear")
            if ilog == 6:
                ilogit("Purchased/Used Reusable Items","using a refillable water bottle, bringing reusable bags to the store, using cloth napkins, and choosing washable containers instead of disposable ones", 3, "Horseshoe Crab, Loggerhead Sea Turtle, North Atlantic Right Whale")
            if ilog == 7:
                ilogit("Donated unwanted items","donate unwanted items are giving old clothes to a thrift store, donating books to a library or school, and dropping off furniture or toys at a local charity center", 2, "Red Panda, Himalayan Brown Bear, Spectacled Bear")
            if ilog == 8:
                ilogit("Participated in Community Clean-up","helping pick up trash at a local park, volunteering to clean a beach or riverbank, and joining neighborhood groups that organize litter collections", 4, "European Hamster, Maned Wolf, Asian Elephant")
            if ilog == 9:
                ilogit("Wasted no food","saving leftovers for another meal, planning meals ahead of time, freezing extra portions, and sharing extra food with friends, family, or food banks", 1, "Red Panda, Himalayan Brown Bear, Spectacled Bear")
            if ilog == 10:
                ilogit("Shopped locally","buying fruits and vegetables at a farmer’s market, supporting local bakeries or small shops, and choosing handmade goods from a local craftsperson", 2, "Atlantic Salmon, Axolotl, River Dolphin")
        if iopt == 2:
            print("""Animal List:
            1) Atlantic Salmon
            2) Axolotl
            3) River Dolphin
            4) Horseshoe Crab
            5) Loggerhead Sea Turtle
            6) North Atlantic Right Whale
            7) Ringed Seal
            8) Emperor Penguin
            9) Polar Bear
            10) European Hamster
            11) Maned Wolf
            12) Asian Elephant
            13) Red Panda
            14) Himalayan Brown Bear
            15) Spectacled Bear""")
            aniopt = int(input("Choose a number to learn more about the animal: "))
            if (aniopt > 15) or (aniopt < 1):
                print("Invalid input. Please choose an option 1-15")
                continue
            if aniopt == 1:
                anioptit("Atlantic Salmon","Saved Water", "Shopped Locally", "Endangered", "Climate change, Poor land use practices, Poor water quality, Dams")
            if aniopt == 2:
                anioptit("Axolotl","Saved Water", "Shopped Locally", "Critically Endangered", "Climate change, Exposure to air pollution, Polluted water, Invasive species ")
            if aniopt == 3:
                anioptit("River Dolphin","Saved Water", "Shopped Locally", "Endangered", "Industrial and human pollution, Exposure to toxic chemicals, Poaching/fishing")
            if aniopt == 4:
                anioptit("Horseshoe Crab","Recycled", "Purchased/Used Reusable Items", "Near Threatened", "Habitat loss due to tourism and infrastructure, Urban pollutants, Sand mining, Dams ")
            if aniopt == 5:
                anioptit("Loggerhead Sea Turtle","Recycled", "Purchased/Used Reusable Items", "Vulnerable", "Bycatch, Ocean Pollution")
            if aniopt == 6:
                anioptit("North Atlantic Right Whale","Recycled", "Purchased/Used Reusable Items", "Endangered", "Bycatch, Climate change, Few sources of food, Ocean noise pollution")
            if aniopt == 7:
                anioptit("Ringed Seal","Used Sustainable Transportation", "Conserved Energy", "Threatened", "Bycatch, Climate change, Ship traffic, Oil discharge")
            if aniopt == 8:
                anioptit("Emperor Penguin","Used Sustainable Transportation", "Conserved Energy", "Near Threatened", "Climate change, Few sources of food")
            if aniopt == 9:
                anioptit("Polar Bear","Used Sustainable Transportation", "Conserved Energy", "Vulnerable", "Habitat loss due to climate change")
            if aniopt == 10:
                anioptit("European Hamster","Planted Vegetation", "Participated in Community Clean-up", "Critically Endangered", "Monoculture, Poor food sources, Climate change, Light pollution")
            if aniopt == 11:
                anioptit("Maned Wolf","Planted Vegetation", "Participated in Community Clean-up", "Threatened", "Habitat loss due to agriculture and infrastructure, Hunting/poaching, Disease transmission")
            if aniopt == 12:
                anioptit("Asian Elephant","Planted Vegetation", "Participated in Community Clean-up", "Endangered", "Habitat loss due to human infrastructure, Fragmentation, Hunting/Poaching")
            if aniopt == 13:
                anioptit("Red Panda","Donated unwanted items", "Wasted no food", "Endangered", "Indiscriminate trapping, Habitat loss due to the clearing of forests")
            if aniopt == 14:
                anioptit("Himalayan Brown Bear","Donated unwanted items", "Wasted no food", "Critically Endangered", "Habitat loss, Poaching")
            if aniopt == 15:
                anioptit("Spectacled Bear","Donated unwanted items", "Wasted no food", "Vulnerable", "Habitat loss, Fragmentation, Hunting/poaching")
        if iopt == 3:
            print("Player Stats: ")
            print(f"In total you have earned {fwpoints+swpoints+fpoints+gpoints+apoints} points!")
            print(f"You have completed activities {times} times!")
            print(f"You have unlocked the: {total}")
    if opt == 4:
        print("""Animal Sets:
        1) Freshwater: Atlantic Salmon, Axolotl, River Dolphin
        2) Saltwater: Horseshoe Crab, Loggerhead Sea Turtle, North Atlantic Right Whale
        3) Arctic: Ringed Seal, Emperor Penguin, Polar Bear
        4) Grassland: European Hamster, Maned Wolf, Asian Elephant
        5) Forest: Red panda, Himalayan Brown Bear, Spectacled Bear
        """)
        set = int(input("Choose an animal set number to reset: "))
        if (set == 1) and (fwcount == 9):
            fwpoints = 0
            print("Freshwater points have been reset")
        elif (set == 2) and (swcount == 9):
            swpoints = 0
            print("Saltwater points have been reset")
        elif (set == 3) and (acount == 9):
            apoints = 0
            print("Arctic points have been reset")
        elif (set == 4) and (gcount == 9):
            print("Grassland points have been reset")
        elif (set == 5) and (fcount == 9):
            fpoints = 0
            print("Forest points have been reset")
        else:
            print("Set not fully unlocked yet. Cannot be reset.")
    if opt == 5:
        print("Thank you for using EcoLog! Goodbye.")
        break

    if opt ==3:
        if total == "":
            print("You haven't unlocked any animals yet :(")
            continue
        else:
            print(f"You've unlocked: {total}")
            view = input("What's the name of the animal you'd like to view: ")
            if view == "salmon" or (view == "Salmon") or (view == "SALMON"):
                viewit("salmon",fwcount)
            if view == "axolotl" or (view == "Axolotl") or (view == "AXOLOTL"):
                viewit("axolotl",fwcount)
            if view == "dolphin" or (view == "Dolphin") or (view == "DOLPHIN"):
                    viewit("dolphin", fwcount)
            if view == "crab" or (view == "Crab") or (view == "CRAB"):
                    viewit("crab", swcount)
            if view == "turtle" or (view == "Turtle") or (view == "TURTLE"):
                    viewit("turtle", swcount)
            if view == "whale" or (view == "Whale") or (view == "WHALE"):
                    viewit("turtle", swcount)
            if view == "red panda" or (view == "Red panda") or (view == "RED PANDA") or (view == "Red Panda"):
                    viewit("red panda", fcount)
            if view == "brown bear" or (view == "Brown bear") or (view == "BROWN BEAR") or (view == "Brown Bear"):
                    viewit("brown bear", fcount)
            if view == "spectacled bear" or (view == "Spectacled bear") or (view == "SPECTACLED BEAR") or (view == "Spectacled Bear"):
                viewit("spectacled bear", fcount)
            if view == "seal" or (view == "Seal") or (view == "SEAL"):
                viewit("seal", acount)
            if view == "penguin" or (view == "Penguin") or (view == "PENGUIN"):
                viewit("penguin", acount)
            if view == "polar bear" or (view == "Polar bear") or (view == "POLAR BEAR") or (view == "Polar Bear"):
                viewit("polar bear", acount)
            if view == "hamster" or (view == "hamster") or (view == "HAMSTER"):
                    viewit("hamster", gcount)
            if view == "maned wolf" or (view == "Maned wolf") or (view == "MANED WOLF") or (view == "Maned Wolf"):
                    viewit("maned wolf", gcount)
            if view == "elephant" or (view == "Elephant") or (view == "ELEPHANT"):
                    viewit("elephant", gcount)
            else:
                print("Invalid input")
                continue










