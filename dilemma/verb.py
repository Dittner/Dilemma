import re
from pathlib import Path

from dilemma.corpus import Corpus

irregular_verbs = [
    ('be', 'is|are|was|were|been', ''),
    ('bear', 'bore|born|borne', 'for|out|over|un|under|up|water'),
    ('beat', 'beaten', 'brow|under'),
    ('beget', 'begot|begotten', 'mis|un'),
    ('begin', 'began|begun', 'mis'),
    ('bend', 'bent', 'down|out|re|un'),
    ('bid', 'bade|bidden', 'counter|her|out|over|pre|re|un|under|up|ver'),
    ('bind', 'bound', 'dis|em|hide|mis|pre|re|spell|un|under|up|wood'),
    ('bite', 'bit|bitten', 'back|flea|frost|over|under'),
    ('bleed', 'bled', 'be|out'),
    ('blow', 'blew|blown', 'fly|in|out|over|re'),
    ('break', 'broke|broken', 'heart|house|up'),
    ('breed', 'bred', 'cross|in|inter|line|out|over|re|up'),
    ('bring', 'brought', 'forth|in|out|up'),
    ('build', 'built', 'mis|out|over|re|un|under|up'),
    ('burn', 'burnt', 'mow|out|over|sun|un|under|wind'),
    ('burst', '', 'in|out|over|re|un|up'),
    ('buy', 'bought', 'over|re|under'),
    ('can', 'could', ''),
    (
        'cast',
        '',
        'after|back|broad|down|endo|fore|forn|hind|in|mis|multi|off|open|out|over|pre|radio|radiobroad|re|rebroad|refore|sub|tele|top|type|umbe|un|unbroad|under|unfore|up|video',
    ),
    ('catch', 'caught', 'out|up'),
    ('choose', 'chose|chosen', 'mis|pre|re'),
    ('cleave', 'clove|cloven|cleft', 'un'),
    ('cling', 'clung', ''),
    ('come', 'came', 'after|be|forth|misbe|out|over'),
    ('cost', '', 'after|be|dis|on|re|un'),
    ('creep', 'crept', 'in|out'),
    (
        'cut',
        '',
        'be|cross|down|draw|for|forth|in|inter|mis|off|open|out|over|pre|re|reunder|un|under|up|upper',
    ),
    ('deal', 'dealt', 'mis|re'),
    ('dig', 'dug', 'un|under'),
    ('do', 'did|done', 'for|fore|mis|out|over|re|spa|un|under'),
    ('draw', 'drew|drawn', 'mis|out|over|pre|re|sneck|un|under|wire|with'),
    ('dream', 'dreamt', 'out|re'),
    ('drink', 'drank|drunk', 'out|over'),
    ('drive', 'drove|driven', 'co|mis|out|over|pre|re|under'),
    ('dwell', 'dwelt', 'in|out'),
    ('eat', 'ate|eaten', 'out|over|under'),
    ('fall', 'fell|fallen', 'be|down|misbe|over|re'),
    ('feed', 'fed', 'out|over|re|spoon|un|under'),
    ('feel', 'felt', 'fore|out|re|un|under'),
    ('fight', 'fought', 'in|out|re|un'),
    ('find', 'found', 'out|re'),
    ('flee', 'fled', 'out'),
    ('fling', 'flung', 'out|up'),
    ('fly', 'flew|flown', 'out|over|re'),
    ('forbid', 'forbade|forbad|forbidden', 'un'),
    ('forget', 'forgot|forgotten', 'un'),
    ('forsake', 'forsook|forsaken', ''),
    ('freeze', 'froze|frozen', 'ad|pre|re|un'),
    ('get', 'got', 'over|un'),
    ('give', 'gave|given', 'for|mis|out|prefor|re|un'),
    ('go', 'went|gone', 'for|fore|out|over|under'),
    ('grind', 'ground', 'over|re'),
    ('grow', 'grew|grown', 'for|in|inter|mis|out|over|re|un|under|up'),
    ('hang', 'hung', 'be|over|re|un|under|up'),
    ('have', 'had', 'un'),
    ('hear', 'heard', 'mis|out|over|re'),
    ('hide', 'hid|hidden', 're|un'),
    ('hit', '', 'mis|out|over|un'),
    ('hold', 'held', 'be|over|un|up|with'),
    ('hurt', '', 'un'),
    ('keep', 'kept', 'house|mis|out'),
    ('kneel', 'knelt', ''),
    ('know', 'knew|known', 'ac|be|fore|mis|pre|un'),
    ('lay', 'laid', 'in|inter|mis|on|out|over|un|under|up|way'),
    ('lead', 'led', 'co|mis|out|un'),
    ('leave', 'left', 'be|for|un'),
    ('lend', 'lent', 'over|re'),
    ('let', '', 'sub|un|under'),
    ('lie', 'lied|lain', ''),
    ('light', 'lit', 'mis|over|re|un|under|up'),
    ('lose', 'lost', 're'),
    ('make', 'made', 'co|mis|pre|re|trans|un'),
    ('may', 'might', ''),
    ('mean', 'meant', ''),
    ('meet', 'met', 'inter|mis|re|un'),
    ('mow', 'mowed|mown', ''),
    ('pay', 'paid', 'mis|over|pre|re|un|under'),
    ('put', '', 'in|mis|out|over|reout|through|thru|trans|un|under'),
    ('read', '', 'mis|out|over|proof|re|un|under|unproof'),
    ('rend', 'rent', ''),
    ('rid', '', ''),
    ('ride', 'rode|ridden', 'out|over|un'),
    ('ring', 'rang|rung', 'out|un'),
    ('rise', 'rose|risen', 'a|over|re|rea|up'),
    ('run', 'ran', 'fore|in|inter|long|mis|out|over|press|re|un|under|up'),
    ('say', 'said', 'fore|mis|out|over|pre|re|un'),
    ('see', 'saw|seen', 'be|for|fore|out|over|pre|sight|un|under|unfore'),
    ('seek', 'sought', 'be|out|re'),
    ('sell', 'sold', 'out|over|pre|re|un|under'),
    ('send', 'sent', 'god|mis|re|up'),
    (
        'set',
        '',
        'down|for|fore|forth|in|inter|mis|off|on|out|over|pre|re|reoff|sub|um|umbe|un|unbe|under|unoff|unup|up|ver',
    ),
    ('sew', 'sewed|sewn', 'hand|over|re|un'),
    ('shake', 'shook|shaken', 're'),
    ('shed', 'shed', ''),
    ('shine', 'shone', 'out|over|re|under'),
    ('shoe', 'shod', 're|slip|un'),
    ('shoot', 'shot', 'inter|out|over|pot|re|snap|trouble|under|up'),
    ('shrink', 'shrank|shrunk', 'pre|un'),
    ('shrive', 'shrove|shriven', ''),
    ('shut', '', 'out|re|un|under|up'),
    ('sing', 'sang|sung', 'mis|out|un'),
    ('sink', 'sank', 'counter'),
    ('sit', 'sat', 'out|re'),
    ('slay', 'slew|slain', ''),
    ('sleep', 'slept', 'out|over|under'),
    ('slide', 'slid', 'back|land|out|over'),
    ('sling', 'slung', 'un'),
    ('slink', 'slunk', ''),
    ('slit', '', 'un'),
    ('smell', 'smelt', 're'),
    ('smite', 'smote|smitten', 'over'),
    ('sow', 'sowed|sown', 'over|re'),
    ('speak', 'spoke|spoken', 'be|for|fore|in|mis|out|over|re|un|unbe'),
    ('speed', 'sped', 'be|out|un'),
    ('spell', 'spelt', 'mis|out|re|un'),
    ('spend', 'spent', 'for|mis|out|over|under'),
    ('spill', 'spilt', 'over'),
    ('spin', 'spun', 'over|un'),
    ('spit', 'spat', 'out'),
    ('split', '', 'be|pre|re|un'),
    ('spoil', 'spoilt', 'un'),
    ('spread', '', 'back|be|broad|di|dis|for|out|over|pre|re|un|under|up|wide|wing'),
    ('spring', 'sprang|sprung', 'over|re|un|up'),
    ('stand', 'stood', 'misunder|out|over|preunder|under|up|with'),
    ('stave', 'stove', ''),
    ('steal', 'stole|stolen', 'out'),
    ('stick', 'stuck', 'be|un'),
    ('sting', 'stung', 'out|re|un'),
    ('stink', 'stank', 'out'),
    ('stride', 'strode|stridden', 'be|out|over'),
    ('strike', 'struck', 'out|over|re|un|under'),
    ('string', 'strung', 'bow|ham|over|re|un|under'),
    ('strive', 'strove|striven', 'inter|out|over|re'),
    ('sweep', 'swept', 're|under|up'),
    ('swell', 'swelled', 'over|un|up'),
    ('swim', 'swam|swum', 'out'),
    ('swing', 'swung', 'out|un|up'),
    ('take', 'took|taken', 'be|care|mis|out|over|par|prepar|preunder|re|under'),
    ('teach', 'taught', 'mis|over|pre|re|un|under'),
    ('tear', 'tore|torn', 'out|re|up'),
    ('tell', 'told', 'fore|mis|out|over|pre|re|s|un'),
    ('think', 'thought', 'be|for|fore|mis|out|over|re|un|unbe|under'),
    ('thrive', 'throve', ''),
    ('throw', 'threw|thrown', 'down|mis|out|over|preover|up'),
    ('thrust', '', 'counter|down|in|out|over|pre|re|un|under|up'),
    ('tread', 'trod|trodden', 'over|re|un|under'),
    ('wake', 'woke|woken', 'a|re|rea'),
    ('wear', 'wore|worn', 'foot|for|fores|fors|out|outs|over|s|uns'),
    ('weave', 'wove|woven', 'en|in|inter|out|over|re|un'),
    ('weep', 'wept', 'be|out'),
    ('wet', '', 'be|over|re|un'),
    ('win', 'won', 'over|re'),
    ('wind', 'wound', 'in|inter|over|re|un|under|up'),
    ('wring', 'wrung', 'out'),
    ('write', 'wrote|written', 'ghost|hand|mis|out|over|re|type|un|under'),
]


