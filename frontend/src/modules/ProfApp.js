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
        position: null,
        num_students: 0
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
     longitude: position.coords.longitude,
     accuracy: position.coords.accuracy
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

  timer = () => {
    axios.get('/prof/students', {
      params: {
        code: this.state.code
      }
    })
    .then((response) => {
         console.log(response)
         this.setState({
             status: response.status,
             num_students: response.data.num_of_students
         })
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  onButtonClick = () => {
   console.log('Sending location and getting code!');
   this.getLocation();
   var intervalId = setInterval(this.timer, 1000);
  }

  render() {
    return (
      <div className="App">
     <div className='card-panel purple lighten-2 center flow-text'>
            <h3>Introduction to Computer Science</h3>
        </div>
        <div className="App-details">
            <p className="App-intro">Attendance Code</p>
            <p className="App-code">{this.state.code}</p>
        </div>
        <div className="App-Button">
          <Button waves='light' onClick={this.onButtonClick} center>Get Code</Button>
        </div>
        <br></br>
        {this.getNumStudentsDisplay()}
      </div>

    );
  }

  getNumStudentsDisplay() {
    return (
        <div>
            Students attending class: {this.state.num_students}
        </div>
    )
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
