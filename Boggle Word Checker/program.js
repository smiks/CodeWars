var x = [-1, -1, -1, 0, 0, 1, 1, 1];
var y = [-1, 0, 1, -1, 1, -1, 0, 1];
var taken = [];

function search(grid, posX, posY, currIndex, word){
	if(currIndex == word.length){
		return true;
	}
	var toLook = word[currIndex];
	/* check neighbours */
	for(var d=0; d<8; d++){
		var rd = posX+x[d],
		cd = posY+y[d];
		if(rd < 0 || rd >= grid.length || cd < 0 || cd >= grid[0].length){
			continue;
		}
		/* check neighbour */
		if(taken[rd][cd] === false && grid[rd][cd] == toLook){		
			var old_taken = taken;
			taken[rd][cd] = true;
			if(search(grid, rd, cd, currIndex+1, word)){
				return true;
			}
			taken = old_taken;
		}
	}
	return false;	
}


function checkWord( board, word ) {
	/* initialize taken */
	for(var row=0, lr=board.length; row<lr; row++){
		taken[row] = [];
		for(var col=0, lc=board[0].length; col<lc; col++){
			taken[row][col] = false;
		}
	}


	/* find first occurence */
	for(var row=0, lr=board.length; row<lr; row++){
		for(var col=0, lc=board[0].length; col<lc; col++){
			if(board[row][col] == word[0]){
				taken[row][col] = true;
				if(word.length == 1){
					return true;
				}
				if(search(board, row, col, 1, word)){
					return true;
				}else{
					for(var row2=0; row2<lr; row2++){
						for(var col2=0; col2<lc; col2++){
							taken[row2][col2] = false;
						}
					}
				}
			}
		}
	}
	return false;
}