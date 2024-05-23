production_rules = [
    2,  # 0. CODE -> DECL CODE
    0,  # 1. CODE -> ''
    3,  # 2. DECL -> vtype id VDECL
    3,  # 3. DECL -> vtype id FDECL
    1,  # 4. VDECL -> semi
    3,  # 5. VDECL -> assign RHS semi
    7,  # 6. FDECL -> lparen ARG rparen lbrace BLOCK RETURN rbrace
    1,  # 7. RHS -> EXPR
    1,  # 8. RHS -> literal
    1,  # 9. RHS -> character
    1,  # 10. RHS -> boolstr
    1,  # 11. EXPR -> TERM
    3,  # 12. EXPR -> EXPR addsub TERM
    1,  # 13. TERM -> FACTOR
    3,  # 14. TERM -> TERM multdiv FACTOR
    3,  # 15. FACTOR -> lparen EXPR rparen
    1,  # 16. FACTOR -> id
    1,  # 17. FACTOR -> num
    3,  # 18. ARG -> vtype id MOREARGS
    0,  # 19. ARG -> ''
    4,  # 20. MOREARGS -> comma vtype id MOREARGS
    0,  # 21. MOREARGS -> ''
    2,  # 22. BLOCK -> STMT BLOCK
    0,  # 23. BLOCK -> ''
    1,  # 24. STMT -> VDECL
    3,  # 25. STMT -> id assign semi
    8,  # 26. STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
    7,  # 27. STMT -> while lparen COND rparen lbrace BLOCK rbrace
    3,  # 28. COND -> COND comp COND'
    1,  # 29. COND -> COND'
    1,  # 30. COND' -> boolstr
    4,  # 31. ELSE -> else lbrace BLOCK rbrace
    0,  # 32. ELSE -> ''
    3   # 33. RETURN -> return RHS semi
]

production_lhs = [
    'CODE', 'CODE', 'DECL', 'DECL', 'VDECL',
    'VDECL', 'FDECL', 'RHS', 'RHS', 'RHS',
    'RHS', 'EXPR', 'EXPR', 'TERM', 'TERM', 
    'FACTOR', 'FACTOR', 'FACTOR', 'ARG', 'ARG', 
    'MOREARGS', 'MOREARGS', 'BLOCK', 'BLOCK', 'STMT',
    'STMT', 'STMT', 'STMT', 'COND', 'COND',
    'COND\'', 'ELSE', 'ELSE', 'RETURN'
]


