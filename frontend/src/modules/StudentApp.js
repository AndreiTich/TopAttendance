import React, { Component } from 'react';

import Button from '../components/Button'
import '../App.css';
import axios from 'axios';


class StudentApp extends Component {
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

        <form action="/student/attendance-code">
          StudentID:<br/>
          <input type="text" name="student_id" value="12345678"/><br/>
          Code:<br/>
          <input type="text" name="code" value="0000"/><br/><br/>
          <input type="submit" value="Submit"/>
        </form>

        </div>
      </div>
    );
  }

}

export default StudentApp;
