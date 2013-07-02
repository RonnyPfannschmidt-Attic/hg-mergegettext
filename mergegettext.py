import argparse
import sys

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

def internal(base, local, other):
    merge = Merge3Gettext(base, local, other)
    lines = merge.merge_lines(
        name_a='local',
        name_b='other',
        reprocess=True,
    )
    lines = list(lines)
    return lines, merge.conflicts


def simple(base, local, other):
    lines, conflicts = internal(base, local, other)
    return ''.join(lines)

def readfile(name):
    with open(name) as fp:
        return fp.read()

def files(base, local, other):
    base_data = readfile(base)
    local_data = readfile(local)
    other_data = readfile(other)

    result, conflicts = internal(base_data, local_data, other_data)

    with open(local, 'w') as fp:
        fp.writelines(result)

    return conflicts


parser = argparse.ArgumentParser()
parser.add_argument('base')
parser.add_argument('local')
parser.add_argument('other')

def main(args=None):
    opts = parser.parse_args(args)
    print opts
    res = files(opts.base, opts.local, opts.other)
    sys.exit(int(res))

if __name__ == '__main__':
    main()
