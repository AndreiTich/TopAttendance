import React, { Component } from 'react';
import { Button, Row, Col, Icon, Input, Navbar } from 'react-materialize';

import '../App.css';
import '../index.css';
import axios from 'axios';

class StudentApp extends Component {
  constructor(props) {
    super(props);
    this.state = {
        code: '',
        status: null
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

    axios.post('/student/attendance-code/', {
     student_id: this.state.student_id,
     code: this.state.code,
     latitude: position.coords.latitude,
     longitude: position.coords.longitude
    })
    .then((response) => {
         console.log(response)
         this.setState({
             status: response.status
         })
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  onButtonClick = () => {
   console.log('Button clicked!');
   this.getLocation();
  }

  handleStudentId = (e) => {
     this.setState({student_id: e.target.value});
  }

  handleCode = (e) => {
     this.setState({code: e.target.value});
  }

  renderStatus = () => {
    const status = this.state.status
    if (!status) {
        return null
    }

    if (status == 200) {
        return (
            <div>
                Your attendance has been accepted
            </div>
        )
    }
  }

  render() {
    return (
      <div className="App">
        <Navbar brand='Introduction to Computer Science' left className="light-blue lighten-1">
        </Navbar>
        <div className="App-details">
          <Row>
              <Input s={6} label="Student ID" onChange={this.handleStudentId}/>
              <Input s={6} label="Code" onChange={this.handleCode}/>
          </Row>
          <Col s={6} center>
            <Button waves='light' onClick={this.onButtonClick}>Submit</Button>
          </Col>
        </div>
        {this.renderStatus()}
      </div>
    );
  }

}

export default StudentApp;
