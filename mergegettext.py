from mercurial import simplemerge
Merge3Text = simplemerge.Merge3Text

class Merge3Gettext(Merge3Text):
    def merge_regions(self):
        regions = super(Merge3Gettext, self).merge_regions()
        for t in regions:
            what = t[0]
            if what != 'conflict':
                yield t
                continue
            base = self.base[t[1]:t[2]]
            a = self.a[t[3]:t[4]]
            b = self.b[t[5]:t[6]]
            full = base + a + b
            if all(x.startswith('#: ') for x in full):
                yield 'b', t[5], t[6]
            else:
                yield t

def simple(base, local, other):
    merge = Merge3Gettext(base, local, other)
    lines = merge.merge_lines(
        name_a='local',
        name_b='other',
        reprocess=True,
    )
    return ''.join(lines)


