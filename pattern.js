
class pattern{
  
  constructor(str,test,n,m){
    
    this.str=str;
    this.test=test;
    this.n=n;
    this.m=m
    
  }
  
  pat(){
    
    for(i=0;i<=this.n-this.m;i++){
  
     for(j=0;j<this.m;j++){
        if(this.str[i+j]!=this.test[j]){
          break;
      
    }
  } 
  
     if(j==this.m){
        console.log(i);
      }
   
    }
    
  }
  
}

var str="prologue";
n=str.length;
var test="log";
m=test.length;

var obj=new pattern(str,test,n,m);
obj.pat();
