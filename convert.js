import CSVToJson from "csvtojson";
import FileSystem from "fs";

CSVToJson().fromFile("./source.csv").then(source =>{
console.log(source)
});
