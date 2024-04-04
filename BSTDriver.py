from BinarySearchTree import BinarySearchTree

def main():
    print("\nCreating a new Binary Search Tree: ")
    mytree = BinarySearchTree()
    print("Inserting 45, 67, 22, 100, 75, 13, 11, 64, 30 into the tree...")
    mytree.insert(45)
    mytree.insert(67)
    mytree.insert(22)
    mytree.insert(100)
    mytree.insert(75)
    mytree.insert(13)
    mytree.insert(11)
    mytree.insert(64)
    mytree.insert(30)

    print("\nTREE TRAVERSALS:")

    print("Here is the preorder tree traversal: ")
    mytree.traverse_preorder(45)

    print("\nHere is the postorder tree traversal: ")
    mytree.traverse_postorder(45)

    print("\nHere is the inorder tree traversal: ")
    mytree.traverse_inorder(45)

    print("\n\nTREE LENGTH AND HEIGHT:")
    print(f"Tree length should be 9: {len(mytree)}")
    print(f"Tree current height should be 3: {mytree.current_height()}")
    print(f"Tree max height should be 3: {mytree.max_height()}")

    print(f"\nPrinting mytree with the display method...")
    mytree.root.display()

    print("DELETING ITEMS:")
    print("Deleting 67, 22, and 11...")
    mytree.delete(67)
    mytree.delete(22)
    mytree.delete(11)
    mytree.root.display()

    print(f"New tree length is: {len(mytree)}")
    print(f"New tree current height is: {mytree.current_height()}")
    print(f"New tree max height is: {mytree.max_height()}")


if __name__ == '__main__':
    main()
