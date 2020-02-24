// Create two arrays, each of which will hold data for a different trace
var y0 = [];
var y1 = [];

// Fill each of the above arrays with randomly generated data
for (var i = 0; i < 50; i++) {
  y0.push(Math.random());
  y1.push(Math.random() + 0.2);
}

// Create a trace object with the data in `y0`
var trace1 = {
  y: y0,
  boxpoints: "all",
  type: "box",
  name:"Who1"
};

// Use `layout` to define a title
var layout = {
    title: "Piruz Alemi Box Plot",
    Name:"Piruz1"
  };

// Create a trace object with the data in `y1`
var trace2 = {
  y: y1,
  boxpoints: "all",
  type: "box",
  name:"Who2"
 
};

// Create a data array with the above two traces
var data = [trace1, trace2];



// Render the plot to the `plot1` div
Plotly.newPlot("plot1", data, layout);
// Use `layout` to define a title
var layout = {
    title: "Box TWO Plot",
    Name:"Piruz2"
  };
Plotly.newPlot("plot2", data, layout);

