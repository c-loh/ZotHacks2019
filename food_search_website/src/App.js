import React from 'react';
import { Route, Switch, Router } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import history from './history';
import Home from './app/views/Home'
import Answer from './app/views/Answer'

function App() {
  return (
  <div className='App'>
    <Router history={history}>
      <Switch>
        <Route exact path='/' component={Home}/>
        <Route exact path='/answer' component={Answer}/>
      </Switch>
    </Router>
  </div>
  );
}

export default App;
