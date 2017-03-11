import React from 'react'
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'
import ProfApp from './modules/ProfApp'
import StudentApp from './modules/StudentApp'

const BasicExample = () => (
  <Router>
    <div>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/student">Student</Link></li>
        <li><Link to="/prof">Prof</Link></li>
      </ul>

      <hr/>

      <Route exact path="/" component={Home}/>
      <Route path="/student" component={StudentApp}/>
      <Route path="/prof" component={ProfApp}/>
    </div>
  </Router>
)

const Home = () => (
  <div>
    <h2>Home</h2>
  </div>
)

const Student = () => (
  <div>
    <h2>Student</h2>
  </div>
)
const Prof = () => (
  <div>
    <h2>Prof</h2>
  </div>
)


export default BasicExample
