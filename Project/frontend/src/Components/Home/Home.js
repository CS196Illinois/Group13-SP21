import React from 'react';
import logo from '../../images/Analytica LOGO.png';
import'./Home.css';
import Button from "@material-ui/core/Button";

const Home = (props) => {

    return (
        <div className="Home">
        <header className="Home-header">
        <img src={logo} className="Home-logo" alt="logo" />
        <p>
          Stock Prediction At Your Fingertips.
        </p>
        <a
        >
          Click <Button href="/explore" color="primary">Explore</Button> to pick which industries you want us to analyze! 
        </a>
      </header>
    </div>
    );
}

export default Home;