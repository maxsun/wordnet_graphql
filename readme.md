
# Wordnet-GraphQL Schema

### To-Do List:

- [x] Implement Synset GraphQL Object Type
- [x] Implement Synset Tests
- [x] Implement Lemma Object Type
- [x] Implement Lemma Tests
- [ ] Implement synsets resolver query
- [ ] Add docstrings
- [ ] Write Code Examples

Missing:
- Synset:
  - hypernym_paths
  - hypernym_distances
  - tree
  - res_similarity
  - jcn_similarity
  - lin_similarity
- Lemma:
  - None :)

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

