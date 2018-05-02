class BinarySearchTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    const newNode = new BinarySearchTree(value);
    if (value < this.value) {
      if (!this.left) {
        this.left = newNode;
      } else {
        this.left.insert(value);
      }
    } else if (value >= this.value) {
      if (!this.right) {
        this.right = newNode;
      } else {
        this.right.insert(value);
      }
    }
  }

  contains(target) {
    if (this.value === target) {
      return true;
    }
    if (this.left) {
      if (this.left.contains(target)) {
        return true;
      }
    }
    if (this.right) {
      if (this.right.contains(target)) {
        return true;
      }
    }
    return false;
  }

  getMax() {
    if (!this) return null;

    let max = this.value;
    let current = this;

    while (current) {
      if (current.value > max) {
        max = current.value;
      }
      current = current.right;
    }

    return max;
  }

  depthFirstForEach(cb) {
    cb(this.value);
    if (this.left) {
      this.left.depthFirstForEach(cb);
    }
    if (this.right) {
      this.right.depthFirstForEach(cb);
    }
  }
}

/* Recursive Solution */
const checkBalanced = (rootNode) => {
  if (!rootNode) return true;

  const minDepth = (node) => {
    if (!node) return 0;
    return 1 + Math.min(minDepth(node.left), minDepth(node.right));
  };

  const maxDepth = (node) => {
    if (!node) return 0;
    return 1 + Math.max(maxDepth(node.left), maxDepth(node.right));
  }

  return (maxDepth(rootNode) - minDepth(rootNode) === 0);
};

/* Iterative Solution */
// const checkBalanced = (rootNode) => {
//   if (!rootNode) return true;
//   const depths = [];
//   const nodes = [];

//   nodes.push([rootNode, 0]);

//   while (nodes.length) {
//     const nodePair = nodes.pop();
//     const node = nodePair[0]; 
//     const depth = nodePair[1];

//     if (!node.left && !node.right) {
//       if (depths.indexOf(depth) < 0) {
//         depths.push(depth);

//         if ((depths.length > 2) || (depths.length === 2 && Math.abs(depths[0] - depths[1]) > 0)) {
//           return false;
//         }
//       }
//     } else {
//       if (node.left) {
//         nodes.push([node.left, depth + 1]);
//       }
//       if (node.right) {
//         nodes.push([node.right, depth + 1]);
//       }
//     }
//   }
//   return true;
// };

module.exports = {
  BinarySearchTree,
  checkBalanced,
}