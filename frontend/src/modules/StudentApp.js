import React, { Component } from 'react';
import { Button, Row, Col, Icon, Input, Navbar } from 'react-materialize';

import '../App.css';
import '../index.css';
import axios from 'axios';

class StudentApp extends Component {
  constructor(props) {
    super(props);
    this.state = {code: '   '};
  }

  onButtonClick = () => {
   console.log('Button clicked!');
   axios.post('/student/attendance-code/', {
    student_id: this.state.student_id,
    code: this.state.code,
    latitude: '00',
    longitude: '00'
   })
   .then((response) => {
     console.log(response);
   })
   .catch(function (error) {
     console.log(error);
   });
  }

  handleStudentId = (e) => {
    console.log(e.target.value);
     this.setState({student_id: e.target.value});
  }

  handleCode = (e) => {
     this.setState({code: e.target.value});
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
      </div>
    );
  }

}

export default StudentApp;
