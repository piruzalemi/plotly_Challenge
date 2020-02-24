// // Create an array of each country's numbers
// var data = {
//     us: {
//         Spotify: 19,
//         Soundcloud: 5,
//         Pandora: 8,
//         Itunes: 30
//     },

//     uk: {
//         Spotify: 10,
//         Soundcloud: 2,
//         Pandora: 22,
//         Itunes: 37
//     },

//     canada: {
//         Spotify: 14,
//         Soundcloud: 2,
//         Pandora: 5,
//         Itunes: 15
//     }
// };

var us = Object.values(data2.us);
var uk = Object.values(data2.uk);
var canada = Object.values(data2.canada);

// Create an array of music provider labels
var labels = Object.keys(data2.us);

// Display the default plot
function init() {
  var data2 = [{
    values: us,
    labels: labels,
    type: "pie"
  }];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.newPlot("pieplot", data2, layout);
}

// On change to the DOM, call getData()
d3.selectAll("#selDataset").on("change", getData);

// Function called by DOM changes
function getData() {
  var dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  var dataset = dropdownMenu.property("value");
  // ---------------------------------------------------
  // Initialize an empty array for the country's data
  // Not to confuse "data" as an array with data2 
  // defined inside the data file
  var dataSel = [];

  if (dataset == 'us') {
      dataSelected = us;
  }
  else if (dataset == 'uk') {
      dataSelected = uk;
  }
  else if (dataset == 'canada') {
      dataSelected = canada;
  }
  // Call function to update the chart
  updatePlotly(dataSelected);
}

// Update the restyled plot's values
function updatePlotly(newdata) {
  Plotly.restyle("pieplot", "values", [newdata]);
}

init();
