if False:
    def visit_tree(tree : dict[int,list],n: int) :
        left_child,right_child = tree[n]
        if left_child :
            visit_tree(tree,left_child)
        if right_child:
            visit_tree(tree,right_child)


tree : dict = {1:[2,3],2:[4,5],3 :{None,None},4 : {None,None},5 :{None,None}}   
#visit_tree(tree,1)     


def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    result = {}
    stack: list[int] = [root]
    while stack: # while len(stack) != 0
        curr_node = stack.pop(0)
        if curr_node:
            left_child, right_child =\
                tree[curr_node]
            if left_child: 
                stack.append(left_child)
            if right_child:
                stack.append(right_child)
    return result            

