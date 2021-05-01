import React from 'react';
import logo from '../../images/Analytica.png';
import'./Home.css';
import Button from "@material-ui/core/Button";
import line from '../../images/line.png';

const Home = (props) => {
    return (
        <div className="Home">
        <header className="Home-header">
        <img src={logo} className="Home-logo" alt="logo"/>
        <img src={line} className="Line" alt="line"/>
        <p>
          Stock Prediction At Your Fingertips.
        </p>
        <a>
          Click <Button href="/explore" color="primary" size="large">Explore</Button> to pick which industries you want us to analyze! 
        </a>
      </header>
    </div>
    );
}

export default Home;