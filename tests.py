import unittest
import wordnet_graphql
from numpy.random import permutation
from graphene.test import Client
from nltk.corpus import wordnet as wn


client = Client(wordnet_graphql.schema)


class SynsetTest(unittest.TestCase):
    """
    (Documentation from: https://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html)

    Synset attributes, accessible via methods with the same name:

    - name: The canonical name of this synset, formed using the first lemma
      of this synset. Note that this may be different from the name
      passed to the constructor if that string used a different lemma to
      identify the synset.
    - pos: The synset's part of speech, matching one of the module level
      attributes ADJ, ADJ_SAT, ADV, NOUN or VERB.
    - lemmas: A list of the Lemma objects for this synset.
    - definition: The definition for this synset.
    - examples: A list of example strings for this synset.
    - offset: The offset in the WordNet dict file of this synset.
    - lexname: The name of the lexicographer file containing this synset.

    Synset methods:

    These methods all return lists of Synsets.

    - hypernyms, instance_hypernyms
    - hyponyms, instance_hyponyms
    - member_holonyms, substance_holonyms, part_holonyms
    - member_meronyms, substance_meronyms, part_meronyms
    - attributes
    - entailments
    - causes
    - also_sees
    - verb_groups
    - similar_tos

    Additionally, Synsets support the following methods specific to the
    hypernym relation:

    - root_hypernyms
    - common_hypernyms
    - lowest_common_hypernyms
    """
    all_synsets = list(wn.all_synsets())

    def test_synset(self, synset_name='entity.n.01', synset_name2='entity.n.01'):
        synset = wn.synset(synset_name)
        synset2 = wn.synset(synset_name2)
        data = client.execute('''
            query TestQuery {
                synset(name: "%s") {
                    name
                    pos
                    
                    definition
                    examples
                    offset
                    lexname
                    depth
                    hypernyms {
                        name
                    }
                    instanceHypernyms {
                        name
                    }
                    hyponyms {
                        name
                    }
                    instanceHyponyms {
                        name
                    }
                    memberHolonyms {
                        name
                    }
                    substanceHolonyms {
                        name
                    }
                    partHolonyms {
                        name
                    }
                    memberMeronyms {
                        name
                    }
                    substanceMeronyms {
                        name
                    }
                    partMeronyms {
                        name
                    }
                    
                    entailments {
                        name
                    }
                    causes {
                        name
                    }
                    alsoSees {
                        name
                    }
                    verbGroups {
                        name
                    }
                    similarTos {
                        name
                    }
                    rootHypernyms {
                        name
                    }
                    commonHypernyms(otherSynsetName: "%s") {
                        name
                    }
                    lowestCommonHypernyms(otherSynsetName: "%s") {
                        name
                    }

                }
            }
        ''' % (synset_name, synset_name2, synset_name2))['data']['synset']

        self.assertEqual(synset.name(), data['name'])
        self.assertEqual(synset.pos(), data['pos'])

        self.assertEqual(synset.definition(), data['definition'])
        self.assertEqual(synset.examples(), data['examples'])
        self.assertEqual(synset.offset(), data['offset'])
        self.assertEqual(synset.lexname(), data['lexname'])
        self.assertEqual(synset.min_depth(), data['depth'])

        hypernyms = synset.hypernyms()
        for i, s in enumerate(hypernyms):
            self.assertEqual(s.name(), data['hypernyms'][i]['name'])

        instanceHypernyms = synset.instance_hypernyms()
        for i, s in enumerate(instanceHypernyms):
            self.assertEqual(s.name(), data['instanceHypernyms'][i]['name'])

        hyponyms = synset.hyponyms()
        for i, s in enumerate(hyponyms):
            self.assertEqual(s.name(), data['hyponyms'][i]['name'])

        instanceHyponyms = synset.instance_hyponyms()
        for i, s in enumerate(instanceHyponyms):
            self.assertEqual(s.name(), data['instanceHyponyms'][i]['name'])

        memberHolonyms = synset.member_holonyms()
        for i, s in enumerate(memberHolonyms):
            self.assertEqual(s.name(), data['memberHolonyms'][i]['name'])

        substanceHolonyms = synset.substance_holonyms()
        for i, s in enumerate(substanceHolonyms):
            self.assertEqual(s.name(), data['substanceHolonyms'][i]['name'])

        partHolonyms = synset.part_holonyms()
        for i, s in enumerate(partHolonyms):
            self.assertEqual(s.name(), data['partHolonyms'][i]['name'])

        memberMeronyms = synset.member_meronyms()
        for i, s in enumerate(memberMeronyms):
            self.assertEqual(s.name(), data['memberMeronyms'][i]['name'])

        substanceMeronyms = synset.substance_meronyms()
        for i, s in enumerate(substanceMeronyms):
            self.assertEqual(s.name(), data['substanceMeronyms'][i]['name'])

        partMeronyms = synset.part_meronyms()
        for i, s in enumerate(partMeronyms):
            self.assertEqual(s.name(), data['partMeronyms'][i]['name'])

        entailments = synset.entailments()
        for i, s in enumerate(entailments):
            self.assertEqual(s.name(), data['entailments'][i]['name'])

        causes = synset.causes()
        for i, s in enumerate(causes):
            self.assertEqual(s.name(), data['causes'][i]['name'])

        alsoSees = synset.also_sees()
        for i, s in enumerate(alsoSees):
            self.assertEqual(s.name(), data['alsoSees'][i]['name'])

        verbGroups = synset.verb_groups()
        for i, s in enumerate(verbGroups):
            self.assertEqual(s.name(), data['verbGroups'][i]['name'])

        similarTos = synset.similar_tos()
        for i, s in enumerate(similarTos):
            self.assertEqual(s.name(), data['similarTos'][i]['name'])

        rootHypernyms = synset.root_hypernyms()
        for i, s in enumerate(rootHypernyms):
            self.assertEqual(s.name(), data['rootHypernyms'][i]['name'])

        commonHypernyms = synset.common_hypernyms(synset2)
        for i, s in enumerate(commonHypernyms):
            self.assertEqual(s.name(), data['commonHypernyms'][i]['name'])

        lowestCommonHypernyms = synset.lowest_common_hypernyms(synset2)
        for i, s in enumerate(lowestCommonHypernyms):
            self.assertEqual(s.name(), data['lowestCommonHypernyms'][i]['name'])


    def test_first_1000_synsets(self):
        for i, synset in enumerate(self.all_synsets):
            self.test_synset(synset.name())
            if i >= 1000:
                break

    
    def test_random_1000_synsets(self):
        for synset in permutation(self.all_synsets)[:1000]:
            self.test_synset(synset.name())


print('Running Tests...')
unittest.main()
