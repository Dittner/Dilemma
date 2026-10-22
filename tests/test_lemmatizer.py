from dilemma.lemmatizer import lemmatize, get_past_and_perfect_form


def test_empty_input():
    assert len(lemmatize('')) == 0
    
    
def test_reg_verbs():
    vv = [
        ('accept', 'accepts|accepted|accepting'), 
        ('plus', 'pluses|plused|plusing'), 
        ('miss', 'misses|missed|missing'),
        ('bake', 'bakes|baked|baking'), 
        ('behave', 'behaves|behaved|behaving'),
        ('close', 'closes|closed|closing'),
        ('compete', 'competes|competed|competing'),
        ('die', 'dies|died|dying'),
        ('borrow', 'borrows|borrowed|borrowing'),
        ('bury', 'buries|buried|burying'),
        ('cry', 'cries|cried|crying'),
        ('complain', 'complains|complained|complaining'),
        ('hate', 'hates|hated|hating'),
        ('play', 'plays|played|playing'),
        ('type', 'types|typed|typing'),
        ('yell', 'yells|yelled|yelling'),
        ('move', 'moves|moved|moving'),
        ('stop', 'stops|stopped|stopping'),
        ('box', 'boxes|boxed|boxing'),
        ('wash', 'washes|washed|washing'),
        ('wait', 'waits|waited|waiting'),
        ('finish', 'finishes|finished|finishing'),
    ]

    for inf, forms in vv:
        assert inf in lemmatize(inf)
        forms = forms.split('|')
        for form in forms:
            assert inf in lemmatize(form)

def test_irreg_verbs():
    vv = [
        ('be', 'is|are|was|were|been'),
        ('do', 'does|done|doing'),
        ('go', 'goes|gone|going'), 
        ('undereat', 'underate|undereaten'), 
        ('rebuild', 'rebuilds|rebuilt|rebuilding'),
        ('sunburn', 'sunburns|sunburnt|sunburning'),
        ('radiobroadcast', 'radiobroadcasts|radiobroadcast|radiobroadcasting'),
        ('mischoose', 'mischooses|mischose|mischoosing'),
        ('lie', 'lain|lying'),
        ('prepay', 'prepaid|prepaying'),
        ('ring', 'rung|ringing'),
        ('arise', 'arose|arisen|arising'),
        ('foresee', 'foresees|foresaw|foreseen|foreseeing'),
        ('outseek', 'outseeks|outsought|outseeking'),
        ('shed', 'shed|sheding'),
        ('overshoot', 'overshot|overshooting'),
        ('shrive', 'shriven'),
        ('outsit', 'outsits|outsat|outsitting'),
        ('widespread', 'widespreads|widespreading'),
        ('misunderstand', 'misunderstands|misunderstood'),
        ('outswim', 'outswam|outswum'),
        ('downthrow', 'downthrew|downthrown'),
        ('reawake', 'reawoke|reawoken'),
        ('handwrite', 'handwrote|handwritten|handwriting'),
    ]

    for inf, forms in vv:
        assert inf in lemmatize(inf)
        forms = forms.split('|')
        for form in forms:
            assert inf in lemmatize(form)

def test_irreg_verb_forms():
    vv = [
        ('be', 'was', 'been'),
        ('be', 'were', 'been'),
        ('do', 'did', 'done'),
        ('go', 'went' ,'gone'), 
        ('have', 'had', 'had'), 
        ('rebuild', 'rebuilt', 'rebuilt'),
        ('sunburn', 'sunburnt', 'sunburnt'),
        ('radiobroadcast', 'radiobroadcast', 'radiobroadcast'),
        ('mischoose', 'mischose', 'mischosen'),
        ('lie', 'lied', 'lied'),
        ('lie', 'lay', 'lain'),
        ('prepay', 'prepaid', 'prepaid'),
        ('ring', 'ran', 'rung'),
        ('arise', 'arose', 'arisen'),
        ('foresee', 'foresaw' ,'foreseen'),
        ('outseek', 'outsought', 'outsought'),
        ('shed', 'shed', 'shed'),
        ('overshoot', 'overshot', 'overshot'),
        ('shrive', 'shrove', 'shriven'),
        ('outsit', 'outsat', 'outsat'),
        ('misunderstand', 'misunderstood', 'misunderstood'),
        ('outswim', 'outswam', 'outswum'),
        ('downthrow', 'downthrew', 'downthrown'),
        ('reawake', 'reawoke', 'reawoken'),
        ('handwrite', 'handwrote', 'handwritten'),
    ]

    for inf, past, perfect in vv:
        res = get_past_and_perfect_form(inf)

        assert res is not None

        res_past, res_perfect = res
        assert past in res_past.split('/')
        assert perfect in res_perfect.split('/')


def test_plural_nouns():
    nouns = [
        ('phenomenon', 'phenomena'),
        ('memorandum', 'memoranda'),
        ('match', 'matches'),
        ('plumpness', 'plumpnesses'),
        ('outbox', 'outboxes'),
        ('factory', 'factories'),
        ('vertex', 'vertices'),
        ('index', 'indices'),
        ('matrix', 'matrices'),
        ('criterion', 'criteria'),
        ('louse', 'lice'),
        ('knife', 'knives'),
        ('half', 'halves'),
        ('potato', 'potatoes'),
        ('photo', 'photos'),
        ('policewoman', 'policewomen'),
        ('godchild', 'godchildren'),
        ('foot', 'feet'),
        ('tooth', 'teeth'),
        ('sawtooth', 'sawteeth'),
        ('algae', 'algae'),
        ('alga', 'algae'),
        ('halobacteria', 'halobacteria'),
        ('halobacterium', 'halobacteria'),
        ('house', 'houses'),
        ('species', 'species'),
        ('jeans', 'jeans'),
    ]

    for sg, pl in nouns:
        assert sg in lemmatize(sg)
        assert sg in lemmatize(pl)

def test_comparative_adjectives():
    aa = [
        ('large', 'larger'),
        ('fine', 'finer'),
        ('thin', 'thinner'),
        ('lazy', 'lazier'),
        ('tall', 'taller'),
        ('high', 'higher'),
        ('smart', 'smarter'),
        ('far', 'farther'),
        ('far', 'further'),
        ('many', 'more'),
        ('old', 'elder'),
    ]

    for adj, comp in aa:
        assert adj in lemmatize(adj)
        assert adj in lemmatize(comp)

def test_superlative_adjectives():
    aa = [
        ('thin', 'thinnest'),
        ('good', 'best'),
        ('bad', 'worst'),
        ('little', 'least'),
        ('thin', 'thinnest'),
        ('lazy', 'laziest'),
        ('tall', 'tallest'),
        ('high', 'highest'),
        ('smart', 'smartest'),
        ('far', 'farthest'),
        ('far', 'furthest'),
        ('many', 'most'),
        ('old', 'eldest'),
        ('old', 'oldest'),
    ]

    for adj, sup in aa:
        assert adj in lemmatize(adj)
        assert adj in lemmatize(sup)

def test_conjunctions_and_prepositions():
    ww = ['a','although','an','and','at','because','beside','case','for','from','how','if','into','neither','yes','no','not','nor','of','or','per','since','than','that','the','till','to','toward','towards','unless','until','upon','versus','via','what','when','whenever','whereas','whether','while','with','without','worth']
    for w in ww:
        assert w in lemmatize(w)

def test_numbers():
    ww = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'hundred', 'thousand', 'million', 'billion', 'trillion']
    for w in ww:
        assert w in lemmatize(w)