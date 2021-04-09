import React from 'react';
import logo from './logo.svg';
import'./Home.css';

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