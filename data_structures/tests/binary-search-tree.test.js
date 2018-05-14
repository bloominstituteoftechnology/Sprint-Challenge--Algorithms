const BinarySearchTree = require('../src/binary-search-tree');

let bst;

describe('`depthFirstForEach` and `breadthFirstForEach`', () => {
  beforeEach(() => {
    bst = new BinarySearchTree(5);
  });

  test("`depthFirstForEach` executes a callback on every value in a tree in depth-first order", () => {
    const array = [];
    const cb = x => array.push(x);

    bst.insert(2);
    bst.insert(3);
    bst.insert(7);
    bst.insert(9);
    bst.depthFirstForEach(cb);

    expect(array).toEqual([5, 2, 3, 7, 9]);
  });

  test("`breadthFirstForEach` executes a callback on every value in a tree in breadth-first order", () => {
    const array = [];
    const cb = x => array.push(x);

    bst.insert(3);
    bst.insert(4);
    bst.insert(10);
    bst.insert(9);
    bst.insert(11);
    bst.breadthFirstForEach(cb);

    expect(array).toEqual([5, 3, 10, 4, 9, 11]);
  });
});