import React, { Component, useState } from 'react'
import { Link, useHistory } from 'react-router-dom';
import { Container, TextField, Button, Grid, Typography } from '@material-ui/core';
import chineseDragon from '../vectors/cherry-chinese-dragon.png'
import sittingOnTheMoon from '../vectors/cherry-sitting-on-the-moon.png'





export default function RoomJoinPage() {

    const [state, setState] = useState({code: '', error: '', helper: ''})
    const history = useHistory()

    const handleCodeChange = e => setState({code: e.target.value})
    const handleButtonPressed = () => {
        fetch('http://127.0.0.1:8000/api/' + state.code + '/', {
            method: 'get',
            headers: {
                'Authorization': `Token ${sessionStorage.getItem('token')}`,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                history.push(`/room/${state.code}/`)
            } else {
                setState({error: true, helper: 'Oda bulunamadı'})
            }
        })
        .catch(err => console.error(err))
    }

    return (
        <div className='jac'>
            <Container>
                <div classname='vector-container'>
                    <img src={chineseDragon} style={{ width: '30rem' }} className='vector bottom-right transform' />
                    <img src={sittingOnTheMoon} style={{ width: '30rem' }} className='vector top-left transform' />
                </div>
                <Grid container spacing={1} alignItems='center'>
                    <Grid item xs={12} align='center'>
                        <Typography variant='h4' component='h4'>
                            Join a Room
                        </Typography>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <TextField error={state.error} helperText={state.helper} label='Kod: ' variant='outlined' onChange={handleCodeChange} />
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <Button variant='contained' color='primary' onClick={handleButtonPressed}>
                            Enter Room
                        </Button>
                    </Grid>
                    <Grid item xs={12} align='center'>
                    <Button variant='contained' color='secondary' to='/' component={Link}>
                            Back
                        </Button>
                    </Grid>
                </Grid>
            </Container>
        </div>
    )
}
