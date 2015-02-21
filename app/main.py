import bottle
import json

@bottle.get('/')
def index():
	return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
	data = bottle.request.json

	return json.dumps({
		'name': 'battlesnake-python',
		'color': '#00ff00',
		'head_url': 'http://battlesnake-python.herokuapp.com',
		'taunt': 'battlesnake-python!'
	})


@bottle.post('/move')
def move():
	data = bottle.request.json
	
	default(data)

	return json.dumps({
		'move': 'left',
		'taunt': 'battlesnake-python!'
	})

our_name = "a1b1"
	
def default(data):
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
	

@bottle.post('/end')
def end():
	data = bottle.request.json

	return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
