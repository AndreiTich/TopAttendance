import React, { Component } from 'react';

import Button from './components/Button'
import './App.css';
import axios from 'axios';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {code: '   '};
  }

  onButtonClick = () => {
   console.log('Button clicked!');
   axios.get('/prof/attendance-code/')
     .then((response) => {
       this.setState({code: response.data.code})
       console.log(response);
     })
     .catch(function (error) {
       console.log(error);
     });
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Intro to Computer Science</h2>
        </div>
        <div className="App-details">
            <p className="App-intro">Attendance Code</p>
            <p className="App-code">{this.state.code}</p>
        </div>
        <Button
            title="Test"
            onClick={this.onButtonClick}/>
      </div>
    );
  }

}

export default App;
