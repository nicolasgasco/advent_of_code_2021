// Never again with JavaScript, I swear
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

// Make object out of coordinates
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

// Calculate height and width of board
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
width = parseInt(width) + 1;
height = parseInt(height) + 1;

// Populate board with dots
board = [];
for (let y = 0; y < height; y++) {
  line = [];
  for (let x = 0; x < width; x++) {
    line.push(".");
  }
  board.push(line);
}

// Put 1 if dot, increase if it's number
const markPosition = (position) => {
  if (position === ".") {
    return "1";
  } else {
    return (parseInt(position) + 1).toString();
  }
};

// Draw lines
rules.forEach((rule_set) => {
  // For every line
  console.log(rule_set);
  for (let y = 0; y < height; y++) {
    // For every dot
    for (let x = 0; x < width; x++) {
      // In case y is fixed
      if (rule_set.start.y === rule_set.end.y) {
        // Establish smallest and biggest number and draw line
        const smallest =
          parseInt(rule_set.start.x) < parseInt(rule_set.end.x)
            ? parseInt(rule_set.start.x)
            : parseInt(rule_set.end.x);
        const biggest =
          parseInt(rule_set.start.x) > parseInt(rule_set.end.x)
            ? parseInt(rule_set.start.x)
            : parseInt(rule_set.end.x);
        if (x >= smallest && x <= biggest && y == rule_set.start.y) {
          board[y][x] = markPosition(board[y][x]);
        }
        // In case x is fixed
      } else if (rule_set.start.x === rule_set.end.x) {
        // Establish smallest and biggest number and draw line
        const smallest =
          parseInt(rule_set.start.y) < parseInt(rule_set.end.y)
            ? parseInt(rule_set.start.y)
            : parseInt(rule_set.end.y);
        const biggest =
          parseInt(rule_set.start.y) > parseInt(rule_set.end.y)
            ? parseInt(rule_set.start.y)
            : parseInt(rule_set.end.y);
        if (y >= smallest && y <= biggest && x == rule_set.start.x) {
          board[y][x] = markPosition(board[y][x]);
        }
      } else if (
        rule_set.start.x === rule_set.start.y &&
        rule_set.end.x == rule_set.end.y
      ) {
        const smallest =
          parseInt(rule_set.start.x) < parseInt(rule_set.end.x)
            ? parseInt(rule_set.start.x)
            : parseInt(rule_set.end.x);
        const biggest =
          parseInt(rule_set.start.x) > parseInt(rule_set.end.x)
            ? parseInt(rule_set.start.x)
            : parseInt(rule_set.end.x);

        if (x === y && x >= smallest && x <= biggest)
          board[y][x] = markPosition(board[y][x]);
      } else if (
        rule_set.start.x === rule_set.end.y &&
        rule_set.start.y === rule_set.end.x
      ) {
        const smallest =
          parseInt(rule_set.start.x) < parseInt(rule_set.start.y)
            ? parseInt(rule_set.start.x)
            : parseInt(rule_set.start.y);
        const biggest =
          parseInt(rule_set.start.x) > parseInt(rule_set.start.y)
            ? parseInt(rule_set.start.x)
            : parseInt(rule_set.start.y);
        if ()
          board[y][x] = markPosition(board[y][x]);
      }
    }
    console.log(JSON.stringify(board[y]));
  }
});

// Count fields with 2 or higer
result = 0;
for (let y = 0; y < height; y++) {
  for (let x = 0; x < width; x++) {
    if (parseInt(board[y][x]) >= 2) {
      result++;
    }
  }
}

console.log(result);
