import React from 'react';
import'./Home.css';
import logo from '../../images/Analytica.png'

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
          Placeholder
        </a>
      </header>
    </div>
    );
}

export default Home;