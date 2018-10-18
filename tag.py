import re
def extract_hash_tags(text):
	d = re.findall(r"#(\w+)", text)
	return(d)

