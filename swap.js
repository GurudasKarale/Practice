var str="abc";
arr=str.split('');
neww=arr.join('');
console.log(neww);

for(var i=0;i<3;i++){
  
  
  console.log(arr[i]);
  
}

[arr[1],arr[2]]=[arr[2],arr[1]];
console.log(arr.join(''));