def read_file(filename):
	chat = []
	with open(filename, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat

def covert(chat):
	new = []
	person = None
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read_file('input.txt')
	chat = covert(chat)
	write_file('output.txt', chat)

main()

