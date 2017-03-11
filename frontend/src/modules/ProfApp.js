import React, { Component } from 'react';

import '../App.css';
import '../index.css';
import axios from 'axios';
import { Button, Row, Col, Icon, Input, Navbar, NavItem } from 'react-materialize';


class ProfApp extends Component {
  constructor(props) {
    super(props);
    this.state = {
        code: '',
        position: null
    };
  }

getLocation = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.updateLocation);
    }
}

  updateLocation = (position) => {
    console.log(position)
    this.setState({
        position: position
    })

    axios.post('/prof/attendance-code/', {
     latitude: position.coords.latitude,
     longitude: position.coords.longitude
    })
    .then((response) => {
         console.log(response)
         this.setState({
             status: response.status,
             code: response.data.code
         })
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  onButtonClick = () => {
   console.log('Sending location and getting code!');
   this.getLocation();
  }

  render() {
    return (
      <div className="App">
      <Navbar brand='Introduction to Computer Science' className="light-blue lighten-1">
      </Navbar>
        <div className="App-details">
            <p className="App-intro">Attendance Code</p>
            <p className="App-code">{this.state.code}</p>
        </div>
        <div className="App-Button">
          <Button waves='light' onClick={this.onButtonClick} center>Get Code</Button>
        </div>
      </div>
    );
  }

  getPositionDisplay() {
    const position = this.state.position
    if (!position) {
        return null
    }
    return (
        <div>
            lat: {position.coords.latitude} lon: {position.coords.longitude}
        </div>
    )
  }

}

export default ProfApp;
