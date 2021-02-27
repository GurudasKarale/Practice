class App extends React.Component{
  
  state={data:[1,2,3,4,5]};
  render(){
    
    return(
    
     <div>{this.state.data.map((user)=>(<div><li>{user}</li></div>))}</div>
    );
  };
  
}
ReactDOM.render(<App/>,document.getElementById('root'));

//<div id="root"></div>