from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.path = []
        self.serial = ""
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Step 1: Build Trie
        root = TrieNode()
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
            node.path = path
        
        # Step 2: Serialize subtrees
        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            items = []
            for name in sorted(node.children):
                child = node.children[name]
                items.append(name + "(" + serialize(child) + ")")
            node.serial = "".join(items)
            serial_map[node.serial].append(node)
            return node.serial

        serialize(root)

        # Step 3: Mark duplicates
        for serial, nodes in serial_map.items():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Step 4: Collect remaining paths
        result = []

        def collect(node, curr):
            for name, child in node.children.items():
                if not child.deleted:
                    result.append(curr + [name])
                    collect(child, curr + [name])

        collect(root, [])
        return result
