def huffman(node, bin_str=''):
    if type(node) is str: 
        return {node: bin_str}
    
    l, r = node.children()

    dictionary = {}
    dictionary.update(huffman(l, bin_str + '0'))
    dictionary.update(huffman(r, bin_str + '1'))
    
    return dictionary