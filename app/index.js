var React = require('react');
var ReactDOM = require('react-dom');
require('./index.css');

//Component is concerned with:
//state
//lifesycle event
//UI (the only part that is absolutely required)

class App extends React.Component { //component definition
    render() {
        return ( 
            <div>Hello World!</div>
        );
    }
}

ReactDOM.render( 
    <App />,
    document.getElementById('app')
);

const cardContainer = document.querySelector('.react-card');

// React component for the frontside of the card
class CardFront extends React.Component {
 render() {
  return(
   <div className='card-side side-front'>
    <div className="panel row">
        <div className="five columns"><img src="{% static 'images/natcon_how_icon.png' %}" />
            </div>
            <div className="seven columns">
              <center>
                <h4 style={{marginBottom : 14}}><strong><a href="/community/natcon2017/">Read more</a></strong> about 2017<br />National Convention</h4>
              <hr />
            	<h4 style={{marginTop: 10}}>Riḍván 2017 <strong><a href="https://s3.amazonaws.com/natcon2017.bahai.us/docs/2017-NSA-annual-report.pdf">Annual Report</a></strong></h4>
              </center>
            </div>
    </div>
  </div>

  )
 }
}
                              

// React component for the backside of the card
class CardBack extends React.Component {
 render() {
  return(
   <div className='card-side side-back'>
      <span className="dice dice-1" title="Dice 1"></span>
      <span className="dice dice-2" title="Dice 2"></span>
      <span className="dice dice-3" title="Dice 3"></span>
      <span className="dice dice-4" title="Dice 4"></span>
      <span className="dice dice-5" title="Dice 5"></span>
      <span className="dice dice-6" title="Dice 6"></span>
      <div id="display"></div>
    </div>
  )
 }
}


// React component for the card (main component)
class Card extends React.Component {
 render() {
  return(
   <div className='card-container'>
    <div className='card-body' id='flipper'>
     <CardBack />

     <CardFront />
    </div> 
   </div>
  )
 }
}

// Render Card component
ReactDOM.render(<Card />, cardContainer);