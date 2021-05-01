import React from 'react';
import './Explore.css';
import { Link } from 'react-router-dom';
import amazon from '../../images/Amazon.webp';
import apple from '../../images/Apple.png';
import fb from '../../images/fb.png';
import sb from '../../images/sb.png';

const Explore = (props) => {

    return (
        <div class="flex-container" className="Explore">
            {/* <div><img src={amazon} className="Amazon-logo" alt="amazon" /></div> */}
            <div className="flex-container">
            <div><img src={amazon} className="amazon" alt="amazon"/></div>
            <div><img src={apple} className="apple" alt="apple"/></div>
            <div><img src={fb} className="fb" alt="fb"/></div>
            <div><img src={sb} className="sb" alt="sb"/></div>
            </div>
            <header className="Explore-header">Explore</header>
            <p>We have four companies for you to choose from! 
            </p>
            <table>
                <tr>
                    <th>Company</th>
                    <th>Price</th>
                    <th>Certainty</th>
                    <th>Consensus</th>
                    <th>Charts</th>
                </tr>
                <tr>
                    <td>Amazon</td>
                    <td>$4</td>
                    <td>75%</td>
                    <td>Buy</td>
                    <td><Link to="/Insights">View Charts</Link></td>
                </tr>
                <tr>
                    <td>Apple</td>
                    <td>$1</td>
                    <td>86%</td>
                    <td>Strong Buy</td>
                    <td><Link to="/Insights">View Charts</Link></td>
                </tr>
                <tr>
                    <td>Facebook</td>
                    <td>$10</td>
                    <td>66%</td>
                    <td>Hold</td>
                    <td><Link to="/Insights">View Charts</Link></td>
                </tr>
                <tr>
                    <td>Starbucks</td>
                    <td>$2</td>
                    <td>92%</td>
                    <td>Buy</td>
                    <td><Link to="/Insights">View Charts</Link></td>
                </tr>
            </table>
        </div>
    );
}

export default Explore;