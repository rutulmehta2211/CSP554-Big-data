from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")
aton = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n')

class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            if(word.startswith(aton)):
                yield 'a_to_n', 1
            else:
                yield 'other', 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordCount.run()