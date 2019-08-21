
# Wordnet-GraphQL Interface

### To-Do List:

- [x] Implement Synset Interface
- [x] Implement Synset Interface Tests
- [ ] Implement Lemma Interface
- [ ] Implement Lemma Interface Tests
- [ ] Write Code Examples

---

This repo contains (work-in-progress) code for a GraphQL schema/API for NLTK Wordnet.


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
