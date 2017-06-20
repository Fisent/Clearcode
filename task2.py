import functools

SPELL_BOOK = {"fe":1, "je":2, "jee":3, "ain":3, "dai":5, "ne":2, "ai":2 }

'''
def custom_comparator(x, y):
    if SPELL_BOOK[x] > SPELL_BOOK[y]:
        return 1
    else:
        return -1
'''

def custom_comparator(x,y):
    if len(x) < len(y):
        if SPELL_BOOK[x] < SPELL_BOOK[y]:
            return 1
        else:
            return -1
    else:
        return -1

def custom_comparator2(x,y):
    if len(x) > len(y):
        if SPELL_BOOK[x] < SPELL_BOOK[y]:
            return 1
        else:
            return -1
    else:
        return -1

sorted_keys = list(SPELL_BOOK.keys())
sorted_keys.sort(key=functools.cmp_to_key(custom_comparator))
print(sorted_keys)

def is_correct(spell):
    start = spell.find("fe")
    stop = spell.rfind("ai")
    return start >=0 and stop >= 0 and start < stop

def find_subspells(spell):
    out = list()
    for subspell in SPELL_BOOK:
        while subspell in spell:
            out.append(subspell)
            index = spell.find(subspell)
            spell = spell[:index] + spell[index+len(subspell):]
    return out

def trim(spell):
    start = spell.find("fe")
    stop = spell.rfind("ai")
    return spell[start + 2: stop]


def damage_inner(spell):
    if is_correct(spell):
        spell = trim(spell)
    else:
        return 0

    dmg = 3
    for key in sorted_keys:
        index = spell.find(key)
        while index >= 0:
            spell = spell[:index] + spell[index+len(key):]
            dmg += SPELL_BOOK[key]
            index = spell.find(key)
    return max(dmg -len(spell), 0)

def damage(spell):
    dmg1 = damage_inner(spell)
    sorted_keys.sort(key=functools.cmp_to_key(custom_comparator2))
    dmg2 = damage_inner(spell)
    return max(dmg1, dmg2)