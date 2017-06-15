import functools

SPELL_BOOK = {"fe":1, "je":2, "jee":3, "ain":3, "dai":5, "ne":2, "ai":2 }

def custom_comparator(x, y):
    if SPELL_BOOK[x] < SPELL_BOOK[y]:
        return 1
    else:
        return -1

sorted_keys = list(SPELL_BOOK.keys())
sorted_keys.sort(key=functools.cmp_to_key(custom_comparator))

def is_correct(spell):
    start = spell.find("fe")
    stop = spell.find("ai")
    return start >=0 and stop >= 0 and start < stop

def trim(spell):
    start = spell.find("fe")
    stop = spell.find("ai")
    return spell[start + 2: stop]


def damage(spell):

    if is_correct(spell):
        spell = trim(spell)
    else:
        return -1

    dmg = 0
    for key in sorted_keys:
        index = spell.find(key)
        while index >= 0:
            #to_print = "subspell: " + spell[index:index+len(key)]
            #to_print += " before: " + spell
            spell = spell[:index] + spell[index+len(key):]
            #print(to_print + " after: " + spell)
            dmg += SPELL_BOOK[key]
            index = spell.find(key)
    return dmg