# Action 테이블 ('state', 'input symbol') : ('rule', 'new state')
action_table = {
    (0, 'vtype'): ('shift', 2),
    (1, 'vtype'): ('shift', 2),    (1, '$'): ('reduce', 1),
    (2, 'id'): ('shift', 4),
    (3, '$'): ('accept', None),
    (4, 'semi'): ('shift', 7),    (4, 'assign'): ('shift', 8),    (4, 'lparen'): ('shift', 9),
    (5, 'vtype'): ('reduce', 2),    (5, '$'): ('reduce', 2),
    (6, 'vtype'): ('reduce', 3),    (6, '$'): ('reduce', 3),
    (7, 'vtype'): ('reduce', 4),    (7, 'id'): ('reduce', 4),    (7, 'semi'): ('reduce', 4),    (7, 'assign'): ('reduce', 4),    (7, 'rbrace'): ('reduce', 4),    (7, 'if'): ('reduce', 4),    (7, 'while'): ('reduce', 4),    (7, 'return'): ('reduce', 4),    (7, '$'): ('reduce', 4),
    (8, 'id'): ('shift', 18),    (8, 'lparen'): ('shift', 17),    (8, 'literal'): ('shift', 12),    (8, 'character'): ('shift', 13),    (8, 'boolstr'): ('shift', 14),    (8, 'num'): ('shift', 19),
    (9, 'vtype'): ('shift', 21),    (9, 'rparen'): ('reduce', 19),
    (10, 'semi'): ('shift', 22),
    (11, 'semi'): ('reduce', 7),   (11, 'addsub'): ('shift', 23),
    (12, 'semi'): ('reduce', 8),    
    (13, 'semi'): ('reduce', 9),    
    (14, 'semi'): ('reduce', 10),
    (15, 'semi'): ('reduce', 11),   (15, 'rparen'): ('reduce', 11),    (15, 'addsub'): ('reduce', 11),    (15, 'multdiv'): ('shift', 24),
    (16, 'semi'): ('reduce', 13),   (16, 'rparen'): ('reduce', 13),    (16, 'addsub'): ('reduce', 13),    (16, 'multdiv'): ('reduce', 13),
    (17, 'id'): ('shift', 18),    (17, 'lparen'): ('shift', 17),    (17, 'num'): ('shift', 19),
    (18, 'semi'): ('reduce', 16),   (18, 'rparen'): ('reduce', 16),    (18, 'addsub'): ('reduce', 16),    (18, 'multdiv'): ('reduce', 16),
    (19, 'semi'): ('reduce', 17),   (19, 'rparen'): ('reduce', 17),    (19, 'addsub'): ('reduce', 17),    (19, 'multdiv'): ('reduce', 17),
    (20, 'rparen'): ('shift', 26),
    (21, 'id'): ('shift', 27),
    (22, 'vtype'): ('reduce', 5),   (22, 'id'): ('reduce', 5),    (22, 'semi'): ('reduce', 5),    (22, 'assign'): ('reduce', 5),    (22, 'rbrace'): ('reduce', 5),    (22, 'if'): ('reduce', 5),    (22, 'while'): ('reduce', 5),    (22, 'return'): ('reduce', 5),    (22, '$'): ('reduce', 5),
    (23, 'id'): ('shift', 18),    (23, 'lparen'): ('shift', 17),    (23, 'num'): ('shift', 19),
    (24, 'id'): ('shift', 18),    (24, 'lparen'): ('shift', 17),    (24, 'num'): ('shift', 19),
    (25, 'rparen'): ('shift', 30),    (25, 'addsub'): ('shift', 23),
    (26, 'lbrace'): ('shift', 31),
    (27, 'rparen'): ('reduce', 21),    (27, 'comma'): ('shift', 33),
    (28, 'semi'): ('reduce', 12),    (28, 'rparen'): ('reduce', 12),    (28, 'addsub'): ('reduce', 12),    (28, 'multdiv'): ('shift', 24),
    (29, 'semi'): ('reduce', 14),    (29, 'rparen'): ('reduce', 14),    (29, 'addsub'): ('reduce', 14),    (29, 'multdiv'): ('reduce', 14),
    (30, 'semi'): ('reduce', 15),    (30, 'rparen'): ('reduce', 15),    (30, 'addsub'): ('reduce', 15),    (30, 'multdiv'): ('reduce', 15),
    (31, 'id'): ('shift', 37),    (31, 'semi'): ('shift', 7),    (31, 'assign'): ('shift', 8),    (31, 'rbrace'): ('reduce', 23),    (31, 'if'): ('shift', 38),    (31, 'while'): ('shift', 39),    (31, 'return'): ('reduce', 23),
    (32, 'rparen'): ('reduce', 18),
    (33, 'vtype'): ('shift', 40),
    (34, 'return'): ('shift', 42),
    (35, 'id'): ('shift', 37),    (35, 'semi'): ('shift', 7),    (35, 'assign'): ('shift', 8),    (35, 'rbrace'): ('reduce', 23),    (35, 'if'): ('shift', 38),    (35, 'while'): ('shift', 39),    (35, 'return'): ('reduce', 23),
    (36, 'id'): ('reduce', 24),    (36, 'semi'): ('reduce', 24),    (36, 'assign'): ('reduce', 24),    (36, 'rbrace'): ('reduce', 24),    (36, 'if'): ('reduce', 24),    (36, 'while'): ('reduce', 24),    (36, 'return'): ('reduce', 24),
    (37, 'assign'): ('shift', 44),
    (38, 'lparen'): ('shift', 45),
    (39, 'lparen'): ('shift', 46),
    (40, 'id'): ('shift', 47),
    (41, 'rbrace'): ('shift', 48),
    (42, 'rbrace'): ('reduce', 22),
    (42, 'id'): ('shift', 18),    (42, 'lparen'): ('shift', 17),    (42, 'literal'): ('shift', 12),    (42, 'character'): ('shift', 13),    (42, 'boolstr'): ('shift', 14),    (42, 'num'): ('shift', 19),    
    (43, 'rbrace'): ('reduce', 22),
    (44, 'semi'): ('shift', 50),
    (45, 'boolstr'): ('shift', 53),
    (46, 'boolstr'): ('shift', 53),
    (47, 'rparen'): ('reduce', 21),    (47, 'comma'): ('shift', 33),    
    (48, 'vtype'): ('reduce', 6),    (48, '$'): ('reduce', 6),
    (49, 'semi'): ('shift', 56),
    (50, 'id'): ('reduce', 25),    (50, 'semi'): ('reduce', 25), (50, 'assign'): ('reduce', 25), (50, 'rbrace'): ('reduce', 25), (50, 'if'): ('reduce', 25), (50, 'while'): ('reduce', 25), (50, 'return'): ('reduce', 25),
    (51, 'rparen'): ('shift', 57),    (51, 'comp'): ('shift', 58),
    (52, 'rparen'): ('reduce', 29),    (52, 'comp'): ('reduce', 29),
    (53, 'rparen'): ('reduce', 30),    (53, 'comp'): ('reduce', 30),
    (54, 'rparen'): ('shift', 59),    (54, 'comp'): ('shift', 58),
    (55, 'rparen'): ('reduce', 20),
    (56, 'rbrace'): ('reduce', 33),
    (57, 'lbrace'): ('shift', 60),
    (58, 'boolstr'): ('shift', 53),
    (59, 'lbrace'): ('shift', 62),
    (60, 'id'): ('shift', 37),    (60, 'semi'): ('shift', 7),    (60, 'assign'): ('shift', 8),    (60, 'rbrace'): ('reduce', 23),    (60, 'if'): ('shift', 38),    (60, 'while'): ('shift', 39),    (60, 'return'): ('reduce', 23),
    (61, 'rparen'): ('reduce', 28),
    (62, 'id'): ('shift', 37),    (62, 'semi'): ('shift', 7),    (62, 'assign'): ('shift', 8),    (62, 'rbrace'): ('reduce', 23),    (62, 'if'): ('shift', 38),    (62, 'while'): ('shift', 39),    (62, 'return'): ('reduce', 23),
    (63, 'rbrace'): ('shift', 65),
    (64, 'rbrace'): ('shift', 66),
    (65, 'id'): ('reduce', 32),    (65, 'semi'): ('reduce', 32),    (65, 'assign'): ('reduce', 32),    (65, 'rbrace'): ('reduce', 32),    (65, 'if'): ('reduce', 32),    (65, 'while'): ('reduce', 32),    (65, 'else'): ('shift', 68),    (65, 'return'): ('reduce', 32),
    (66, 'id'): ('reduce', 27),    (66, 'semi'): ('reduce', 27),    (66, 'assign'): ('reduce', 27),    (66, 'rbrace'): ('reduce', 27),    (66, 'if'): ('reduce', 27),    (66, 'while'): ('reduce', 27),    (66, 'return'): ('reduce', 27),
    (67, 'id'): ('reduce', 26),    (67, 'semi'): ('reduce', 26),    (67, 'assign'): ('reduce', 26),    (67, 'rbrace'): ('reduce', 26),    (67, 'if'): ('reduce', 26),    (67, 'while'): ('reduce', 26),    (67, 'return'): ('reduce', 26),
    (68, 'lbrace'): ('shift', 69),
    (69, 'id'): ('shift', 37),    (69, 'semi'): ('shift', 7),    (69, 'assign'): ('shift', 8),    (69, 'rbrace'): ('reduce', 23),    (69, 'if'): ('shift', 38),    (69, 'while'): ('shift', 39),    (69, 'return'): ('reduce', 23),
    (70, 'rbrace'): ('shift', 71),
    (71, 'id'): ('reduce', 31),    (71, 'semi'): ('reduce', 31),    (71, 'assign'): ('reduce', 31),    (71, 'rbrace'): ('reduce', 31),    (71, 'if'): ('reduce', 31),    (71, 'while'): ('reduce', 31),    (71, 'return'): ('reduce', 31),
}

