import bottle
import json
import sys

taunts = ["I'm Gonna Wreck-It!",
"I'm not from the candy tree department.",
"I am bad and that is good, I will never be good and...",
"...that's not bad, there's no one I'd rather be than me.",
"It's kind of hard to do your job...",
"...when nobody likes you for doing it.",
"I'm already happy, I got the coolest job in the world!",
"It may not be as fancy as being president,", 
"but I have a duty, a big duty!",
"I wonder how many licks it would take to get to your center?"]

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
		'head_url': 'https://raw.githubusercontent.com/alexlaj/battlesnake-python/master/ralph_full.png',
		'taunt': 'IM GUNNA WRECK IT!!!'
	})


@bottle.post('/move')
def move():
	data = bottle.request.json
	
	move = default(data)
	if (data['turn']%3 == 0):
		theTaunt = taunts[data['turn']/3 %10]
		return json.dumps({
			'move': move,
			'taunt': theTaunt
		})
	else:
		return json.dumps({
			'move': move
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
			# add depth here
			for space2 in temp:				
				if(space2[0] >= 0):
					curr_score += scores[space2[2]]
					temp2 = check_around(board, space2[0], space2[1])
					for good_space2 in temp2:
						curr_score += scores[good_space2[2]]
		if(curr_score > best_score):
			best_score = curr_score
			best_space = curr_space
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
	print(len(board[0]))
	print(len(board))
	is_wall = x < 0 or x > len(board[0]) - 1 or y < 0 or y > len(board) - 1 
	if(is_wall):
		return [-1, -1, "wall"]
	elif(board[x][y]["state"] in good_array):
		return [x, y, board[x][y]["state"]]
	return False
@bottle.post('/end')
def end():
	data = bottle.request.json

	return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
