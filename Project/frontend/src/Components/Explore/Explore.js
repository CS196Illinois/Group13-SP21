import React from 'react';
import './Explore.css';

const Explore = (props) => {

    return (
        <div className="Explore">
            <header className="Explore-header"></header>
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
                </tr>
                <tr>
                    <td>Amazon</td>
                    <td>$4</td>
                    <td>75%</td>
                    <td>Buy</td>
                </tr>
                <tr>
                    <td>Apple</td>
                    <td>$1</td>
                    <td>86%</td>
                    <td>Strong Buy</td>
                </tr>
                <tr>
                    <td>Facebook</td>
                    <td>$10</td>
                    <td>66%</td>
                    <td>Hold</td>
                </tr>
                <tr>
                    <td>Starbucks</td>
                    <td>$2</td>
                    <td>92%</td>
                    <td>Buy</td>
                </tr>
            </table>
        </div>
    );
}

export default Explore;