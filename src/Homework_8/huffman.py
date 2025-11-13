def huffman(node, bin_str=''):
    if type(node) is str: 
        return {node: bin_str}
    
    left_children, right_children = node.children()

    dictionary = {}
    dictionary.update(huffman(left_children, bin_str + '0'))
    dictionary.update(huffman(right_children, bin_str + '1'))
    
    return dictionary
