from random import choice

FIRST = [
    "Attractive", "Bald", "Beautiful", "Chubby", "Clean",
    "Dazzling", "Drab", "Elegant", "Fancy", "Fit",
    "Flabby", "Glamorous", "Gorgeous", "Handsome", "Magnificent",
    "Muscular", "Plain", "Plump", "Skinny", "Stocky",
    "Unkempt", "Unsightly", "Agreeable", "Ambitious", "Brave",
    "Calm", "Delightful", "Eager", "Faithful", "Gentle",
    "Happy", "Jolly", "Kind", "Lively", "Nice",
    "Obedient", "Polite", "Proud", "Silly", "Thankful",
    "Victorious", "Witty", "Wonderful", "Zealous", "Modest",
    "Crazy", "Stupid", "Awesome", "Brilliant", "Amazing",
]

SECOND = [
    "Angry", "Bewildered", "Clumsy", "Defeated", "Embarassed",
    "Fierce", "Grumpy", "Helpless", "Itchy", "Jealous",
    "Lazy", "Mysterious", "Nervous", "Obnoxious", "Panicky",
    "Pitiful", "Repulsive", "Scary", "Thoughtless", "Uptight",
    "Worried", "Big", "Colossal", "Fat", "Gigantic",
    "Great", "Huge", "Immense", "Large", "Little",
    "Mammoth", "Massive", "Microscopic", "Miniature", "Petite",
    "Puny", "Scrawny", "Short", "Small", "Tall",
    "Teeny", "Tiny", "Dreadful", "Ugly", "Spooky",
    "Helpful", "Holographic", "Expressive", "Sharp", "Precise",
]

THIRD = [
    "People", "Family", "Government", "System", "Computers",
    "Music", "Person", "Methods", "Data", "Food",
    "Theory", "Laws", "Birds", "Problems", "Power",
    "Knowledge", "Ability", "Love", "Internet", "Science",
    "Nature", "Ideas", "Players", "Army", "Children",
    "Kids", "Monsters", "Ghosts", "Bandits", "Killers",
    "Burglars", "Villains", "Demons", "Scammers", "Workers",
    "Murderers", "Fighters", "Gamblers", "Musicians", "Painters",
    "Artists", "Architects", "Engineers", "Spies", "Soldiers",
    "Medics", "Sisters", "Brothers", "Firefighters", "Maniacs",
]


def get_title_list(n):
    titles = []
    for _ in range(n):
        title = choice(FIRST) + " " + choice(SECOND) + " " + choice(THIRD)
        titles.append(title)
    return titles
