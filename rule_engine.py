from ast_node import ASTNode

def create_rule(rule_string):
    tokens = rule_string.split()
    root = ASTNode("operator", tokens[1])
    root.left = ASTNode("operand", {tokens[0]: tokens[2]})
    root.right = ASTNode("operand", {tokens[4]: tokens[5]})
    return root

def combine_rules(rules):
    combined_root = ASTNode("operator", "AND")
    current = combined_root
    
    for rule_string in rules:
        if current.left is None:
            current.left = create_rule(rule_string)
        else:
            current.right = create_rule(rule_string)
            new_node = ASTNode("operator", "AND")
            new_node.left = current
            current = new_node
    
    return combined_root

def evaluate_rule(ast, data):
    if ast.node_type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    elif ast.node_type == "operand":
        for key, value in ast.value.items():
            if key in data and data[key] == value:
                return True
    return False
