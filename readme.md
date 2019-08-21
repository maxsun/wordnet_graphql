
# Wordnet-GraphQL Interface

### To-Do List:

- [x] Implement Synset Interface
- [x] Implement Synset Interface Tests
- [x] Implement Lemma Interface
- [x] Implement Lemma Interface Tests
- [ ] Implement Finitely recursive queries (ie: get hyponyms until depth >= n)
- [ ] Write Code Examples

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

