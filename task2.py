import functools

SPELL_BOOK = {"fe":1, "je":2, "jee":3, "ain":3, "dai":5, "ne":2, "ai":2 }



def damage(spell):
    def custom_comparator(x, y):
        if SPELL_BOOK[x] < SPELL_BOOK[y]:
            return 1
        else:
            return -1

    sorted_keys = list(SPELL_BOOK.keys())
    sorted_keys.sort(key=functools.cmp_to_key(custom_comparator))
    print(sorted_keys)

    dmg = 0
    for key in sorted_keys:
        index = spell.find(key)
        while index >= 0:
            to_print = "subspell: " + spell[index:index+len(key)]
            to_print += " before: " + spell
            spell = spell[:index] + spell[index+len(key):]
            print(to_print + " after: " + spell)
            dmg += SPELL_BOOK[key]
            index = spell.find(key)
    return dmg

print(damage("fejee"))