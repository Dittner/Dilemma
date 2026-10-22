from dilemma.lemmatizer import lemmatize

if __name__ == '__main__':
    """
    E.g.
    missing -> ['miss', 'missing']
    lazy -> ['lazy']
    buries -> ['bury']
    best -> ['good', 'best']
    criteria -> ['criterion']
    understood -> ['understand']
    algae -> ['alga', 'algae']

    The word "missing" can be the gerund form of the verb "miss"
    or it can be the verb "sing" with the prefix "mis-".
    """

    # examples2 = ['misunderstand']
    # for e in examples2:
    #     res = get_past_and_perfect_form(e)
    #     if res is not None:
    #         print(f'{e} -> {res[0], res[1]}')

    examples = ['missing', 'lazy', 'buries', 'best', 'criteria', 'understood', 'algae']
    for e in examples:
        res = lemmatize(e)
        print(f'{e} -> {res}')
