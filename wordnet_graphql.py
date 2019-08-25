# 2019 Max Sun

from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import Synset, Lemma
from typing import List, Optional
from enum import Enum

import graphene
from graphene.test import Client
from pprint import pprint


def get_lemma_str(lemma: Lemma) -> str:
    return "%s.%s" % (lemma._synset._name, lemma._name)


def synset_to_node(synset: Synset):
    return SynsetNode(name=synset.name())


def lemma_to_node(lemma: Lemma):
    return LemmaNode(id=get_lemma_str(lemma))


class SynsetNode(graphene.ObjectType):
    # Synset Attributes
    name = graphene.String()
    pos = graphene.String()
    lemmas = graphene.List(lambda: LemmaNode)
    definition = graphene.String()
    examples = graphene.List(graphene.String)
    offset = graphene.Int()
    lexname = graphene.String()
    # Synset Methods
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
    entailments = graphene.List(lambda: SynsetNode)
    causes = graphene.List(lambda: SynsetNode)
    also_sees = graphene.List(lambda: SynsetNode)
    verb_groups = graphene.List(lambda: SynsetNode)
    similar_tos = graphene.List(lambda: SynsetNode)
    root_hypernyms = graphene.List(lambda: SynsetNode)
    max_depth = graphene.Int()
    min_depth = graphene.Int()
    # Missing: closure
    # Missing: hypernym_paths
    common_hypernyms = graphene.List(lambda: SynsetNode, otherSynsetName=graphene.String())
    lowest_common_hypernyms = graphene.List(lambda: SynsetNode, otherSynsetName=graphene.String())
    # Missing: hypernym_distances
    # Missing: _shortest_hypernym_paths
    shortest_path_distance = graphene.Float(otherSynsetName=graphene.String(required=False), simulateRoot=graphene.Boolean(required=False))
    # Missing: shortest_path_distance
    # Missing: tree
    path_similarity = graphene.Float(otherSynsetName=graphene.String(required=False), simulateRoot=graphene.Boolean(required=False))
    lch_similarity = graphene.Float(otherSynsetName=graphene.String(), simulateRoot=graphene.Boolean(required=False), default_value=None)
    wup_similarity = graphene.Float(otherSynsetName=graphene.String(required=False), simulateRoot=graphene.Boolean(required=False), default_value=None)
    # Missing: res_similarity
    # Missing: jcn_similarity
    # Missing: lin_similarity
    # Missing: _iter_hypernym_lists
    # Missing: __repr__
    # Missing: _related


    def resolve_pos(self, info):
        return wn.synset(self.name).pos()


    def resolve_lemmas(self, info):
        return list(map(lemma_to_node, wn.synset(self.name).lemmas()))


    def resolve_examples(self, info):
        return wn.synset(self.name).examples()


    def resolve_offset(self, info):
        return wn.synset(self.name).offset()


    def resolve_lexname(self, info):
        return wn.synset(self.name).lexname()


    def resolve_definition(self, info):
        return wn.synset(self.name).definition()


    def resolve_hypernyms(self, info):
        """
        Y is a hypernym of X if every X is a (kind of) Y
        (canine is a hypernym of dog)
        """
        return list(map(synset_to_node, wn.synset(self.name).hypernyms()))


    def resolve_instance_hypernyms(self, info):
        return list(map(synset_to_node, wn.synset(self.name).instance_hypernyms()))


    def resolve_hyponyms(self, info):
        """
        Y is a hyponym of X if every Y is a (kind of) X
        (dog is a hyponym of canine)
        """
        return list(map(synset_to_node, wn.synset(self.name).hyponyms()))


    def resolve_instance_hyponyms(self, info):
        """
        Y is a hyponym of X if every Y is a (kind of) X
        (dog is a hyponym of canine)
        """
        return list(map(synset_to_node, wn.synset(self.name).instance_hyponyms()))


    def resolve_member_holonyms(self, info):
        return list(map(synset_to_node, wn.synset(self.name).member_holonyms()))


    def resolve_substance_holonyms(self, info):
        """
        Y is a holonym of X if X is a part of Y
        (building is a holonym of window)
        """
        return list(map(synset_to_node, wn.synset(self.name).substance_holonyms()))


    def resolve_part_holonyms(self, info):
        """
        Y is a holonym of X if X is a part of Y
        (building is a holonym of window)
        """
        return list(map(synset_to_node, wn.synset(self.name).part_holonyms()))
    

    def resolve_member_meronyms(self, info):
        return list(map(synset_to_node, wn.synset(self.name).member_meronyms()))


    def resolve_substance_meronyms(self, info):
        """
        Y is a meronym of X if Y is a part of X
        (window is a meronym of building)
        """
        return list(map(synset_to_node, wn.synset(self.name).substance_meronyms()))


    def resolve_part_meronyms(self, info):
        """
        Y is a meronym of X if Y is a part of X
        (window is a meronym of building)
        """
        return list(map(synset_to_node, wn.synset(self.name).part_meronyms()))
    
    
    def resolve_entailments(self, info):
        """
        the verb Y is entailed by X if by doing X you must be doing Y
        (to sleep is entailed by to snore)
        """
        return list(map(synset_to_node, wn.synset(self.name).entailments()))


    def resolve_causes(self, info):
        return list(map(synset_to_node, wn.synset(self.name).causes()))


    def resolve_also_sees(self, info):
        return list(map(synset_to_node, wn.synset(self.name).also_sees()))


    def resolve_verb_groups(self, info):
        return list(map(synset_to_node, wn.synset(self.name).verb_groups()))


    def resolve_similar_tos(self, info):
        return list(map(synset_to_node, wn.synset(self.name).similar_tos()))


    def resolve_root_hypernyms(self, info):
        return list(map(synset_to_node, wn.synset(self.name).root_hypernyms()))


    def resolve_max_depth(self, info):
        return wn.synset(self.name).max_depth()


    def resolve_min_depth(self, info):
        return wn.synset(self.name).min_depth()


    def resolve_common_hypernyms(self, info, otherSynsetName='entity.n.01'):
        otherSynset = wn.synset(otherSynsetName)
        return list(map(synset_to_node, wn.synset(self.name).common_hypernyms(otherSynset)))


    def resolve_lowest_common_hypernyms(self, info, otherSynsetName='entity.n.01'):
        otherSynset = wn.synset(otherSynsetName)
        return list(map(synset_to_node, wn.synset(self.name).lowest_common_hypernyms(otherSynset)))


    def resolve_shortest_path_distance(self, info, otherSynsetName='entity.n.01', simulateRoot=False):
        otherSynset = wn.synset(otherSynsetName)
        return wn.synset(self.name).shortest_path_distance(otherSynset, simulateRoot)


    def resolve_path_similarity(self, info, otherSynsetName='entity.n.01', simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return wn.synset(self.name).path_similarity(otherSynset, simulateRoot)


    def resolve_lch_similarity(self, info, otherSynsetName, simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return wn.synset(self.name).lch_similarity(otherSynset, simulate_root=simulateRoot)


    def resolve_wup_similarity(self, info, otherSynsetName='entity.n.01', simulateRoot=True):
        otherSynset = wn.synset(otherSynsetName)
        return wn.synset(self.name).wup_similarity(otherSynset, simulate_root=simulateRoot)


    def __repr__(self):
        return 'SynsetNode(' + self.name + ')'


class LemmaNode(graphene.ObjectType):
    # Lemma Attributes
    id = graphene.String()
    name = graphene.String()
    synset = graphene.Field(SynsetNode())
    syntactic_marker = graphene.String()
    count = graphene.Int()
    # Lemma Methods
    antonyms = graphene.List(lambda: LemmaNode)
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
    region_domains = graphene.List(lambda: LemmaNode)
    usage_domains = graphene.List(lambda: LemmaNode)
    attributes = graphene.List(lambda: LemmaNode)
    derivationally_related_forms = graphene.List(lambda: LemmaNode)
    entailments = graphene.List(lambda: LemmaNode)
    causes = graphene.List(lambda: LemmaNode)
    also_sees = graphene.List(lambda: LemmaNode)
    verb_groups = graphene.List(lambda: LemmaNode)
    similar_tos = graphene.List(lambda: LemmaNode)
    pertainyms = graphene.List(lambda: LemmaNode)


    def resolve_name(self, info):
        return wn.lemma(self.id).name()


    def resolve_synset(self, info):
        return synset_to_node(wn.lemma(self.id).synset())


    def resolve_syntactic_marker(self, info):
        return wn.lemma(self.id).syntactic_marker()


    def resolve_count(self, info):
        return wn.lemma(self.id).count()


    def resolve_antonyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).antonyms()))


    def resolve_hypernyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).hypernyms()))


    def resolve_instance_hypernyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).instance_hypernyms()))


    def resolve_hyponyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).hyponyms()))


    def resolve_instance_hyponyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).instance_hyponyms()))


    def resolve_member_holonyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).member_holonyms()))


    def resolve_substance_holonyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).substance_holonyms()))


    def resolve_part_holonyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).part_holonyms()))


    def resolve_member_meronyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).member_meronyms()))


    def resolve_substance_meronyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).substance_meronyms()))


    def resolve_part_meronyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).part_meronyms()))


    def resolve_topic_domains(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).topic_domains()))


    def resolve_region_domains(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).region_domains()))


    def resolve_usage_domains(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).usage_domains()))


    def resolve_attributes(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).attributes()))


    def resolve_derivationally_related_forms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).derivationally_related_forms()))


    def resolve_entailments(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).entailments()))


    def resolve_causes(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).causes()))

    
    def resolve_also_sees(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).also_sees()))


    def resolve_verb_groups(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).verb_groups()))


    def resolve_similar_tos(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).similar_tos()))


    def resolve_pertainyms(self, info):
        return list(map(lemma_to_node, wn.lemma(self.id).pertainyms()))


    def __repr__(self):
        return 'LemmaNode(' + self.id + ')'


class Query(graphene.ObjectType):
    all_synsets = graphene.List(SynsetNode, pos=graphene.String(required=False))
    synset = graphene.Field(SynsetNode, name=graphene.String())
    lemma = graphene.Field(LemmaNode, id=graphene.String())


    def resolve_all_synsets(self, info, pos=None):
        return list(map(synset_to_node, wn.all_synsets(pos=pos)))

    def resolve_synset(self, info, name):
        return synset_to_node(wn.synset(name))


    def resolve_lemma(self, info, id):
        return lemma_to_node(wn.lemma(id))


schema = graphene.Schema(query=Query)

# a = wn.synset('entity.n.01')
# b = wn.synset('baby.n.05')
# print(a.path_similarity(b))
