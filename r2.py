def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines 

def convert(lines):
	person = None # 无，是个预设值
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_word_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == ''
				allen_sticker_count += 1
			else: 
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '贴图'
				viki_sticker_count += 1
			else
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen说了', allen_word_count, '传了', allen_sticker_count, '个贴图')
	print('viki说了', viki_word_count, '传了', viki_sticker_count, '个贴图')
	
#计数

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main() #程式的进入点