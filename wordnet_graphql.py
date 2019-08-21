from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import Synset
from typing import List, Optional
from enum import Enum

import graphene
from graphene.test import Client
from pprint import pprint

NOUN = 'n'
VERB = 'v'
ADVERB = 'r'
ADJECTIVE = 'a'


def synset_to_node(synset: Synset):
    return SynsetNode(name=synset.name())

class SynsetNode(graphene.ObjectType):
    # Synset Attributes
    name = graphene.String()
    pos = graphene.String()
    # ToDo: Lemmas ...
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
    depth = graphene.Int()
    root_hypernyms = graphene.List(lambda: SynsetNode)
    common_hypernyms = graphene.List(lambda: SynsetNode, otherSynsetName=graphene.String())
    lowest_common_hypernyms = graphene.List(lambda: SynsetNode, otherSynsetName=graphene.String())


    def resolve_pos(self, info):
        return wn.synset(self.name).pos()


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


    def resolve_depth(self, info):
        """
        shortest path from node to a top taxonomy node
        'entity' has depth = 0
        'horse' has depth = 14
        'mare' has depth = 15
        """
        return wn.synset(self.name).min_depth()


    def resolve_root_hypernyms(self, info):
        return list(map(synset_to_node, wn.synset(self.name).root_hypernyms()))


    def resolve_common_hypernyms(self, info, otherSynsetName='entity.n.01'):
        otherSynset = wn.synset(otherSynsetName)
        return list(map(synset_to_node, wn.synset(self.name).common_hypernyms(otherSynset)))


    def resolve_lowest_common_hypernyms(self, info, otherSynsetName='entity.n.01'):
        otherSynset = wn.synset(otherSynsetName)
        return list(map(synset_to_node, wn.synset(self.name).lowest_common_hypernyms(otherSynset)))


    def __repr__(self):
        return 'SynsetNode(' + self.name + ')'


class Query(graphene.ObjectType):
    synset = graphene.Field(SynsetNode, name=graphene.String())


    def resolve_synset(self, info, name):
        return synset_to_node(wn.synset(name))


schema = graphene.Schema(query=Query)
