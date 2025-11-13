from binary_tree_structure import Tree
from huffman import huffman

def encode(string):
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
    huffman_code = huffman(root)

    encoded_message = ''

    for elm in string:
        encoded_message += huffman_code[elm]

    return encoded_message

def decode(encode_message):
    pass


string = 'there should be text that needs to be encoded'

encode_message = encode(string)
print(f'encoded message: {encode_message}')

decode_message = decode(encode_message)
print(f'decode message: {decode_message}')