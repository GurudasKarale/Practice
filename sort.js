class sortt{
		
     constructor(a,n){
	  this.a=a;
          this.n=n;
	}
				
     sor(){
	for(i=0;i<n-1;i++){
		for( j=0;j<n-i-1;j++){
			if(a[j]>a[j+1]){
                           [a[j],a[j+1]]=[a[j+1],a[j]];
				}
			}	
		}
	     return a;
	}
}
var a=[64, 34, 25, 12, 22, 11, 90];
n=a.length;
var obj=new sortt(a,n);
result=obj.sor();
console.log(result);



		
