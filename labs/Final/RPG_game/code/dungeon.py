import random

def generate_room():
    return random.choice(["battle", "chest", "rest"])

def room_name(room_type):
    names = {"battle": "Бой", "chest": "Сундук", "rest": "Отдых"}
    return names.get(room_type, "???")