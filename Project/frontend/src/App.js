import React from "react";
import Home from "./Components/Home/Home.js";
import Insights from "./Components/Insights/Insights.js";
import Account from "./Components/Account/Account.js";
import Navbar from "./Components/Navbar/Navbar.js";
import Explore from "./Components/Explore/Explore.js";
import Button from "@material-ui/core/Button";
import Tabs from "@material-ui/core/Tabs"

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


export default function App() {
  return (
    <div>
      <Button>test</Button>
    <Router>
      <div>
        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Navbar />
        <Switch>
          <Route path="/insights">
            <Insights />
          </Route>
          <Route path="/explore">
            <Explore />
          </Route>
          <Route path="/Account">
            <Account />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
    </div>
  );
}

function Home() {
  return <h2>Home</h2>;
}

function Insights() {
  return <h2>Insights</h2>;
}

/*
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
**/
