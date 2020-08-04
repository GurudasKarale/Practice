var arr1=[[1,2,3],[4,5,6],[7,8,9]];
var arr2=[[1,2],[3,4],[5,6]];
//console.log(arr2);

var result=[[],[],[]];

for(var i=0;i<3;i++){
  
  for(var k=0;k<2;k++){
    
    var summ=0;
    
    for(var j=0;j<3;j++){
      
      summ+=arr1[i][j]*arr2[j][k];
      
    }
    result[i][k]=summ;
  }
}
console.log(result);