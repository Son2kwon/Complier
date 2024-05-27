import sys


production_rules = [
    2,  # 0. CODE -> DECL CODE
    0,  # 1. CODE -> ''
    2,  # 2. DECL -> VDECL semi
    1,  # 3. DECL -> FDECL
    2,  # 4. VDECL -> vtype id
    2,  # 5. VDECL -> vtype ASSIGN
    3,  # 6. ASSIGN -> id assign RHS
    9,  # 7. FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
    1,  # 8. RHS -> EXPR
    1,  # 9. RHS -> literal
    1,  # 10. RHS -> character
    1,  # 11. RHS -> boolstr
    1,  # 12. EXPR -> TERM
    3,  # 13. EXPR -> EXPR addsub TERM
    1,  # 14. TERM -> FACTOR
    3,  # 15. TERM -> TERM multdiv FACTOR
    3,  # 16. FACTOR -> lparen EXPR rparen
    1,  # 17. FACTOR -> id
    1,  # 18. FACTOR -> num
    3,  # 19. ARG -> vtype id MOREARGS
    0,  # 20. ARG -> ''
    4,  # 21. MOREARGS -> comma vtype id MOREARGS
    0,  # 22. MOREARGS -> ''
    2,  # 23. BLOCK -> STMT BLOCK
    0,  # 24. BLOCK -> ''
    2,  # 25. STMT -> VDECL semi
    2,  # 26. STMT -> ASSIGN semi
    8,  # 27. STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
    7,  # 28. STMT -> while lparen COND rparen lbrace BLOCK rbrace
    3,  # 29. COND -> COND comp COND'
    1,  # 30. COND -> COND'
    1,  # 31. COND' -> boolstr
    4,  # 32. ELSE -> else lbrace BLOCK rbrace
    0,  # 33. ELSE -> ''
    3   # 34. RETURN -> return RHS semi
]

production_lhs = [
    'CODE', 'CODE', 'DECL', 'DECL', 'VDECL',
    'VDECL', 'ASSIGN', 'FDECL', 'RHS', 'RHS', 
    'RHS', 'RHS', 'EXPR', 'EXPR', 'TERM',
    'TERM', 'FACTOR', 'FACTOR', 'FACTOR', 'ARG',
    'ARG', 'MOREARGS', 'MOREARGS', 'BLOCK', 'BLOCK',
    'STMT', 'STMT', 'STMT', 'STMT', 'COND',
    'COND', 'COND\'', 'ELSE', 'ELSE', 'RETURN'
]


