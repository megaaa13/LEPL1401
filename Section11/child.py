class Child:
    def is_next_valid():
        # Implementation non fournie
        pass
    def next_child():
        # Implementation non fournie
        pass
def is_every_child_here(first_child):
    child = first_child
    while child.is_next_valid() and child.next_child() != first_child:
        child = child.next_child()
    if not child.is_next_valid():
        return False
    return True