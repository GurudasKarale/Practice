class App extends React.Component{
  
  
  state={
    posts : []
      }
 componentDidMount(){
   
   axios.get('https://jsonplaceholder.typicode.com/posts/')
        .then(res=>{
             console.log(res)
             this.setState({posts: res.data.slice(0,10)
             });
          })
      }
  
  render(){
    
   const{posts}=this.state
   const postList=posts.map(
          post=>{
            
            return(
              <div >
              <span ><h1>{post.title}</h1></span>
              <p>{post.body}</p>
            </div>
                  )
            
          })
    
    
    return(
      <div>
        <div >
          <h4 >POSTS</h4>
          {postList}
        </div>
      </div>
          )
    
  }
  
}

ReactDOM.render(<App/>,document.getElementById('root'));

<div id="root"></div>