# Action 테이블 ('state', 'input symbol') : ('rule', 'new state')
action_table = {
    (0, 'vtype'): ('shift', 4),
    (1, 'vtype'): ('shift', 4),    (1, '$'): ('reduce', 1),
    (2, 'semi'): ('shift', 6),
    (3, 'vtype'): ('reduce', 3),    (3, '$'): ('reduce', 3),
    (4, 'id'): ('shift', 7),    (4, 'assign'): ('shift', 8),    (4, 'lparen'): ('shift', 9),
    (5, '$'): ('accept', None),
    (6, 'vtype'): ('reduce', 2),    (6, '$'): ('reduce', 2),
    (7, 'semi'): ('reduce', 4),    (7, 'assign'): ('shift', 10),    (7, 'lparen'): ('shift', 9),
    (8, 'semi'): ('reduce', 5),
    (9, 'vtype'): ('shift', 12),    (9, 'rparen'): ('reduce', 20),
    (10, 'id'): ('shift', 21),    (10, 'lparen'): ('shift', 20),    (10, 'literal'): ('shift', 15),    (10, 'character'): ('shift', 16),    (10, 'boolstr'): ('shift', 17),    (10, 'num'): ('shift', 22),
    (11, 'rparen'): ('shift', 23),
    (12, 'id'): ('shift', 24),    
    (13, 'semi'): ('reduce', 6), 
    (14, 'semi'): ('reduce', 8),    (14, 'addsub'): ('shift', 25),
    (15, 'semi'): ('reduce', 9),
    (16, 'semi'): ('reduce', 10),
    (17, 'semi'): ('reduce', 11),
    (18, 'semi'): ('reduce', 12),   (18, 'rparen'): ('reduce', 12),    (18, 'addsub'): ('reduce', 12),    (18, 'multdiv'): ('reduce', 26),
    (19, 'semi'): ('reduce', 14),   (19, 'rparen'): ('reduce', 14),    (19, 'addsub'): ('reduce', 14),    (19, 'multdiv'): ('reduce', 14),
    (20, 'id'): ('shift', 21),    (20, 'lparen'): ('shift', 20),    (20, 'num'): ('shift', 22),
    (21, 'semi'): ('reduce', 17),   (21, 'rparen'): ('reduce', 17),    (21, 'addsub'): ('reduce', 17),    (21, 'multdiv'): ('reduce', 17),
    (22, 'semi'): ('reduce', 18),   (22, 'rparen'): ('reduce', 18),    (22, 'addsub'): ('reduce', 18),    (22, 'multdiv'): ('reduce', 18),
    (23, 'lbrace'): ('shift', 28),
    (24, 'rparen'): ('reduce', 22),   (24, 'comma'): ('shift', 30),
    (25, 'id'): ('shift', 21),    (25, 'lparen'): ('shift', 20),   (25, 'num'): ('shift', 22),
    (26, 'id'): ('shift', 21),    (26, 'lparen'): ('shift', 20),   (26, 'num'): ('shift', 22),
    (27, 'rparen'): ('shift', 33),    (27, 'addsub'): ('shift', 25),
    (28, 'vtype'): ('shift', 40),    (28, 'id'): ('shift', 41),    (28, 'rbrace'): ('reduce', 24),    (28, 'if'): ('shift', 38),    (28, 'while'): ('shift', 39),    (28, 'return'): ('reduce', 24),
    (29, 'rparen'): ('reduce', 19),
    (30, 'vtype'): ('shift', 42),
    (31, 'semi'): ('reduce', 13),    (31, 'rparen'): ('reduce', 13),    (31, 'addsub'): ('reduce', 13),    (31, 'multdiv'): ('shift', 26),
    (32, 'semi'): ('reduce', 15),    (32, 'rparen'): ('reduce', 15),    (32, 'addsub'): ('reduce', 15),    (32, 'multdiv'): ('reduce', 15),
    (33, 'semi'): ('reduce', 16),    (33, 'rparen'): ('reduce', 16),    (33, 'addsub'): ('reduce', 16),    (33, 'multdiv'): ('reduce', 16),
    (34, 'return'): ('shift', 44),
    (35, 'vtype'): ('shift', 40),    (35, 'id'): ('shift', 41),    (35, 'rbrace'): ('reduce', 24),    (35, 'if'): ('shift', 38),    (35, 'while'): ('shift', 39),    (35, 'return'): ('reduce', 24),
    (36, 'semi'): ('shift', 46),
    (37, 'semi'): ('shift', 47),
    (38, 'lparen'): ('shift', 48),
    (39, 'lparen'): ('shift', 49),
    (40, 'id'): ('shift', 50),
    (41, 'assign'): ('shift', 10),
    (42, 'id'): ('shift', 51),
    (43, 'rbrace'): ('shift', 52),
    (44, 'id'): ('shift', 21),    (44, 'lparen'): ('shift', 20),    (44, 'literal'): ('shift', 15),    (44, 'character'): ('shift', 16),    (44, 'boolstr'): ('shift', 17),    (44, 'num'): ('shift', 22),    
    (45, 'rbrace'): ('reduce', 23),    (45, 'return'): ('reduce', 23),
    (46, 'vtype'): ('reduce', 25),    (46, 'id'): ('reduce', 25),    (46, 'rbrace'): ('reduce', 25), (46, 'if'): ('reduce', 25), (46, 'while'): ('reduce', 25), (46, 'return'): ('reduce', 25),
    (47, 'vtype'): ('reduce', 26),    (47, 'id'): ('reduce', 26),    (47, 'rbrace'): ('reduce', 26), (47, 'if'): ('reduce', 26), (47, 'while'): ('reduce', 26), (47, 'return'): ('reduce', 26),
    (48, 'boolstr'): ('shift', 56),
    (49, 'boolstr'): ('shift', 56),
    (50, 'semi'): ('reduce', 4),    (50, 'assign'): ('shift', 10),
    (51, 'rparen'): ('reduce', 22),    (51, 'comma'): ('shift', 30),    
    (52, 'vtype'): ('reduce', 7),    (52, '$'): ('reduce', 7),
    (53, 'semi'): ('shift', 59),
    (54, 'rparen'): ('shift', 60),    (54, 'comp'): ('shift', 61),
    (55, 'rparen'): ('reduce', 30),    (55, 'comp'): ('reduce', 30),
    (56, 'rparen'): ('reduce', 31),    (56, 'comp'): ('reduce', 31),
    (57, 'rparen'): ('shift', 62),    (57, 'comp'): ('shift', 61),
    (58, 'rparen'): ('reduce', 21),
    (59, 'rbrace'): ('reduce', 34),
    (60, 'lbrace'): ('shift', 63),
    (61, 'boolstr'): ('shift', 56),
    (62, 'lbrace'): ('shift', 65),
    (63, 'vtype'): ('shift', 40),    (63, 'id'): ('shift', 41),    (63, 'rbrace'): ('reduce', 24),    (63, 'if'): ('shift', 38),    (63, 'while'): ('shift', 39),    (63, 'return'): ('reduce', 24),
    (64, 'rparen'): ('reduce', 29),    (64, 'comp'): ('reduce', 29),
    (65, 'semi'): ('shift', 40),    (65, 'id'): ('shift', 41),    (65, 'rbrace'): ('reduce', 24),    (65, 'if'): ('shift', 38),    (65, 'while'): ('shift', 39),    (65, 'return'): ('reduce', 24),
    (66, 'rbrace'): ('shift', 68),
    (67, 'rbrace'): ('shift', 69),
    (68, 'vtype'): ('reduce', 33),    (68, 'id'): ('reduce', 33),    (68, 'rbrace'): ('reduce', 33),    (68, 'if'): ('reduce', 33),    (68, 'while'): ('reduce', 33),    (68, 'else'): ('shift', 71),    (68, 'return'): ('reduce', 33),
    (69, 'vtype'): ('reduce', 28),    (69, 'semi'): ('reduce', 28),    (69, 'rbrace'): ('reduce', 28),    (69, 'if'): ('reduce', 28),    (69, 'while'): ('reduce', 28),    (69, 'return'): ('reduce', 28),
    (70, 'id'): ('reduce', 27),    (70, 'semi'): ('reduce', 27),    (70, 'rbrace'): ('reduce', 27),    (70, 'if'): ('reduce', 27),    (70, 'while'): ('reduce', 27),    (70, 'return'): ('reduce', 27),
    (71, 'lbrace'): ('shift', 72),
    (72, 'vtype'): ('shift', 40),    (72, 'id'): ('shift', 41),    (72, 'rbrace'): ('reduce', 24),    (72, 'if'): ('shift', 38),    (72, 'while'): ('shift', 39),    (72, 'return'): ('reduce', 24),
    (73, 'rbrace'): ('shift', 74),
    (74, 'vtype'): ('reduce', 32),    (74, 'id'): ('reduce', 32),    (74, 'rbrace'): ('reduce', 32),    (74, 'if'): ('reduce', 32),    (74, 'while'): ('reduce', 32),    (74, 'return'): ('reduce', 32),
}

