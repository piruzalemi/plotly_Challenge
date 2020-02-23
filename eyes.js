var trace1 = {

 eyeColor: ["Brown", "Brown", "Brown", "Brown", "Brown",
  "Brown", "Brown", "Brown", "Green", "Green",
  "Green", "Green", "Green", "Blue", "Blue",
  "Blue", "Blue", "Blue", "Blue"],

eyeFlicker: [26.8, 27.9, 23.7, 25, 26.3, 24.8,
  25.7, 24.5, 26.4, 24.2, 28, 26.9,
  29.1, 25.7, 27.2, 29.9, 28.5, 29.4, 28.3],
  type: "bar"
};

// @TODO: Complete the Following Steps

// Create the Trace

// Create the data array for our plot

var data = [trace1];
  
  var layout = {
    title: "'Bar' Chart"
  };
  
  //Plotly.newPlot("plot-Div", data, layout);
  Plotly.newPlot("plot-div", data, layout);

// Define our plot layout

// Plot the chart to a div tag with id "bar-plot"

// Part 1
// var trace1 = {
//     x: ["beer", "wine", "martini", "margarita",
//       "ice tea", "rum & coke", "mai tai", "gin & tonic"],
//     y: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
//     type: "bar"
//   };
  
  
