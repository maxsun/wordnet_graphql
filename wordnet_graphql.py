# 2019 Max Sun

from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import Synset, Lemma, _WordNetObject
from typing import List, Optional
from enum import Enum

import graphene
from graphene.test import Client
from pprint import pprint


def get_lemma_str(lemma: Lemma) -> str:
    return "%s.%s" % (lemma._synset._name, lemma._name)


class WordNetObjectNode(graphene.ObjectType):

    def resolve_type(self, wordnet_object):
        if isinstance(wordnet_object, Synset):
            return SynsetNode
        elif isinstance(wordnet_object, Lemma):
            return LemmaNode
        else:
            return NotImplementedError

    def resolve_hypernyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.hypernyms()))

    def resolve_instance_hypernyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.instance_hypernyms()))

    def resolve_hyponyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.hyponyms()))

    def resolve_instance_hyponyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.instance_hyponyms()))

    def resolve_member_holonyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.member_holonyms()))

    def resolve_substance_holonyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.substance_holonyms()))

    def resolve_part_holonyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.part_holonyms()))

    def resolve_part_meronyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.part_meronyms()))

    def resolve_member_meronyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.member_meronyms()))

    def resolve_substance_meronyms(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.substance_meronyms()))

    def resolve_topic_domains(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.topic_domains()))

    def resolve_in_topic_domains(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.in_topic_domains()))

    def resolve_region_domains(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.region_domains()))

    def resolve_in_region_domains(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.in_region_domains()))

    def resolve_usage_domains(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.usage_domains()))

    def resolve_in_usage_domains(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.in_usage_domains()))

    def resolve_attributes(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.attributes()))

    def resolve_entailments(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.entailments()))

    def resolve_causes(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.causes()))

    def resolve_also_sees(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.also_sees()))

    def resolve_verb_groups(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.verb_groups()))

    def resolve_similar_tos(self, info):
        typ = self.resolve_type(wordnet_object=self.wordnet_object)
        return list(map(lambda x: typ(x), self.wordnet_object.similar_tos()))

    def __init__(self, wordnet_object):
        self.wordnet_object = wordnet_object