### Goto 테이블
goto_table = {
    (0, 'DECL'): 1,    (0, 'VDECL'): 2,    (0, 'FDECL'): 3,
    (1, 'CODE'): 5,    (1, 'DECL'): 1,    (1, 'VDECL'): 2,     (1, 'FDECL'): 3,
    (4, 'ASSIGN'): 8,
    (9, 'ARG'): 11,
    (10, 'RHS'): 13,    (10, 'EXPR'): 14,    (10, 'TERM'): 18,    (10, 'FACTOR'): 19,
    (20, 'EXPR'): 27,    (20, 'TERM'): 18,    (20, 'FACTOR'): 19,
    (24, 'MOREARGS'): 29,
    (25, 'TERM'): 31,    (25, 'FACTOR'): 19,
    (26, 'FACTOR'): 32,
    (28, 'VDECL'): 36,    (28, 'ASSIGN'): 37,    (28, 'BLOCK'): 34,    (28, 'STMT'): 35,
    (34, 'RETURN'): 43,    
    (35, 'VDECL'): 36,    (35, 'ASSIGN'): 37,    (35, 'BLOCK'): 45,    (35, 'STMT'): 35,
    (40, 'ASSIGN'): 8,
    (44, 'RHS'): 53,    (44, 'EXPR'): 14,    (44, 'TERM'): 18,    (44, 'FACTOR'): 19,
    (48, 'COND'): 54,    (48, 'COND\''): 55,
    (49, 'COND'): 57,    (49, 'COND\''): 55,
    (51, 'MOREARGS'): 58,
    (61, 'COND\''): 64,
    (63, 'VDECL'): 36,    (63, 'BLOCK'): 37,    (63, 'BLOCK'): 66,    (63, 'STMT'): 35,
    (65, 'VDECL'): 36,    (65, 'BLOCK'): 37,    (65, 'BLOCK'): 67,    (65, 'STMT'): 35,
    (68, 'ELSE'): 70,
    (72, 'VDECL'): 36,    (72, 'BLOCK'): 37,    (72, 'BLOCK'): 73,    (72, 'STMT'): 35,
}


