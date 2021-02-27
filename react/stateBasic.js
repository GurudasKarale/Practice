class  App extends React.Component{
  
  state={name:"mohit"}
  newname=()=>{
    
    this.setState({name:"rohit"})
  }
  render(){
    return(
    <div>
      <div>{this.state.name}</div>
      <button onClick={this.newname}>click me</button>
    </div> 
   )
    
    
  }
  
  
} 
ReactDOM.render(<App/>, document.getElementById('root'));

//<div id="root"> </div>