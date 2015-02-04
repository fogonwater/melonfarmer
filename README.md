## melon.farmer()
---

Simple utilities that I seem to use all the time when harvesting metadata.


`import melon`

`farmer = melon.Farmer()`

Some example uses.

`farmer.write_json({'foo' : 'bar'}, 'test.json')`

`d = farmer.read_json('test.json')`

`farmer.post_json(d, 'http://example.com/')`
