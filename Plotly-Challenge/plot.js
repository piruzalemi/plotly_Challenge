d3.json("samples.json").then((data) => {
  //  Create the Traces
  var trace1 = {
    x: data.otu_ids,
    y: data.sample_values,
    type: "box",
    name: "biodiversity from trace1",
    boxpoints: "all"
  };

  // Create the data array for the plot
  var data = [trace1];

  // Define the plot layout
  var layout = {
    title: "Alemi data.json Plots",
    xaxis: { title: "otu ids" },
    yaxis: { title: "Sample Values" }
  };

  // Plot the chart to a div tag with id "plot"
  Plotly.newPlot("plot", data, layout);
});
