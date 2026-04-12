function permutations(str) {
  if (str.length <= 1) {
    return [str];
  }

  const result = [];

  for (let i = 0; i < str.length; i++) {
    const fixed = str[i];
    const rest = str.slice(0, i) + str.slice(i + 1);
    const restPerms = permutations(rest);

    for (const p of restPerms) {
      result.push(fixed + p);
    }
  }

  return result;
}

console.log(permutations("abg"));