
// Create your own mad lib that collects (at least) the following information:
	// At least 2 strings */
	// At least 2 numbers */
// And includes the following elements:
	// One list/array */
	// One conditional statement with at least one logical operator */
	// One function */
	// Must return a value */
	// Must have and use parameters */
	// One loop */

function userInputs(){
	// create a variable data to hold the user inputs 
	var data = [];
	
	while(data.length < 3 && data != -1){
		// request user for input
		input1 = prompt("Please enter a number: ");
		// parse the string into an integer to satisfy the number requirement
		input1 = parseInt(input1);
		// push the collected data into the array
		data.push(input1);
		// request user for input
		input2 = prompt("Please enter an animal name in the plural. Example cats: ");
		// push the collected data into the array
		data.push(input2);
		// request user for input
		input3 = prompt("Please enter a number: ");
		// parse the string into an integer to satisfy the number requirement
		input3 = parseInt(input3);
		// push the collected data into the array
		data.push(input3);
		// request user for input
		input4 = prompt("Please enter an animal name in the plural. Example dogs: ");
		// push the collected data into the array
		data.push(input4);
		// request user for input
	}
	return data;
}

// defining the function makeIt() passing in one parameter, 'data'
function makeIt(d){
	// verify the function is running
	// console.log('the makeIt() function is running');
	
	// variables containing parts of the madlib to be used
	var part1="While I was walking down the street, I saw "
	var part2="and they were following "
	var part3="who were complaining about the weather in Boise."

	// the concatenation of the predefined components above and the values parsed from the string
	var madlib =
		part1 + input1 + " " + input2 + " " +  
		part2 + input3 + " " + input4 + " " + 
		part3;

	return madlib;	
}

// the variable data is both a container and a function call
// it will contain the output of the function userInputs once run
// that value will then be passed into the makeIt() function as an argument
var data = userInputs();
// logging 'data' for verification of data type 'Number' requirement
console.log(data);

// the variable madlib will equal the result of the makeIt() function
// the makeIt() function's output is contigent upon the argument 'data'
var madlib = makeIt(data);
// output the madlib, the desired result
console.log(madlib);


