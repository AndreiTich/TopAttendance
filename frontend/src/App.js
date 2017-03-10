import React, { Component } from 'react';

import Button from './components/Button'
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {code: ''};
  }

    onClick = () => {
        console.log('button!')
        this.setState({code: '1234'})
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
            onClick={this.onClick}/>
      </div>
    );
  }
}

export default App;
