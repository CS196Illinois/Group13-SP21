import React from 'react';
import './Explore.css';
import { Link } from 'react-router-dom';
//import logo from '../../images/Apple.png';
//import logo from '../../images/Amazon.png';
//import logo from '../../images/fb.png';
//import logo from '../../images/Starbucks.png';

const Explore = (props) => {

    return (
        <div className="Explore">
            <header className="Explore-header">Explore</header>
            <h2 className="Apple-Header"></h2>
            <h2 className="Starbucks-Header"></h2>
            <h2 className="Amazon-Header"></h2>
            <h2 className="Facebook-Header"></h2>
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