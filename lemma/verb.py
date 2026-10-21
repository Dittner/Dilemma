import re
from pathlib import Path

from lemma.corpus import Corpus

irregular_verbs = [
    ('be', 'is|are|was|were|been', ''),
    ('bear', 'bore|born|borne', 'for|out|over|un|under|up|water'),
    ('beat', 'beaten', 'brow|under'),
    ('beget', 'begot|begotten', 'mis|un'),
    ('begin', 'began|begun', 'mis'),
    ('bend', 'bent', 'down|out|re|un'),
    ('bid', '', 'counter|her|out|over|pre|re|un|under|up|ver'),
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
    ('catch', '', 'out|up'),
    ('choose', 'chose|chosen', 'mis|pre|re'),
    ('cleave', 'clove|cloven', 'un'),
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
    ('tear', 'tore', 'out|re|up'),
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
        self.patterns = [
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

        self.irr_verbs = {}
        for verb, forms, prefixes in irregular_verbs:
            ff = forms.split('|')
            ff.append(verb)
            pp = prefixes.split('|')
            for f in ff:
                if f == '':
                    continue
                self.irr_verbs[f] = verb
                for p in pp:
                    if p == '':
                        continue
                    if self.irr_verbs.get(p + f):
                        raise ValueError('Duplicated key=' + (p + f))

                    self.irr_verbs[p + f] = p + verb

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
