function sumStrings(a, b) {
  if (a === "") {
    a = BigInt(0);
  } else {
    a = BigInt(a);
  }
  if (b === "") {
    b = BigInt(0);
  } else {
    b = BigInt(b);
  }

  return (a + b).toString();
}

console.log(
  sumStrings("712569312664357328695151392", "8100824045303269669937")
);
