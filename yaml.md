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