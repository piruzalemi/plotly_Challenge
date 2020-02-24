


var arr = [10, 100, 1000];

for (var i = 0; i < arr.length; i++) {
    sum=sum + arr[i]
  console.log(Math.floor(Math.random() * arr[i]));
}

// Or

for (var i = 0; i < arr.length; i++) {
  console.log(Math.round(Math.random() * arr[i]));
}
