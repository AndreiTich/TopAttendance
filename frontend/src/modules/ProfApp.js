import React, { Component } from 'react';

import '../App.css';
import axios from 'axios';
import { Button, Row, Col, Icon, Input, Navbar, NavItem } from 'react-materialize';


class ProfApp extends Component {
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
      <Navbar brand='Introduction to Computer Science' left className="light-blue lighten-1">
      </Navbar>
        <div className="App-details">
            <p className="App-intro">Attendance Code</p>
            <p className="App-code">{this.state.code}</p>
        </div>
        <div>
          <Button waves='light' onClick={this.onButtonClick} center>Get Code</Button>
        </div>
      </div>
    );
  }

}

export default ProfApp;
