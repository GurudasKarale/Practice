class Game extends React.Component{
  
  render(){
  
  return(
      <div className="games">
        <h2>{this.props.name}</h2>
        <p>{this.props.description}</p>
      </div>
  );
 }
}


var app=(
<div>
  <Game name="CS:GO" description="Highly competitive fps video game."/>
  <Game name="League of legends" description="Award winning MOBA game."/>
</div>
);

ReactDOM.render(app,document.querySelector('#app'));
