const { BinarySearchTree, checkBalanced } = require('../src/binary-search-tree');

let bst;

describe('checkBalanced', () => {
  beforeEach(() => {
    bst = new BinarySearchTree(10);
  });

  test('checkBalanced returns true given a perfectly balanced tree', () => {
    expect(checkBalanced(bst)).toBe(true);

    bst.insert(11);
    bst.insert(9);

    expect(checkBalanced(bst)).toBe(true);
  });

  test('checkBalanced returns false given a tree that is not perfectly balanced', () => {
    bst.insert(11);
    bst.insert(12);
    expect(checkBalanced(bst)).toBe(false);

    bst.insert(9);
    expect(checkBalanced(bst)).toBe(false);
  });
});