class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, level=0):
        print('  ' * level + self.symbol)
        for child in self.children:
            child.print_tree(level + 1)

def parse(tokens):
    stack = [0]  # 초기 상태
    tree_stack = []  # 트리 노드를 저장할 스택
    tokens.append('$')  # 입력 끝을 나타내는 엔드마커
    cursor = 0

    while True:
        current_state = stack[-1]
        current_token = tokens[cursor]
        action_key = (current_state, current_token)
        
        if action_key in action_table:
            action, next_state = action_table[action_key]
            if action == 'shift':
                stack.append(next_state)
                tree_stack.append(Node(current_token))
                cursor += 1

            elif action == 'reduce':
                production_rule_length = production_rules[next_state]
                children = []
                for _ in range(production_rule_length):
                    stack.pop()
                    children.append(tree_stack.pop())

                lhs = production_lhs[next_state]
                node = Node(lhs)
                for child in reversed(children):
                    node.add_child(child)
                tree_stack.append(node)

                top_state = stack[-1]
                nonterminal = lhs
                goto_key = (top_state, nonterminal)
                if goto_key in goto_table:
                    next_state = goto_table[goto_key]
                    stack.append(next_state)
                else:
                    print(f"Syntax error: Missing goto entry for {goto_key} at token index {cursor}")
                    return

            elif action == 'accept':
                root = Node('CODE')
                for node in tree_stack:
                    root.add_child(node)
                print("Parsing successful!")
                root.print_tree()
                return

            else:
                print(f"Syntax error at state {current_state} with token {current_token} at token index {cursor}")
                return
        else:
            print(f"Syntax error at state {current_state} with token {current_token} at token index {cursor}")
            return

def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content.split()
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main(filename):
    tokens = read_input_file(filename)
    parse(tokens)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: syntax_analyzer <input file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    main(filename)