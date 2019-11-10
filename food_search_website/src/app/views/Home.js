import React from 'react';
import { Route, Switch, Router } from 'react-router-dom';

import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

function Home(){

    function handleInputChange(e) {

    }

    function handleSubmit(e) {

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