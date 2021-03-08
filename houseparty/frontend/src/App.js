import React, { Component } from 'react'
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from 'react-router-dom'
import HomePage from './components/HomePage'
import Room from './components/Room'
import RoomJoinPage from './components/RoomJoinPage'
import RoomCreatePage from './components/RoomCreatePage'

export default class App extends Component {
  render() {
    return (
      <div>
        <Router>
          <Switch>
            <Route exact path='/' component={HomePage} />
            <Route path='/room/:code' component={Room} />
            <Route path='/join' component={RoomJoinPage} />
            <Route path='/create' component={RoomCreatePage} />
          </Switch>
        </Router>
      </div>
    )
  }
}
