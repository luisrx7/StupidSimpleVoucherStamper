import hashlib
from rich import print

def generate_codes(initial_string,count=100,file_name="codes.txt",code_length=6,hash_type="sha256"):
    h = hashlib.new(hash_type)
    h.update(initial_string.encode('utf-8'))
    codes = []
    for i in range(count):
        codes.append(h.hexdigest())
        h.update(codes[i].encode('utf-8'))


    shorted_codes = []
    for i in range(len(codes)):
        shorted_code = codes[i][:code_length]
        print(f"{i+1} - {codes[i]} - {shorted_code}")
        if shorted_code not in shorted_codes:
            shorted_codes.append(shorted_code)
        else:
            print("Code already exists, choose a bigger code length or a different initial string")
            exit(1)

    with open(file_name, 'w') as f:
        for code in shorted_codes:
            f.write(code + "\n")


if __name__ == "__main__":
    generate_codes(initial_string="test")
