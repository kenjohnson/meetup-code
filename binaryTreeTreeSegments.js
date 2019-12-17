// Segment trees
// Given an array of leaf nodes like this:
//   [ 7,8, 9, 10, 11, 12, 13, 14] 
// sum a segment of those nodes. 
// Do this by building a binary
// tree around those leaf nodes. 
//              0
//        1             2
//     3     4      5      6
//    7 8   9 10  11 12  13 14 
// 
// Set the values of
// those nodes to the sum of the leaf nodes.
// For example, 
//  the value of 3 would be 15,
//  the value of 4 would be 19,
//  the value of 1 would be 34,
// If the segment you
// are summing is contained within a higher node of
// the tree, then just return the value in that higher node.
// For example, if you are summing 7-10, then return 
// the value in node 1 (which would be 34).  
// NOTE: Currently this works on arrays of even size
//       like 8.  
// To run on windows, bring up command prompt and do
// >node binaryTreeTreeSegments
"use strict";
class Node {

	constructor(value, end) {
		this.left = null;
		this.right = null;
		this.value = value;
		this.startSegment = 0;
		this.endSegment = end;
	}

	getLeft() {
		return this.left;
	}

	setLeft(n) {
		this.left = n;
	}

	getRight() {
		return this.right;
	}
	setRight(n) {
		this.right = n;
	}

	getValue() {
		return this.value;
	}

	setValue(value) {
		this.value = value;
	}

	getStartSegment() {
		return this.startSegment;
	}

	setStartSegment(n) {
		this.startSegment = n;
	}
 
    getEndSegment() {
		return this.endSegment;
	}
	setEndSegment(n) {
		this.endSegment = n;
	}

}

// recuriverly traverse the tree
// n - node
// l - left (start of desired segment)
// r - right (end of desired segment)
function traverse(n,l,r) {
	
	console.log("\nentering traverse, \n  array index: " + arr.indexOf(n) + " array val: " + n.getValue() + "\n  startSeg " +
		n.getStartSegment() + " endSegment " + n.getEndSegment() + "\n  range start " + l + " range end " + r );

	var sum = 0;
	var left = 0;
	var right = 0;

	// if segment totally within range
	if ( l <= n.getStartSegment() && n.getEndSegment() <= r ) {
		sum = n.getValue();
		console.log("     segment is totally within range. value is: " + sum );
		return sum;

	// if segment totally outside of range
	} else if (r < n.getStartSegment() || l > n.getEndSegment() ) {
       
       console.log("     segment is totally outside range.  left is: " + left + " right is: " + right );
	   //return left + right;
	   return 0;

	// if segment partially in range
	}  else {

	   if (n.getLeft()) {
		   left = traverse(n.getLeft(),l, r); 
	   }

	   if (n.getRight()) {
		   right = traverse(n.getRight(),l,r);  
	   }

	   console.log("     segment is partially in range. left is: " + left + " right is: " + right );
	   return left + right;
	}
}


// The purpose of this function is to determine the
// index of a node which may be several levels 
// below you in the tree. Specifically left most node.
//  
// i - index going from left to right at some given level 
// levels - tells you how many levels you will have to skip to 
//         get to the bottom.  
//
//  in skipping levels, you will see a pattern
//  skip 1 level     2*i +1 
//  skip 2 levels    2 * (2i + 1) + 1
//  skip 3 levels    2 * (2 * (2i + 1 ) + 1 ) + 1
// 
//  you can see a pattern. 
//  2**level *i + summation ( 2 **(n-1))  + 1
// 
function determineStartSeg(i, levels) {
    console.log(i, " ", levels);

    //var iFactor = 2**levels * i;
    var iFactor = Math.pow(2, levels) * i;
    var n = levels;
    
    // gets the summation for the sequence
    // I could have made the condition n> 0, then
    // on the last iteration, 2**(1-1) = 2**0 = 1; 
    // that will work, but  that was too tricky. 
    // Instead, I just added
    // that last 1 outside the while loop.  This leaves
    // just the sequence of the 2*2*... inside the while
    // loop, which makes it easier to understand. 
    // 
    var sum = 0;
    while(n>1) {
    	//sum = sum + 2**(n-1);
    	sum = sum + Math.pow(2, n-1);
    	n = n-1;
    }
    sum = sum + 1;
    console.log("determineStartSeg iFactor " + iFactor + "  sum " + sum);
    return iFactor + sum;
}

function determineEndSeg(i, levels){
    console.log(i, " ", levels);
    
    var iFactor = Math.pow(2, levels) * i;
    var n = levels;

    var sum = 0;
    while(n>1) {
    	sum = sum + Math.pow(2, n);
    	n = n-1;
    }
    sum = sum + 2;

    console.log("determineEndSeg, iFactor " + iFactor + "  sum " + sum);
    return iFactor + sum;
}

// This function takes your input array,
// and creates a binary tree data structure. This
// tree data structure is implemented as an
// array.
//
// Builds tree from the bottom up 
//
// returns the tree array 
// 
function buildTree( arrIn) {

	var arr = [];

	// Build the leaf nodes first 
	for ( var i =0; i < arrIn.length; i++) {
		var idx = arrIn.length - 1 + i;
		arr[idx] = new Node(i);
		arr[idx].setValue(arrIn[i]);
		arr[idx].setStartSegment(idx);
		arr[idx].setEndSegment(idx);
	}
	  
	// Now build up the rest of the tree above the leaf nodes

	var idx2 = arrIn.length;
    var reverseLevel = 1;

	// each iteration through this while loop
	// takes us 1 level up the tree, like
	// 3-6, 1-2, 0
	while ( idx2 > 1 ) {
 
		for (  i = idx2/2 -1; i< idx2-1; i++) { 
			arr[i] = new Node();
			arr[i].setValue(arr[2*i+1].getValue() + arr[2*i +2].getValue() );
			arr[i].setLeft( arr[2*i+1] );
			arr[i].setRight( arr[2*i+2] );

        
            var startSegIdx = determineStartSeg(i, reverseLevel);
            var endSegIdx = determineEndSeg(i, reverseLevel);
            
            arr[i].setStartSegment( startSegIdx );
			arr[i].setEndSegment( endSegIdx );

            console.log("** " + i + " reverseLevel " + reverseLevel + " startSegIndex: " + startSegIdx + " endSegIndex " + endSegIdx);
			
		}
	
	    idx2 = idx2 / 2;
        reverseLevel = reverseLevel + 1;
    
	}

	console.log("Completed building tree, tree looks like this.");
	for ( i = 0; i < arrIn.length *2 -1 ; i++){
		console.log("\nindex: " + i);
		console.log("  value: " + arr[i].getValue());
		console.log("  start seg: " + arr[i].getStartSegment());
		console.log("  end seg:   " + arr[i].getEndSegment() + "\n" ) ;
	}

	return arr;  // return the array representing the tree
}  //end buildTree

var inputLeaves = [ 7, 8, 9, 10, 11, 12, 13, 14];
var arr = [];
var arr = buildTree( inputLeaves);

// run the test

var i= 7; // start segment 
var j = 11; // end segment
var sum = 0;
sum = traverse(arr[0], i, j);
console.log("sum is " + sum );