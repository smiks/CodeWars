function smaller(arr) {
   var l = [],
       tmp;
       
       
   for(var i=0, ln=arr.length; i<ln; i++){
     
     tmp = 0;
     for(var j=i+1; j<ln; j++){
       if(arr[j] < arr[i])
         tmp += 1;
     }
     
     l.push(tmp)
   }
   
   return l;
}