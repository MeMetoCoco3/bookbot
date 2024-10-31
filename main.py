with open("books/frankenstein.txt", "r") as f:
	data = f.read()
print(len(data.split()))

counter = {}
for character in data:
	if not character.isalpha():
		continue
	if character.isupper():
		character = character.lower()
	if counter.get(character):
		counter[character] +=1
		continue
	counter[character] = 1

print("+++FRANKEINSTEIN REPORT+++")
print("Character counter:")
for k, v  in counter.items():
	print(f"'{k}': {v}")
print("---End of report---")
