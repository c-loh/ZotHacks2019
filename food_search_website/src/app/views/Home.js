import React, { useState } from 'react';
import { Route, Switch, Router } from 'react-router-dom';
import axios from "axios"

import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

function Home(){

    const [foodName, setFoodName] = useState("")

    function handleInputChange(e) {
        setFoodName(e.target.value);
        //console.log(foodName);
    }

    function handleSubmit(e) {
        e.preventDefault()  // makes sure it doesn't re-render the whole page after submitting
        // send to backend --> axios
        axios.post('http://localhost:3000/answer', "").then(res => {
            console.log(res.data);
          }).catch(err => {
            console.log("IT DIDNT WORK");
          })
    }

    return (
        <div>
            <h1>Food Search</h1>
            <Form>
                <Form.Label>Enter food:</Form.Label>
                <p></p>
                <Form.Control name="food" onChange={handleInputChange}></Form.Control>
                <p></p>
                <Button onClick={handleSubmit}>Submit</Button>
            </Form>
        </div>
    )
}

export default Home;