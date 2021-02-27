class App extends React.Component{
  
  constructor(props){
    super(props);
    this.state={value:''};
    
  }
  
  handleChange=(event)=>{
    this.setState({value:event.target.value})
    
  }
 
  handleSubmit=(event)=>{
    
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
    
  }
  render(){
    return(
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            name:
            <input type="text" value={this.state.value} onChange={this.handleChange}/>
            
          </label>
         <input type="submit" value="submit"/> 
        </form> 
        
      </div>
    );
  }
}

ReactDOM.render(<App/>,document.getElementById('root'));

<div id="root"></div>