### Goto 테이블 ('state', 'input symbol') : 'new state'
goto_table = {
    (0, 'DECL'): 1,
    (1, 'CODE'): 3,    (1, 'DECL'): 1,
    (4, 'VDECL'): 5,    (4, 'FDECL'): 6,
    (8, 'RHS'): 10,    (8, 'EXPR'): 11,    (8, 'TERM'): 15,    (8, 'FACTOR'): 16,
    (9, 'ARG'): 20,
    (17, 'EXPR'): 25,    (17, 'TERM'): 15,    (17, 'FACTOR'): 16,
    (23, 'TERM'): 28,    (23, 'FACTOR'): 16,    
    (24, 'FACTOR'): 29,    
    (27, 'MOREARGS'): 32,
    (31, 'VDECL'): 36,    (31, 'BLOCK'): 34,    (31, 'STMT'): 35,
    (34, 'RETURN'): 41,
    (35, 'VDECL'): 36,    (35, 'BLOCK'): 43,    (35, 'STMT'): 35,
    (42, 'RHS'): 49,    (42, 'EXPR'): 11,    (42, 'TERM'): 15,    (42, 'FACTOR'): 16,
    (45, 'COND'): 51,    (45, 'COND\''): 52,
    (46, 'COND'): 54,    (45, 'COND\''): 52,
    (47, 'MOREARGS'): 55,
    (58, 'COND\''): 61,
    (60, 'VDECL'): 36,    (60, 'BLOCK'): 64,    (60, 'STMT'): 35,
    (62, 'VDECL'): 36,    (62, 'BLOCK'): 64,    (62, 'STMT'): 35,
    (65, 'ELSE'): 67,
    (69, 'VDECL'): 36,    (69, 'BLOCK'): 70,    (69, 'STMT'): 35,
}