class VerbLemmatizer:
    def __init__(self) -> None:
        path = Path(__file__).resolve().parent / 'data/verbs.txt'
        self.corpus = Corpus(path)
        self.patterns = self._init_patterns()
        self.irr_verbs: dict[str, str] = self._init_irr_verbs()
        self.past_perfect: dict[str, tuple[str, str]] = self._init_irr_verb_forms()

    def _init_patterns(self):
        return [
            # present
            (r'^([a-zA-Z]+)ies$', lambda res: res + 'y'),  # buries -> bury
            (r'^([a-zA-Z]+(sh|ch|x|s|o))es$', lambda res: res[0]),  # goes -> go, watches -> watch
            (r'^([a-zA-Z]+[^s])s$', None),  # miss -> miss, moves -> move
            # past
            (r'^([a-zA-Z]+)ied$', lambda res: res + 'y'),  # studied -> study
            (r'^([a-zA-Z]+(bb|dd|ff|gg|mm|nn|pp|rr|tt|ll))ed$', lambda res: res[0][:-1]),  # stopped -> stop
            (r'^([a-zA-Z]+e)d$', None),  # moved -> move
            (r'^([a-zA-Z]+)ed$', None),  # worked -> work
            # gerund
            (r'^([a-zA-Z]+)ying$', lambda res: res + 'ie'),  # dying -> die
            (r'^([a-zA-Z]+(bb|dd|ff|gg|mm|nn|pp|rr|tt|ll))ing$', lambda res: res[0][:-1]),  # sitting -> sit
            (r'^([a-zA-Z]+)ing$', lambda res: res + 'e'),  # writing -> write
            (r'^([a-zA-Z]+)ing$', None),  # playing -> play, reading -> read
        ]

    def _init_irr_verbs(self):
        res = {}
        for verb, forms, prefixes in irregular_verbs:
            ff = forms.split('|')
            ff.append(verb)
            pp = prefixes.split('|')
            for f in ff:
                if f == '':
                    continue
                res[f] = verb
                for p in pp:
                    if p == '':
                        continue
                    if res.get(p + f):
                        raise ValueError('Duplicated key=' + (p + f))

                    res[p + f] = p + verb
        return res

    def _init_irr_verb_forms(self) -> dict[str, tuple[str, str]]:
        res = {}
        # ('wake', 'woke/waked', 'woken/waked', 'a|re|rea')
        for inf, past, perfect, prefixes in irregular_verb_forms:
            pasts = past.split('/')
            perfects = perfect.split('/')
            res[inf] = (past, perfect)
            for prefix in prefixes.split('|'):
                if prefix == '':
                    continue

                if res.get(prefix + inf) is not None:
                    raise ValueError('Duplicated key=' + (prefix + inf))

                res[prefix + inf] = (
                    '/'.join([prefix + past for past in pasts if past != '']),
                    '/'.join([prefix + perfect for perfect in perfects if perfect != '']),
                )
        return res

    def find(self, word: str) -> list[str]:
        res = []
        if self.corpus.has(word):
            res.append(word)

        for pattern, post_handler in self.patterns:
            matches = re.findall(pattern, word)
            if len(matches) > 0:
                m = matches[0]
                if post_handler:
                    m = post_handler(m)
                if self.corpus.has(m):
                    res.append(m)

        irr_verb = self.irr_verbs.get(word)
        if irr_verb:
            res.append(irr_verb)

        return res

    def get_past_and_perfect_form(self, verb: str) -> tuple[str, str] | None:
        return self.past_perfect.get(verb)


