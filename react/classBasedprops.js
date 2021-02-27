class Welcome extends React.Component{
  
  render(){
    
    return(
    
      <h1>{this.props.name}</h1>
    );
  }
}
ReactDOM.render(<Welcome name="mohit"/>,document.getElementById('root'));

<div id="root"></div