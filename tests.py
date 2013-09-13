from duckduckgo import query
import unittest


class GrandDuckDuckGoTestSuite(unittest.TestCase):
    def testDuckDuckGo(self):
        dataset = query('duckduckgo')
        ds = dataset
        self.assertEqual(ds.type, 'answer')
        self.assertEqual(ds.result[0].url, 'https://duckduckgo.com/')
        self.assertEqual(len(ds.related), 1)
        self.assertEqual(ds.related[0].url, 'http://duckduckgo.com/c/Internet_search_engines?kp=1')
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract.url, 'https://en.wikipedia.org/wiki/Duck_Duck_Go')
        self.assertEqual(ds.redirect, None)

    def test4_pow_10(self):
        dataset = query('4 ^ 10')
        ds = dataset
        self.assertEqual(ds.type, 'exclusive')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 0)
        self.assertEqual(ds.answer.primary, '4 ^ 10 = 1,048,576')
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract, None)
        self.assertEqual(ds.redirect, None)

    def testYahoo(self):
        dataset = query('Yahoo!')
        ds = dataset
        self.assertEqual(ds.type, 'disambiguation')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 6)
        self.assertEqual(ds.related[0].url, 'http://duckduckgo.com/Yahoo!?kp=1')
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract, None)
        self.assertEqual(ds.redirect, None)

    def test42(self):
        dataset = query('42')
        ds = dataset
        self.assertEqual(ds.type, 'disambiguation')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 7)
        self.assertEqual(ds.related[0].url, 'http://duckduckgo.com/42?kp=1')
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract, None)
        self.assertEqual(ds.redirect, None)

    def testGenomeProject(self):
        dataset = query('Genome Project')
        ds = dataset
        self.assertEqual(ds.type, 'answer')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 6)
        self.assertEqual(ds.related[0].url, 'http://duckduckgo.com/Joint_Genome_Institute?kp=1')
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract.url, 'https://en.wikipedia.org/wiki/Genome_project')
        self.assertEqual(ds.redirect, None)

    def testBeetle(self):
        dataset = query('Beetle')
        ds = dataset
        self.assertEqual(ds.type, 'disambiguation')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 20)
        self.assertEqual(ds.related[0].url, 'http://duckduckgo.com/Beetle?kp=1')
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition.url, 'http://www.merriam-webster.com/dictionary/beetle')
        self.assertEqual(ds.abstract, None)
        self.assertEqual(ds.redirect, None)

    def testGoLang(self):
        dataset = query('golang')
        ds = dataset
        self.assertEqual(ds.type, 'answer')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 7)
        self.assertEqual(ds.related[0].url, 'http://duckduckgo.com/Go!_(programming_language)?kp=1')
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract.url, 'https://en.wikipedia.org/wiki/Go_(programming_language)')
        self.assertEqual(ds.redirect, None)

    def testPythonDuckDuckGo(self):
        dataset = query('python-duckduckgo')
        ds = dataset
        self.assertEqual(ds.type, 'answer')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 0)
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract.url, 'https://github.com/mikejs/python-duckduckgo')
        self.assertEqual(ds.redirect, None)

    def testPythonDjango(self):
        dataset = query('python django')
        ds = dataset
        self.assertEqual(ds.type, 'nothing')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 0)
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract, None)
        self.assertEqual(ds.redirect, None)

    def testNFAK(self):
        dataset = query('NFAK')
        ds = dataset
        self.assertEqual(ds.type, 'answer')
        self.assertEqual(ds.result, [])
        self.assertEqual(len(ds.related), 8)
        self.assertEqual(ds.related[0].url, 'http://duckduckgo.com/c/Harmonium_players?kp=1')
        self.assertEqual(ds.answer, None)
        self.assertEqual(ds.definition, None)
        self.assertEqual(ds.abstract.url, 'https://en.wikipedia.org/wiki/Nusrat_Fateh_Ali_Khan')
        self.assertEqual(ds.redirect, None)


if __name__ == '__main__':
    unittest.main()
