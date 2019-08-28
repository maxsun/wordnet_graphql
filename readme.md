
# Wordnet-GraphQL Schema

### To-Do List:

- [x] Implement Synset GraphQL Object Type
- [x] Implement Synset Tests
- [x] Implement Lemma Object Type
- [x] Implement Lemma Tests
- [ ] Implement Finitely recursive queries (ie: get hyponyms until depth >= n)
- [ ] Add docstrings
- [ ] Write Code Examples
- [ ] Improve tests by using variables in the queries

Missing:
- Synset:
  - closure
  - hypernym_paths
  - hypernym_distances
  - _shortest_hypernym_paths
  - tree
  - res_similarity
  - jcn_similarity
  - lin_similarity
  - _iter_hypernym_lists
  - __repr__
  - _related

---

This repo contains (work-in-progress) code for a [GraphQL](https://graphql.org/) schema/API for [NLTK Wordnet](http://www.nltk.org/howto/wordnet.html).

For deeper documentation, see the [Wordnet Source](https://wordnet.princeton.edu/documentation/wngloss7wn).


For example, this query:
```graphql
query ExampleQuery {
                synset(name: "computer.n.01") {
                    name
                    definition
                    hypernyms {
                        name
                    }
                }
            }
```
returns:
```python
{'data': OrderedDict([('synset',
                       OrderedDict([('name', 'computer.n.01'),
                                    ('definition',
                                     'a machine for performing calculations '
                                     'automatically'),
                                    ('hypernyms',
                                     [OrderedDict([('name',
                                                    'machine.n.01')])])]))])}
```

