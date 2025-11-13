from binary_tree_structure import Tree
from huffman import huffman


def dictionary(string: str) -> dict[str, str]:
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


def encode(string: str) -> tuple[str, dict[str, str]]:
    encoded_message = ''
    huffman_code = dictionary(string)

    for elm in string:
        encoded_message += huffman_code[elm]

    return encoded_message, huffman_code


def decode(encode_message: str, huffman_dict: dict[str, str]) -> str:
    reversed_huffman_dict = {v: k for k, v in huffman_dict.items()} 
    decode_message = ''

    current_elm = ''
    for i in range(0, len(encode_message)):
        current_elm += encode_message[i]
        if current_elm in huffman_dict.values():
            decode_message += reversed_huffman_dict[current_elm]
            current_elm = ''

    return decode_message


string = 'there should be text that needs to be encoded'

encode_message, dict = encode(string)
print(f'encoded message: {encode_message}\n\ndictionary: {dict}\n')

decode_message = decode(encode_message, dictionary(string))
print(f'decode message: {decode_message}')
