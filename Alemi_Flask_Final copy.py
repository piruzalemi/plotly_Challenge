<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Flask Plotlyjs Example</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>

<body>

  <div class="container">
    <div class="row">
      <div class="col-md-12 jumbotron text-center">
        <h2>Belly Button Biodiversity Dashboard</h2>
        <h3>Explore the Wild Life!</h3>

        <h3>Select your sample number from the dropdown menu:</h3>
        <p>Use the interactive charts below to explore the dataset</p>
      </div>
    </div>
    <div class="row">
      <div class="col-md-2">
        <div class="well">
          <h5>SELECT Sample:</h5>
          <select id="selDataset" onchange="optionChanged(this.value)"></select>
        </div>
        <div class="panel panel-primary">
          <div class="panel-heading">
            <h3 class="panel-title">Sample MetaData</h3>
          </div>
          <div id="sample-metadata" class="panel-body"></div>
        </div>
      </div>
      <div class="col-md-5">
        <div id="pie"></div>
      </div>
      <div class="col-md-5">
        <div id="gauge"></div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <div id="bubble"></div>
    </div>
  </div>

    <script src="https://cdn.plot.ly/plotly-1.31.2.min.js"></script> 
    <script src="https://d3js.org/d3.v5.min.js"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/5.5.0/d3.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/5.9.7/d3.min.js"></script>

    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    
    <script src="{{ url_for('static', filename='js/bonus.js') }}"></script>
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
  
</body>

</html>