# Parse tree 만들기
# 1. Shift의 경우, Node를 만들어 stack에 push
# 2. Reduce의 경우, LHS를 기준으로 하나의 Node를 만들고, RHS의 token 수 만큼 pop 하면서 Parent, Child 지정. 다 끝나면 Push
class Node:
    def __init__(self, token):
        self.data = token
        self.child = []
        self.parent = None

    def addChild(self, child):
        self.child.append(child)

    def printTree(self):
        print(self.data + " ")
        for node in self.child:
            printTree(node)


def parse(tokens):
    stack = [0]  # 초기 상태
    treeStack = [] # Tree 구현에 필요한 Stack, 초기 상태
    tokens.append('$')  # 입력 끝을 나타내는 end marker
    cursor = 0

    while True:
        current_state = stack[-1]
        current_token = tokens[cursor]
        action_key = (current_state, current_token)
        if action_key in action_table:
            action, next_state = action_table[action_key]
            if action == 'shift':
                stack.append(next_state)  # 새 상태를 스택에 푸시
                node = Node(tokens[cursor])  # Shift의 경우, Token으로 Node를 만들어서 Push
                treeStack.append(node)
                cursor += 1  # 다음 토큰으로 이동
            elif action == 'reduce':
                nodeStack = []
                # reduce 액션 수행 (규칙의 길이만큼 스택에서 팝)
                # production_rules는 규칙의 길이를 저장한 배열
                production_rule_length = production_rules[next_state]
                for _ in range(production_rule_length):
                    stack.pop()
                    nodeStack.append(treeStack.pop())   # nodeStack에 뺀 만큼 push
                # goto_table에서 다음 상태를 찾아 스택에 푸시
                top_state = stack[-1]
                nonterminal = production_lhs[next_state]  # 이 규칙의 LHS
                parent = Node(nonterminal)    # 그 LHS로 Node를 만듦
                goto_key = (top_state, nonterminal)
                next_state = goto_table[goto_key]
                stack.append(next_state)
                for _ in range(production_rule_length):
                    child = nodeStack.pop()
                    child.parent = parent
                    parent.addChild(child)
                treeStack.append(parent)
            elif action == 'accept':
                print("Parsing successful!")
                global root
                root = treeStack.pop()
                return
            else:
                print("Syntax error!")
                return
        else:
            print("Syntax error at state", current_state, "with token", current_token)
            return

root = None
input_string = "vtype id assign num semi"
parse(input_string.split())
root.printTree()