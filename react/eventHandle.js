
class Example extends React.Component {
  
    state = {
      count: 0
    }
   handleChange=()=>{
    
    this.setState({count:this.state.count+1})
  }
  render() {
    return (
      <div>
        <p>You clicked {this.state.count} times</p>
        <button onClick={this.handleChange}>
          Click me
        </button>
      </div>
    );
  }
}
ReactDOM.render(<Example/>,document.getElementById('root'));
<div id="root"></div>