const input = `0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2`;

const parseInput = (input) => {
  const result = input.split("\n").map((line) => {
    const partial_result = {};
    const coordinates = line.split(" -> ");
    coordinates.map((coordinate, i) => {
      if (i == 0) {
        partial_result.start = {
          x: coordinate.split(",")[0],
          y: coordinate.split(",")[1],
        };
      } else {
        partial_result.end = {
          x: coordinate.split(",")[0],
          y: coordinate.split(",")[1],
        };
      }
    });
    return partial_result;
  });
  return result;
};

const rules = parseInput(input);
let width = 0;
let height = 0;

rules.forEach((rule_set) => {
  for (set_label of Object.keys(rule_set)) {
    for (const [key, value] of Object.entries(rule_set[set_label])) {
      if (key === "x") {
        if (value > parseInt(width)) {
          width = value;
        }
      } else {
        if (value > parseInt(height)) {
          height = value;
        }
      }
    }
  }
});

board = [];
for (let y = 0; y < height; y++) {
  line = [];
  for (let x = 0; x < width; x++) {
    line.push(".");
  }
  board.push(line);
}

rules.forEach((rule_set) => {
  console.log(rule_set);
});
