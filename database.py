import pickle

file = "children.db"

def dbLoad():
    children_dict = pickle.load(open(file, "rb"))
    return children_dict

def dbSave(children_dict):
    pickle.dump(children_dict, open(file, "wb"))