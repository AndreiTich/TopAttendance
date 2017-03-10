import React, { Component } from 'react';

import Button from './components/Button'
import logo from './logo.svg';
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
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to the course</h2>
        </div>
        <div> {this.state.code} </div>
        <Button
            title="Get Code"
            onClick={() => this.onButtonClick()}/>
      </div>
    );
  }

}

export default App;
