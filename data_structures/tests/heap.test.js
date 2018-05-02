const { heapsort } = require('../src/heap');

const generateRandomInput = (length, max) => {
  const input = new Array(length);
  for (let i = 0; i < length; i++) {
    input[i] = ~~(Math.random() * (~~max));
  }
  return input;
};

const isSorted = (arr) => {
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i+1]) return false;
  }
  return true;
};

describe('heapsort', () => {
  test('heapsort correctly sorts an array of integers', () => {
    const input = generateRandomInput(20, 100);
    expect(isSorted(heapsort(input))).toBe(true);
  });
});