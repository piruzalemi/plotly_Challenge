const urld = "data.csv";

// Fetch the JSON data and console log it
d3.csv(urld).then(function(data) {
  console.log(data);
});

// Promise Pending
const dataPromise = d3.csv(urld);
console.log("Data Promise: ", dataPromise);