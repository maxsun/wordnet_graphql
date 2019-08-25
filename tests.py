import unittest
import wordnet_graphql
from numpy.random import permutation
from graphene.test import Client
from nltk.corpus import wordnet as wn

all_synsets = list(wn.all_synsets())

client = Client(wordnet_graphql.schema)


class LemmaTest(unittest.TestCase):
    """
    (Documentation from: https://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html)
    
    Lemma attributes, accessible via methods with the same name:

    - name: The canonical name of this lemma.
    - synset: The synset that this lemma belongs to.
    - syntactic_marker: For adjectives, the WordNet string identifying the
      syntactic position relative modified noun. See:
      https://wordnet.princeton.edu/documentation/wninput5wn
      For all other parts of speech, this attribute is None.
    - count: The frequency of this lemma in wordnet.

    Lemma methods:

    These methods all return lists of Lemmas.

    - antonyms
    - hypernyms, instance_hypernyms
    - hyponyms, instance_hyponyms
    - member_holonyms, substance_holonyms, part_holonyms
    - member_meronyms, substance_meronyms, part_meronyms
    - topic_domains, region_domains, usage_domains
    - attributes
    - derivationally_related_forms
    - entailments
    - causes
    - also_sees
    - verb_groups
    - similar_tos
    - pertainyms
    """
    def test_lemma(self, lemma_id='vocal.a.01.vocal'):
        lemma = wn.lemma(lemma_id)
        data = client.execute('''
            query TestQuery {
                    lemma (id: "%s") {
                        name
                        synset {
                            name
                        }
                        syntacticMarker
                        count
                        antonyms {
                            name
                        }
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
                        topicDomains {
                            name
                        }
                        regionDomains {
                            name
                        }
                        usageDomains {
                            name
                        }
                        attributes {
                            name
                        }
                        derivationallyRelatedForms {
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
                        pertainyms {
                            name
                        }
                    }
                }
        ''' % lemma_id)
        data = data['data']['lemma']

        self.assertEqual(lemma.name(), data['name'])
        self.assertEqual(lemma.synset().name(), data['synset']['name'])
        self.assertEqual(lemma.syntactic_marker(), data['syntacticMarker'])
        self.assertEqual(lemma.count(), data['count'])
        
        antonyms = lemma.antonyms()
        for i, l in enumerate(antonyms):
            self.assertEqual(l.name(), data['antonyms'][i]['name'])

        hypernyms = lemma.hypernyms()
        for i, l in enumerate(hypernyms):
            self.assertEqual(l.name(), data['hypernyms'][i]['name'])

        instanceHypernyms = lemma.instance_hypernyms()
        for i, l in enumerate(instanceHypernyms):
            self.assertEqual(l.name(), data['instanceHypernyms'][i]['name'])

        hyponyms = lemma.hyponyms()
        for i, l in enumerate(hyponyms):
            self.assertEqual(l.name(), data['hyponyms'][i]['name'])

        instanceHyponyms = lemma.instance_hyponyms()
        for i, l in enumerate(instanceHyponyms):
            self.assertEqual(l.name(), data['instanceHyponyms'][i]['name'])

        memberHolonyms = lemma.member_holonyms()
        for i, l in enumerate(memberHolonyms):
            self.assertEqual(l.name(), data['memberHolonyms'][i]['name'])

        substanceHolonyms = lemma.substance_holonyms()
        for i, l in enumerate(substanceHolonyms):
            self.assertEqual(l.name(), data['substanceHolonyms'][i]['name'])

        partHolonyms = lemma.part_holonyms()
        for i, l in enumerate(partHolonyms):
            self.assertEqual(l.name(), data['partHolonyms'][i]['name'])

        memberMeronyms = lemma.member_meronyms()
        for i, l in enumerate(memberMeronyms):
            self.assertEqual(l.name(), data['memberMeronyms'][i]['name'])

        substanceMeronyms = lemma.substance_meronyms()
        for i, l in enumerate(substanceMeronyms):
            self.assertEqual(l.name(), data['substanceMeronyms'][i]['name'])

        partMeronyms = lemma.part_meronyms()
        for i, l in enumerate(partMeronyms):
            self.assertEqual(l.name(), data['partMeronyms'][i]['name'])

        topicDomains = lemma.topic_domains()
        for i, l in enumerate(topicDomains):
            self.assertEqual(l.name(), data['topicDomains'][i]['name'])

        regionDomains = lemma.region_domains()
        for i, l in enumerate(regionDomains):
            self.assertEqual(l.name(), data['regionDomains'][i]['name'])

        usageDomains = lemma.usage_domains()
        for i, l in enumerate(usageDomains):
            self.assertEqual(l.name(), data['usageDomains'][i]['name'])

        attributes = lemma.attributes()
        for i, l in enumerate(attributes):
            self.assertEqual(l.name(), data['attributes'][i]['name'])

        derivationallyRelatedForms = lemma.derivationally_related_forms()
        for i, l in enumerate(derivationallyRelatedForms):
            self.assertEqual(l.name(), data['derivationallyRelatedForms'][i]['name'])

        entailments = lemma.entailments()
        for i, l in enumerate(entailments):
            self.assertEqual(l.name(), data['entailments'][i]['name'])

        causes = lemma.causes()
        for i, l in enumerate(causes):
            self.assertEqual(l.name(), data['causes'][i]['name'])

        alsoSees = lemma.also_sees()
        for i, l in enumerate(alsoSees):
            self.assertEqual(l.name(), data['alsoSees'][i]['name'])

        verbGroups = lemma.verb_groups()
        for i, l in enumerate(verbGroups):
            self.assertEqual(l.name(), data['verbGroups'][i]['name'])

        similarTos = lemma.similar_tos()
        for i, l in enumerate(similarTos):
            self.assertEqual(l.name(), data['similarTos'][i]['name'])

        pertainyms = lemma.pertainyms()
        for i, l in enumerate(pertainyms):
            self.assertEqual(l.name(), data['pertainyms'][i]['name'])


    def test_first_1000_lemmas(self):
        for synset in all_synsets[:1000]:
            self.test_lemma(wordnet_graphql.get_lemma_str(synset.lemmas()[0]))


    def test_random_1000_lemmas(self):
        for synset in permutation(all_synsets)[:1000]:
            self.test_lemma(wordnet_graphql.get_lemma_str(synset.lemmas()[0]))


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
    def test_all_synsets(self):
        data = client.execute('''
            query TestQuery {
                allSynsets {
                    name
                }
            }
        ''')['data']
        for i, synset in enumerate(data['allSynsets']):
            self.assertEqual(all_synsets[i].name(), synset['name'])

    def test_synset(self, synset_name='entity.n.01', synset_name2='entity.n.01'):
        synset = wn.synset(synset_name)
        synset2 = wn.synset(synset_name2)
        data = client.execute('''
            query TestQuery {
                synset(name: "%s") {
                    name
                    pos
                    lemmas {
                        name
                    }
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

        lemmas = synset.lemmas()
        for i, l in enumerate(lemmas):
            self.assertEqual(l.name(), data['lemmas'][i]['name'])

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
        for synset in all_synsets[:1000]:
            self.test_synset(synset.name())

    
    def test_random_1000_synsets(self):
        for synset in permutation(all_synsets)[:1000]:
            self.test_synset(synset.name())


print('Running Tests...')
unittest.main()
