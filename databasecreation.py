import pickle

file = "resources/leaderboard.db"

def dbLoad():
    leaderboard = pickle.load(open(file, "rb"))
    return leaderboard

def dbSave(x):
    pickle.dump(x, open(file, "wb"))

leaderboard = {"Lachlan":8, "Roderick":7, "Johno":2, "Jeff":8, "Tim":5}
print(leaderboard)

t = input()

if t == "read":
    for i in leaderboard:
        print(i)

    res = list(sorted(leaderboard, key=leaderboard.__getitem__, reverse=True))
    print(res)

elif t == "save":
    dbSave(leaderboard)
    print("Done")
