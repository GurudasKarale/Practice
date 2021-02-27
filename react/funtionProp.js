function Namelist(props){
  
  const mylist=props.list;
  const listitem=mylist.map((user)=><div>{user}</div>);
   return(
        <div>{listitem}</div>);                         
  
}

const mylist=[1,2,3,4,5];
ReactDOM.render(<Namelist list={mylist}/>,document.getElementById('root'));
<div id="root"></div>