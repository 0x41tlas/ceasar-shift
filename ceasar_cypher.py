import string
import sys

def ceasar(text, shift):
	alph = string.ascii_lowercase
	s_alph = alph[shift:] + alph[:shift]
	table = string.maketrans(alph, s_alph)
	print text.lower().translate(table)

def main():
	text = ' '.join(sys.argv[1:])
	for i in range(26):
		ceasar(text, i)

main()
