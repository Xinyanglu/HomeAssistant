import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

class Toggle extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            active: false,
        };
    }

    clicked(){
        this.setState({
            active: !this.state.active,
        });
        var xhr = new XMLHttpRequest()
        xhr.addEventListener('load', () => {
            console.log(xhr.responseText)
        })
        xhr.open('POST', 'http://localhost:5000/getValueFromLightSwitch')
        xhr.send(JSON.stringify({status: this.state.active}))
    }

    render(){
        return(
            <div>
                <div className = "container">
                    <h2 className = "light-heading">Light Switch</h2>
                    <div className = {this.state.active ? "toggle-btn  active":"toggle-btn"} onClick = {() => this.clicked()}>
                        <div className = "circle">

                        </div>
                    </div>
                </div>
            </div>
        );
    }

    
}




ReactDOM.render(
    <Toggle />,
    document.getElementById('root')
);