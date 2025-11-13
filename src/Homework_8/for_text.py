from binary_tree_structure import Tree
from huffman import huffman


def dictionary(string):
    freq = {}
    for elm in string:
        freq[elm] = freq[elm] + 1 if elm in freq else 1

    freq = sorted(freq.items(), key=lambda x: x[1])

    nodes = freq[:]
    while len(nodes) > 1:
        elm1, freq1 = nodes.pop(0)
        elm2, freq2 = nodes.pop(0)

        node = Tree(elm1, elm2)
        nodes.append((node, freq1 + freq2))

        nodes.sort(key=lambda x: x[1])

    root = nodes[0][0]
    
    return huffman(root)


def encode(string):
    encoded_message = ''
    huffman_code = dictionary(string)

    for elm in string:
        encoded_message += huffman_code[elm]

    return encoded_message


def decode(string, encode_message):
    huffman_dict = dictionary(string)
    reversed_huffman_dict = {v: k for k, v in huffman_dict.items()} 
    decode_message = ''
    print(huffman_dict.items())

    current_elm = ''
    for i in range(0, len(encode_message)):
        current_elm += encode_message[i]
        if current_elm in huffman_dict.values():
            decode_message += reversed_huffman_dict.get(current_elm)
            current_elm = ''

    return decode_message


string = 'there should be text that needs to be encoded'

encode_message = encode(string)
print(f'encoded message: {encode_message}')

decode_message = decode(string, encode_message)
print(f'decode message: {decode_message}')
