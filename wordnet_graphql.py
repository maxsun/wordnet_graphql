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

    hypernyms = graphene.List(lambda: WordNetObjectNode)
    instance_hypernyms = graphene.List(lambda: WordNetObjectNode)
    hyponyms = graphene.List(lambda: WordNetObjectNode)
    instance_hyponyms = graphene.List(lambda: WordNetObjectNode)
    member_holonyms = graphene.List(lambda: WordNetObjectNode)
    substance_holonyms = graphene.List(lambda: WordNetObjectNode)
    part_holonyms = graphene.List(lambda: WordNetObjectNode)
    member_meronyms = graphene.List(lambda: WordNetObjectNode)
    substance_meronyms = graphene.List(lambda: WordNetObjectNode)
    part_meronyms = graphene.List(lambda: WordNetObjectNode)
    topic_domains = graphene.List(lambda: WordNetObjectNode)
    in_topic_domains = graphene.List(lambda: WordNetObjectNode)
    region_domains = graphene.List(lambda: WordNetObjectNode)
    in_region_domains = graphene.List(lambda: WordNetObjectNode)
    usage_domains = graphene.List(lambda: WordNetObjectNode)
    in_usage_domains = graphene.List(lambda: WordNetObjectNode)
    attributes = graphene.List(lambda: WordNetObjectNode)
    entailments = graphene.List(lambda: WordNetObjectNode)
    causes = graphene.List(lambda: WordNetObjectNode)
    also_sees = graphene.List(lambda: WordNetObjectNode)
    verb_groups = graphene.List(lambda: WordNetObjectNode)
    similar_tos = graphene.List(lambda: WordNetObjectNode)

    def resolve_type(self):
        if isinstance(self.wordnet_obj, Synset):
            return SynsetNode
        elif isinstance(self.wordnet_obj, Lemma):
            return LemmaNode
        else:
            return NotImplementedError

    def resolve_hypernyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.hypernyms()))

    def resolve_instance_hypernyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.instance_hypernyms()))

    def resolve_hyponyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.hyponyms()))

    def resolve_instance_hyponyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.instance_hyponyms()))

    def resolve_member_holonyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.member_holonyms()))

    def resolve_substance_holonyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.substance_holonyms()))

    def resolve_part_holonyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.part_holonyms()))

    def resolve_part_meronyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.part_meronyms()))

    def resolve_member_meronyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.member_meronyms()))

    def resolve_substance_meronyms(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.substance_meronyms()))

    def resolve_topic_domains(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.topic_domains()))

    def resolve_in_topic_domains(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.in_topic_domains()))

    def resolve_region_domains(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.region_domains()))

    def resolve_in_region_domains(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.in_region_domains()))

    def resolve_usage_domains(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.usage_domains()))

    def resolve_in_usage_domains(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.in_usage_domains()))

    def resolve_attributes(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.attributes()))

    def resolve_entailments(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.entailments()))

    def resolve_causes(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.causes()))

    def resolve_also_sees(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.also_sees()))

    def resolve_verb_groups(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.verb_groups()))

    def resolve_similar_tos(self, info):
        return list(map(
            self.resolve_type(),
            self.wordnet_obj.similar_tos()))

    def __init__(self, wordnet_obj):
        self.wordnet_obj = wordnet_obj


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
    frame_ids = graphene.List(graphene.Int)
    definition = graphene.String()
    examples = graphene.List(graphene.String)
    lexname = graphene.String()
    lemma_names = graphene.List(graphene.String)
    lemmas = graphene.List(lambda: LemmaNode)
    root_hypernyms = graphene.List(lambda: SynsetNode)
    max_depth = graphene.Int()
    min_depth = graphene.Int()
    closure = graphene.List(
        lambda: SynsetNode,
        relationshipName=graphene.String(required=True),
        depth=graphene.Int(required=False))
    # Missing: hypernym paths
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
        return self.wordnet_obj.pos()

    def resolve_offset(self, info):
        return self.wordnet_obj.offset()

    def resolve_name(self, info):
        return self.wordnet_obj.name()

    def resolve_frame_ids(self, info):
        return self.wordnet_obj.frame_ids()

    def resolve_definition(self, info):
        return self.wordnet_obj.definition()

    def resolve_examples(self, info):
        return self.wordnet_obj.examples()

    def resolve_lexname(self, info):
        return self.wordnet_obj.lexname()

    def resolve_lemma_names(self, info):
        return self.wordnet_obj.lemma_names()

    def resolve_lemmas(self, info):
        return list(map(lambda x: LemmaNode(x), self.wordnet_obj.lemmas()))

    def resolve_root_hypernyms(self, info):
        return list(map(
            lambda x: SynsetNode(x),
            self.wordnet_obj.root_hypernyms()))

    def resolve_max_depth(self, info):
        return self.wordnet_obj.max_depth()

    def resolve_min_depth(self, info):
        return self.wordnet_obj.min_depth()

    def resolve_closure(self, info, relationshipName, depth=-1):
        if relationshipName == "hypernyms":
            rel = lambda s:s.hypernyms()
        elif relationshipName == "instance_hypernyms":
            rel = lambda s:s.instance_hypernyms()
        elif relationshipName == "hyponyms":
            rel = lambda s:s.hyponyms()
        elif relationshipName == "instance_hyponyms":
            rel = lambda s:s.instance_hyponyms()
        elif relationshipName == "member_holonyms":
            rel = lambda s:s.member_holonyms()
        elif relationshipName == "substance_holonyms":
            rel = lambda s:s.substance_holonyms()
        elif relationshipName == "part_holonyms":
            rel = lambda s:s.part_holonyms()
        elif relationshipName == "member_meronyms":
            rel = lambda s:s.member_meronyms()
        elif relationshipName == "substance_meronyms":
            rel = lambda s:s.substance_meronyms()
        elif relationshipName == "part_meronyms":
            rel = lambda s:s.part_meronyms()
        elif relationshipName == "topic_domains":
            rel = lambda s:s.topic_domains()
        elif relationshipName == "in_topic_domains":
            rel = lambda s:s.in_topic_domains()
        elif relationshipName == "region_domains":
            rel = lambda s:s.region_domains()
        elif relationshipName == "in_region_domains":
            rel = lambda s:s.in_region_domains()
        elif relationshipName == "usage_domains":
            rel = lambda s:s.usage_domains()
        elif relationshipName == "in_usage_domains":
            rel = lambda s:s.in_usage_domains()
        elif relationshipName == "attributes":
            rel = lambda s:s.attributes()
        elif relationshipName == "entailments":
            rel = lambda s:s.entailments()
        elif relationshipName == "causes":
            rel = lambda s:s.causes()
        elif relationshipName == "also_sees":
            rel = lambda s:s.also_sees()
        elif relationshipName == "verb_groups":
            rel = lambda s:s.verb_groups()
        elif relationshipName == "similar_tos":
            rel = lambda s:s.similar_tos()

        return list(map(
            lambda x: SynsetNode(x),
            self.wordnet_obj.closure(rel, depth)))

    def resolve_common_hypernyms(self, info, otherSynsetName):
        otherSynset = wn.synset(otherSynsetName)
        return list(map(
            lambda x: SynsetNode(x),
            self.wordnet_obj.common_hypernyms(otherSynset)))

    def resolve_lowest_common_hypernyms(self, info, otherSynsetName):
        otherSynset = wn.synset(otherSynsetName)
        return list(map(
            lambda x: SynsetNode(x),
            self.wordnet_obj.lowest_common_hypernyms(otherSynset)))

    def resolve_shortest_path_distance(self, info,
                                       otherSynsetName, simulateRoot=False):
        otherSynset = wn.synset(otherSynsetName)
        return self.wordnet_obj.shortest_path_distance(
            otherSynset,
            simulateRoot)

    def resolve_path_similarity(
            self,
            info,
            otherSynsetName='entity.n.01',
            simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return self.wordnet_obj.path_similarity(otherSynset, simulateRoot)

    def resolve_lch_similarity(
            self,
            info,
            otherSynsetName,
            simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return self.wordnet_obj.lch_similarity(otherSynset, simulateRoot)

    def resolve_wup_similarity(
            self,
            info,
            otherSynsetName='entity.n.01',
            simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return self.wordnet_obj.wup_similarity(otherSynset, simulateRoot)

    def __init__(self, wordnet_obj):
        WordNetObjectNode.__init__(self, wordnet_obj)


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
    frame_strings = graphene.List(graphene.String)
    frame_ids = graphene.List(graphene.Int)
    lang = graphene.String()
    key = graphene.String()
    count = graphene.Int()
    antonyms = graphene.List(lambda: LemmaNode)
    derivationally_related_forms = graphene.List(lambda: LemmaNode)
    pertainyms = graphene.List(lambda: LemmaNode)

    def resolve_name(self, info):
        return self.wordnet_obj.name()

    def resolve_syntactic_marker(self, info):
        return self.wordnet_obj.syntactic_marker()

    def resolve_synset(self, info):
        return SynsetNode(self.wordnet_obj.synset())

    def resolve_frame_strings(self, info):
        return self.wordnet_obj.frame_strings()

    def resolve_frame_ids(self, info):
        return self.wordnet_obj.frame_ids()

    def resolve_lang(self, info):
        return self.wordnet_obj.lang()

    def resolve_key(self, info):
        return self.wordnet_obj.key()

    def resolve_count(self, info):
        return self.wordnet_obj.count()

    def resolve_antonyms(self, info):
        return list(map(
            lambda x: LemmaNode(x),
            self.wordnet_obj.antonyms()))

    def resolve_derivationally_related_forms(self, info):
        return list(map(
            lambda x: LemmaNode(x),
            self.wordnet_obj.derivationally_related_forms()))

    def resolve_pertainyms(self, info):
        return list(map(
            lambda x: LemmaNode(x),
            self.wordnet_obj.pertainyms()))

    def __init__(self, wordnet_obj: _WordNetObject):
        WordNetObjectNode.__init__(self, wordnet_obj)


class Query(graphene.ObjectType):

    all_synsets = graphene.List(
        SynsetNode,
        pos=graphene.String(required=False))

    synset = graphene.Field(
        SynsetNode,
        name=graphene.String())

    lemma = graphene.Field(
        LemmaNode,
        id=graphene.String())

    def resolve_all_synsets(self, info, pos=None):
        return list(map(lambda x: SynsetNode(x), wn.all_synsets(pos=pos)))

    def resolve_synset(self, info, name="entity.n.01"):
        return SynsetNode(wn.synset(name))

    def resolve_lemma(self, info, id="entity.n.01.entity"):
        return LemmaNode(wn.lemma(id))


schema = graphene.Schema(query=Query, types=[SynsetNode])
# r = schema.execute('''
#     query TestQuery {
#         lemma(id: "dog.n.01.dog") {
#             frameStrings
#         }
#     }
# ''')
# print(r.data, r.errors)