# inf, past, perfect, prefixes
irregular_verb_forms = [
    ('be', 'was/were', 'been', ''),
    ('bear', 'bore', 'born/borne', 'for|out|over|un|under|up|water'),
    ('beat', 'beat', 'beaten', 'brow|under'),
    ('beget', 'begot', 'begotten', 'mis|un'),
    ('begin', 'began', 'begun', 'mis'),
    ('bend', 'bent', 'bent', 'down|out|re|un'),
    ('bid', 'bid/bade', 'bid/bidden', 'counter|her|out|over|pre|re|un|under|up|ver'),
    ('bind', 'bound', 'bound', 'dis|em|hide|mis|pre|re|spell|un|under|up|wood'),
    ('bite', 'bit', 'bitten', 'back|flea|frost|over|under'),
    ('bleed', 'bled', 'bled', 'be|out'),
    ('blow', 'blew', 'blown', 'fly|in|out|over|re'),
    ('break', 'broke', 'broken', 'heart|house|up'),
    ('breed', 'bred', 'bred', 'cross|in|inter|line|out|over|re|up'),
    ('bring', 'brought', 'brought', 'forth|in|out|up'),
    ('build', 'built', 'built', 'mis|out|over|re|un|under|up'),
    ('burn', 'burnt/burned', 'burnt/burned', 'mow|out|over|sun|un|under|wind'),
    ('burst', 'burst', 'burst', 'in|out|over|re|un|up'),
    ('buy', 'bought', 'bought', 'over|re|under'),
    ('can', 'could', 'could', ''),
    (
        'cast',
        'cast',
        'cast',
        'after|back|broad|down|endo|fore|forn|hind|in|mis|multi|off|open|out|over|pre|radio|radiobroad|re|rebroad|refore|sub|tele|top|type|umbe|un|unbroad|under|unfore|up|video',
    ),
    ('catch', 'caught', 'caught', 'out|up'),
    ('choose', 'chose', 'chosen', 'mis|pre|re'),
    ('cleave', 'clove/cleft', 'cloven/cleft', 'un'),
    ('cling', 'clung', 'clung', ''),
    ('come', 'came', 'come', 'after|be|forth|misbe|out|over'),
    ('cost', 'cost', 'cost', 'after|be|dis|on|re|un'),
    ('creep', 'crept', 'crept', 'in|out'),
    (
        'cut',
        'cut',
        'cut',
        'be|cross|down|draw|for|forth|in|inter|mis|off|open|out|over|pre|re|reunder|un|under|up|upper',
    ),
    ('deal', 'dealt', 'dealt', 'mis|re'),
    ('dig', 'dug', 'dug', 'un|under'),
    ('do', 'did', 'done', 'for|fore|mis|out|over|re|spa|un|under'),
    ('draw', 'drew', 'drawn', 'mis|out|over|pre|re|sneck|un|under|wire|with'),
    ('dream', 'dreamt/dreamed', 'dreamt/dreamed', 'out|re'),
    ('drink', 'drank', 'drunk', 'out|over'),
    ('drive', 'drove', 'driven', 'co|mis|out|over|pre|re|under'),
    ('dwell', 'dwelt/dwelled', 'dwelt/dwelled', 'in|out'),
    ('eat', 'ate', 'eaten', 'out|over|under'),
    ('fall', 'fell', 'fallen', 'be|down|misbe|over|re'),
    ('feed', 'fed', 'fed', 'out|over|re|spoon|un|under'),
    ('feel', 'felt', 'felt', 'fore|out|re|un|under'),
    ('fight', 'fought', 'fought', 'in|out|re|un'),
    ('find', 'found', 'found', 'out|re'),
    ('flee', 'fled', 'fled', 'out'),
    ('fling', 'flung', 'flung', 'out|up'),
    ('fly', 'flew', 'flown', 'out|over|re'),
    ('forbid', 'forbade/forbad', 'forbidden', 'un'),
    ('forget', 'forgot', 'forgotten', 'un'),
    ('forsake', 'forsook', 'forsaken', ''),
    ('freeze', 'froze', 'frozen', 'ad|pre|re|un'),
    ('get', 'got', 'got', 'over|un'),
    ('give', 'gave', 'given', 'for|mis|out|prefor|re|un'),
    ('go', 'went', 'gone', 'for|fore|out|over|under'),
    ('grind', 'ground', 'ground', 'over|re'),
    ('grow', 'grew', 'grown', 'for|in|inter|mis|out|over|re|un|under|up'),
    ('hang', 'hung', 'hung', 'be|over|re|un|under|up'),
    ('have', 'had', 'had', 'un'),
    ('hear', 'heard', 'heard', 'mis|out|over|re'),
    ('hide', 'hid', 'hidden', 're|un'),
    ('hit', 'hit', 'hit', 'mis|out|over|un'),
    ('hold', 'held', 'held', 'be|over|un|up|with'),
    ('hurt', 'hurt', 'hurt', 'un'),
    ('keep', 'kept', 'kept', 'house|mis|out'),
    ('kneel', 'knelt/kneeled', 'knelt/kneeled', ''),
    ('know', 'knew', 'known', 'ac|be|fore|mis|pre|un'),
    ('lay', 'laid', 'laid', 'in|inter|mis|on|out|over|un|under|up|way'),
    ('lead', 'led', 'led', 'co|mis|out|un'),
    ('leave', 'left', 'left', 'be|for|un'),
    ('lend', 'lent', 'lent', 'over|re'),
    ('let', 'let', 'let', 'sub|un|under'),
    ('lie', 'lied/lay', 'lied/lain', ''),
    ('light', 'lit', 'lit/lighted', 'mis|over|re|un|under|up'),
    ('lose', 'lost', 'lost', 're'),
    ('make', 'made', 'made', 'co|mis|pre|re|trans|un'),
    ('may', 'might', '', ''),
    ('mean', 'meant', 'meant', ''),
    ('meet', 'met', 'met', 'inter|mis|re|un'),
    ('mow', 'mowed', 'mown/mowed', ''),
    ('pay', 'paid', 'paid', 'mis|over|pre|re|un|under'),
    ('put', 'put', 'put', 'in|mis|out|over|reout|through|thru|trans|un|under'),
    ('read', 'read/red', 'read/red', 'mis|out|over|proof|re|un|under|unproof'),
    ('rend', 'rent', 'rent', ''),
    ('rid', 'rid', 'rid', ''),
    ('ride', 'rod', 'ridden', 'out|over|un'),
    ('ring', 'ran', 'rung', 'out|un'),
    ('rise', 'rose', 'risen', 'a|over|re|rea|up'),
    ('run', 'ran', 'run', 'fore|in|inter|long|mis|out|over|press|re|un|under|up'),
    ('say', 'said', 'said', 'fore|mis|out|over|pre|re|un'),
    ('see', 'saw', 'seen', 'be|for|fore|out|over|pre|sight|un|under|unfore'),
    ('seek', 'sought', 'sought', 'be|out|re'),
    ('sell', 'sold', 'sold', 'out|over|pre|re|un|under'),
    ('send', 'sent', 'sent', 'god|mis|re|up'),
    (
        'set',
        'set',
        'set',
        'down|for|fore|forth|in|inter|mis|off|on|out|over|pre|re|reoff|sub|um|umbe|un|unbe|under|unoff|unup|up|ver',
    ),
    ('sew', 'sewed', 'sewn/sewed', 'hand|over|re|un'),
    ('shake', 'shook', 'shaken', 're'),
    ('shed', 'shed', 'shed', ''),
    ('shine', 'shone/shined', 'shone/shined', 'out|over|re|under'),
    ('shoe', 'shod', 'shod', 're|slip|un'),
    ('shoot', 'shot', 'shot', 'inter|out|over|pot|re|snap|trouble|under|up'),
    ('shrink', 'shrank', 'shrunk', 'pre|un'),
    ('shrive', 'shrove', 'shriven', ''),
    ('shut', 'shut', 'shut', 'out|re|un|under|up'),
    ('sing', 'sang', 'sung', 'mis|out|un'),
    ('sink', 'sank/sunk', 'sunk', 'counter'),
    ('sit', 'sat', 'sat', 'out|re'),
    ('slay', 'slew', 'slain', ''),
    ('sleep', 'slept', 'slept', 'out|over|under'),
    ('slide', 'slid', 'slid', 'back|land|out|over'),
    ('sling', 'slung', 'slung', 'un'),
    ('slink', 'slunk', 'slunk', ''),
    ('slit', 'slit', 'slit', 'un'),
    ('smell', 'smelt/smelled', 'smelt/smelled', 're'),
    ('smite', 'smote', 'smitten', 'over'),
    ('sow', 'sowed', 'sown/sowed', 'over|re'),
    ('speak', 'spoke', 'spoken', 'be|for|fore|in|mis|out|over|re|un|unbe'),
    ('speed', 'sped', 'sped', 'be|out|un'),
    ('spell', 'spelt/spelled', 'spelt/spelled', 'mis|out|re|un'),
    ('spend', 'spent', 'spent', 'for|mis|out|over|under'),
    ('spill', 'spilt/spilled', 'spilt/spilled', 'over'),
    ('spin', 'spun', 'spun', 'over|un'),
    ('spit', 'spat/spit', 'spat/spit', 'out'),
    ('split', 'split', 'split', 'be|pre|re|un'),
    ('spoil', 'spoilt/spoiled', 'spoilt/spoiled', 'un'),
    ('spread', 'spread', 'spread', 'back|be|broad|di|dis|for|out|over|pre|re|un|under|up|wide|wing'),
    ('spring', 'sprang', 'sprung', 'over|re|un|up'),
    ('stand', 'stood', 'stood', 'misunder|out|over|preunder|under|up|with'),
    ('stave', 'stove/staved', 'stove/staved', ''),
    ('steal', 'stole', 'stolen', 'out'),
    ('stick', 'stuck', 'stuck', 'be|un'),
    ('sting', 'stung', 'stung', 'out|re|un'),
    ('stink', 'stank/stunk', 'stunk', 'out'),
    ('stride', 'strode', 'stridden', 'be|out|over'),
    ('strike', 'struck', 'struck', 'out|over|re|un|under'),
    ('string', 'strung', 'strung', 'bow|ham|over|re|un|under'),
    ('strive', 'strove', 'striven', 'inter|out|over|re'),
    ('sweep', 'swept', 'swept', 're|under|up'),
    ('swell', 'swelled', 'swelled/swollen', 'over|un|up'),
    ('swim', 'swam', 'swum', 'out'),
    ('swing', 'swung', 'swung', 'out|un|up'),
    ('take', 'took', 'taken', 'be|care|mis|out|over|par|prepar|preunder|re|under'),
    ('teach', 'taught', 'taught', 'mis|over|pre|re|un|under'),
    ('tear', 'tore', 'torn', 'out|re|up'),
    ('tell', 'told', 'told', 'fore|mis|out|over|pre|re|s|un'),
    ('think', 'thought', 'thought', 'be|for|fore|mis|out|over|re|un|unbe|under'),
    ('thrive', 'throve/thrived', 'thriven/thrived', ''),
    ('throw', 'threw', 'thrown', 'down|mis|out|over|preover|up'),
    ('thrust', 'thrust', 'thrust', 'counter|down|in|out|over|pre|re|un|under|up'),
    ('tread', 'trod', 'trodden/trod', 'over|re|un|under'),
    ('wake', 'woke/waked', 'woken/waked', 'a|re|rea'),
    ('wear', 'wore', 'worn', 'foot|for|fores|fors|out|outs|over|s|uns'),
    ('weave', 'wove', 'woven/wove', 'en|in|inter|out|over|re|un'),
    ('weep', 'wept', 'wept', 'be|out'),
    ('wet', 'wet/wetted', 'wet/wetted', 'be|over|re|un'),
    ('win', 'won', 'won', 'over|re'),
    ('wind', 'wound', 'wound', 'in|inter|over|re|un|under|up'),
    ('wring', 'wrung', 'wrung', 'out'),
    ('write', 'wrote', 'written', 'ghost|hand|mis|out|over|re|type|un|under'),
]
