import bottle
import json
import sys

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
		'name': our_name,
		'color': '#00ff00',
		'head_url': 'https://github.com/alexlaj/battlesnake-python/blob/master/ralph_full.png',
		'taunt': 'IM GUNNA WRECK IT!!!'
	})


@bottle.post('/move')
def move():
	data = bottle.request.json
	
	move = default(data)

	return json.dumps({
		'move': move,
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
	move = detect_bad(data, our_snake)
	sys.stdout.flush()
	return move

good_array = ["food", "empty"]
scores = { "head" : 0, "body" : 1, "wall" : 1.5, "empty" : 2, "food" : 3 }
def detect_bad(data, our_snake):
	board = data["board"]
	head = our_snake["coords"][0]
	head_x = head[0]
	head_y = head[1]
	good_spaces = check_around(board, head_x, head_y)
	print(good_spaces)
	print()
	best_space = 0
	best_score = 0
	curr_space = 0
	for space in good_spaces:
		curr_score = 0
		if(space[0] >= 0):
			curr_score = scores[space[2]]
			temp = check_around(board, space[0], space[1])
			for good_space in temp:
				curr_score += scores[good_space[2]]
		if(curr_score > best_score):
			best_score = curr_score
			best_space = curr_space
		print(curr_score)
		curr_space += 1
	move_space = good_spaces[best_space]
	return map_direction(head_x, head_y, move_space[0], move_space[1])

def map_direction(head_x, head_y, x, y):
	if(x < head_x):
		return "left"
	elif(y < head_y):
		return "up"
	elif(x > head_x):
		return "right"
	elif(y > head_y):
		return "down"

def check_around(board, x, y):
	good_spaces = []
	if(x < 0 or y < 0):
		return good_spaces
	#check left
	space = check_space(board, x-1, y)
	if(space != False):
		good_spaces.append(space)
	#check up
	space = check_space(board, x, y+1)
	if(space != False):
		good_spaces.append(space)
	#check right
	space = check_space(board, x+1, y)
	if(space != False):
		good_spaces.append(space)
	#check down
	space = check_space(board, x, y-1)
	if(space != False):
		good_spaces.append(space)
	
	return good_spaces

def check_space(board, x, y):
	is_wall = not(x > 0 or x < len(board[0]) or y > 0 or y < len(board)) 
	if(is_wall):
		return [-1, -1, "wall"]
	if(board[x][y]["state"] in good_array):
		return [x, y, board[x][y]["state"]]
	return False
@bottle.post('/end')
def end():
	data = bottle.request.json

	return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