class SynsetNode(WordNetObjectNode):
    hypernyms = graphene.List(lambda: SynsetNode)
    instance_hypernyms = graphene.List(lambda: SynsetNode)
    hyponyms = graphene.List(lambda: SynsetNode)
    instance_hyponyms = graphene.List(lambda: SynsetNode)
    member_holonyms = graphene.List(lambda: SynsetNode)
    substance_holonyms = graphene.List(lambda: SynsetNode)
    part_holonyms = graphene.List(lambda: SynsetNode)
    member_meronyms = graphene.List(lambda: SynsetNode)
    substance_meronyms = graphene.List(lambda: SynsetNode)
    part_meronyms = graphene.List(lambda: SynsetNode)
    topic_domains = graphene.List(lambda: SynsetNode)
    in_topic_domains = graphene.List(lambda: SynsetNode)
    region_domains = graphene.List(lambda: SynsetNode)
    in_region_domains = graphene.List(lambda: SynsetNode)
    usage_domains = graphene.List(lambda: SynsetNode)
    in_usage_domains = graphene.List(lambda: SynsetNode)
    attributes = graphene.List(lambda: SynsetNode)
    entailments = graphene.List(lambda: SynsetNode)
    causes = graphene.List(lambda: SynsetNode)
    also_sees = graphene.List(lambda: SynsetNode)
    verb_groups = graphene.List(lambda: SynsetNode)
    similar_tos = graphene.List(lambda: SynsetNode)

    pos = graphene.String()
    offset = graphene.Int()
    name = graphene.String()
    # frame ids
    definition = graphene.String()
    # examples = graphene.String()
    lexname = graphene.String()
    # lemma_names = graphene.List(graphene.String()
    lemmas = graphene.List(lambda: LemmaNode)
    root_hypernyms = graphene.List(lambda: SynsetNode)
    max_depth = graphene.Int()
    min_depth = graphene.Int()
    # closure
    # hypernym paths
    common_hypernyms = graphene.List(
        lambda: SynsetNode,
        otherSynsetName=graphene.String())
    lowest_common_hypernyms = graphene.List(
        lambda: SynsetNode,
        otherSynsetName=graphene.String())
    # Missing: hypernym_distances
    shortest_path_distance = graphene.Float(
        otherSynsetName=graphene.String(),
        simulateRoot=graphene.Boolean(required=False))
    # Missing: tree
    path_similarity = graphene.Float(
        otherSynsetName=graphene.String(),
        simulateRoot=graphene.Boolean(required=False))
    lch_similarity = graphene.Float(
        otherSynsetName=graphene.String(),
        simulateRoot=graphene.Boolean(required=False),
        default_value=None)
    wup_similarity = graphene.Float(
        otherSynsetName=graphene.String(),
        simulateRoot=graphene.Boolean(required=False),
        default_value=None)
    # Missing: res_similarity
    # Missing: jcn_similarity
    # Missing: lin_similarity

    def resolve_pos(self, info):
        return self.wordnet_object.pos()

    def resolve_offset(self, info):
        return self.wordnet_object.offset()

    def resolve_name(self, info):
        return self.wordnet_object.name()

    def resolve_definition(self, info):
        return self.wordnet_object.definition()

    def resolve_lexname(self, info):
        return self.wordnet_object.lexname()

    def resolve_lemmas(self, info):
        return list(map(lambda x: LemmaNode(x), self.wordnet_object.lemmas()))

    def resolve_root_hypernyms(self, info):
        return list(map(lambda x: SynsetNode(x), self.wordnet_object.root_hypernyms()))

    def resolve_max_depth(self, info):
        return self.wordnet_object.max_depth()

    def resolve_min_depth(self, info):
        return self.wordnet_object.min_depth()

    def resolve_common_hypernyms(self, info, otherSynsetName):
        otherSynset = wn.synset(otherSynsetName)
        return list(map(lambda x: SynsetNode(x), self.wordnet_object.common_hypernyms(otherSynset)))

    def resolve_lowest_common_hypernyms(self, info, otherSynsetName):
        otherSynset = wn.synset(otherSynsetName)
        return list(map(lambda x: SynsetNode(x), self.wordnet_object.lowest_common_hypernyms(otherSynset)))

    def resolve_shortest_path_distance(self, info, otherSynsetName, simulateRoot=False):
        otherSynset = wn.synset(otherSynsetName)
        return self.wordnet_object.shortest_path_distance(otherSynset, simulateRoot)

    def resolve_path_similarity(self, info, otherSynsetName='entity.n.01', simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return self.wordnet_object.path_similarity(otherSynset, simulateRoot)

    def resolve_lch_similarity(self, info, otherSynsetName, simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return self.wordnet_object.lch_similarity(otherSynset, simulate_root=simulateRoot)

    def resolve_wup_similarity(self, info, otherSynsetName='entity.n.01', simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return self.wordnet_object.wup_similarity(otherSynset, simulate_root=simulateRoot)

    def __init__(self, wordnet_object):
        WordNetObjectNode.__init__(self, wordnet_object)


class LemmaNode(WordNetObjectNode):
    hypernyms = graphene.List(lambda: LemmaNode)
    instance_hypernyms = graphene.List(lambda: LemmaNode)
    hyponyms = graphene.List(lambda: LemmaNode)
    instance_hyponyms = graphene.List(lambda: LemmaNode)
    member_holonyms = graphene.List(lambda: LemmaNode)
    substance_holonyms = graphene.List(lambda: LemmaNode)
    part_holonyms = graphene.List(lambda: LemmaNode)
    member_meronyms = graphene.List(lambda: LemmaNode)
    substance_meronyms = graphene.List(lambda: LemmaNode)
    part_meronyms = graphene.List(lambda: LemmaNode)
    topic_domains = graphene.List(lambda: LemmaNode)
    in_topic_domains = graphene.List(lambda: LemmaNode)
    region_domains = graphene.List(lambda: LemmaNode)
    in_region_domains = graphene.List(lambda: LemmaNode)
    usage_domains = graphene.List(lambda: LemmaNode)
    in_usage_domains = graphene.List(lambda: LemmaNode)
    attributes = graphene.List(lambda: LemmaNode)
    entailments = graphene.List(lambda: LemmaNode)
    causes = graphene.List(lambda: LemmaNode)
    also_sees = graphene.List(lambda: LemmaNode)
    verb_groups = graphene.List(lambda: LemmaNode)
    similar_tos = graphene.List(lambda: LemmaNode)

    name = graphene.String()
    syntactic_marker = graphene.String()
    synset = graphene.Field(SynsetNode)
    # Missing: frame_strings
    # Missing: frame_ids
    lang = graphene.String()
    key = graphene.String()
    count = graphene.Int()
    antonyms = graphene.List(lambda: LemmaNode)
    derivationally_related_forms = graphene.List(lambda: LemmaNode)
    pertainyms = graphene.List(lambda: LemmaNode)

    def resolve_name(self, info):
        return self.wordnet_object.name()

    def resolve_syntactic_marker(self, info):
        return self.wordnet_object.syntactic_marker()

    def resolve_synset(self, info):
        return SynsetNode(self.wordnet_object.synset())

    def resolve_lang(self, info):
        return self.wordnet_object.lang()

    def resolve_key(self, info):
        return self.wordnet_object.key()

    def resolve_count(self, info):
        return self.wordnet_object.count()

    def resolve_antonyms(self, info):
        return list(map(lambda x: LemmaNode(x), self.wordnet_object.antonyms()))

    def resolve_derivationally_related_forms(self, info):
        return list(map(lambda x: LemmaNode(x), self.wordnet_object.derivationally_related_forms()))

    def resolve_pertainyms(self, info):
        return list(map(lambda x: LemmaNode(x), self.wordnet_object.pertainyms()))

    def __init__(self, wordnet_object: _WordNetObject):
        WordNetObjectNode.__init__(self, wordnet_object)


class Query(graphene.ObjectType):

    all_synsets = graphene.List(SynsetNode, pos=graphene.String(required=False))
    synset = graphene.Field(SynsetNode, name=graphene.String())
    lemma = graphene.Field(LemmaNode, id=graphene.String())

    def resolve_all_synsets(self, info, pos=None):
        return list(map(lambda x: SynsetNode(x), wn.all_synsets(pos=pos)))

    def resolve_synset(self, info, name="entity.n.01"):
        return SynsetNode(wn.synset(name))

    def resolve_lemma(self, info, id):
        return LemmaNode(wn.lemma(id))


schema = graphene.Schema(query=Query, types=[SynsetNode])
