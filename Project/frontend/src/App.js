import React from "react";
import Home from "./Components/Home/Home.js";
import Insights from "./Components/Insights/Insights.js";
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
        <Navbar />
        <Switch>
          <Route path="/insights">
            <Insights />
          </Route>
          <Route path="/explore">
            <Explore />
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