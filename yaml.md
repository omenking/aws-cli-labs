## Basic Example

Example of basic YAML

```
---
Hello:
      World: "Canada"
```
    	
```yml
---
Hello: "World"
Planets:
  Sol:
    - Mercury 
    - Venus
    - Earth
    - Mars
    - Jupiter
    - Saturn
    - Uranus
    - Neptune
```

would be the same in JS

```json
{
  "Hello": "World",
  "Planets": {
    "Sol": [
      "Mercury",
      "Venus",
      "Earth",
      "Mars",
      "Jupiter",
      "Saturn",
      "Uranus",
      "Neptune"
    ]
  }
}
```

## YQ

You can do this:
```
yq . ./examples/yaml/collections.yaml
```

But you should probably do this when piping
```
sudo cat ./examples/yaml/collections.yaml | yq .
```


If we are converting to json
```
yq -o=json '.' ./examples/yaml/collections.yaml
```