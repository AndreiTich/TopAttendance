import React, { Component } from 'react';

import Button from './components/Button'
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <Button
            title="Test"
            onClick={() => console.log('look a button!')}/>
      </div>
    );
  }
}

export default App;
