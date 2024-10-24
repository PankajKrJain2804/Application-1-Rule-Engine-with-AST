from rule_engine import create_rule, combine_rules, evaluate_rule

if __name__ == "__main__":
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "salary > 50000 OR experience > 5"
    ast1 = create_rule(rule1)
    ast2 = create_rule(rule2)
    
    combined_ast = combine_rules([rule1, rule2])
    
    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(combined_ast, data)
    print(result)
