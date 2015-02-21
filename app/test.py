def test(data):	
	snake_dict = {}
	snakes = data["snakes"]
	our_snake = {}
	for snake in snakes:
		snake_dict[snake["name"]] = snake
		if snake["name"] == our_name:
			our_snake = snake
	print(snakes)
	print()
	print(our_snake)
our_name = 'a1b1'
data = {
  "game_id": "hairy-cheese",
  "turn": 1,
  "board": [],
  "snakes":[
{
  "name": "Noodlez",
  "state": "alive",
  "coords": [[0, 0], [0, 1], [0, 2], [1, 2]],
  "score": 4,
  "color": "#ff0000",
  "head_url": "http://img.server.com/snake_head.png",
  "taunt": "I'm one slippery noodle"
},{
  "name": "a1b1",
  "state": "alive",
  "coords": [[0, 0], [0, 1], [0, 2], [1, 2]],
  "score": 4,
  "color": "#ff0000",
  "head_url": "http://img.server.com/snake_head.png",
  "taunt": "I'm one slippery noodle"
},{
  "name": "lulz",
  "state": "alive",
  "coords": [[0, 0], [0, 1], [0, 2], [1, 2]],
  "score": 4,
  "color": "#ff0000",
  "head_url": "http://img.server.com/snake_head.png",
  "taunt": "I'm one slippery noodle"
}],
  "food": [[1, 4], [3, 0], [5, 2]]
}

test(data)
